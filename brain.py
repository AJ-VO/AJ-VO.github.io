from utils import *

def main():

    #Database Entry Script
    print_main_menu()

    #Answer
    choice = input("Input: ")

    #Menu
    if choice == "0":#Quit

        #Exits Script
        sys.exit(0)

    elif choice =="-3":#Add Team Player

        #json
        teamData = load_data('teams')

        #returned # of teams
        tp = show_teams()

        teamIndex = int(input("Team Index: "))

        addingStatus = False
        while addingStatus == False:
            player = input("Adding: ")
            if player == "0":
                addingStatus = True
            else:
                teamData[teamIndex]["players"].append(player)
                print("Added "+player+" to ["+teamData[teamIndex]["team_tag"]+"]")

        #dump
        dump_json_file("teams", teamData)

        #loop back to main
        main()

    elif choice == "-2":#Add Player

        #json
        playerData = load_data('players')

        playerDict = {}
        #Name
        playerDict["name"] = input("Name: ")
        #Gender
        genderResolved = False
        while genderResolved == False:
            answer = input("Gender (W/G): ")
            if (answer.lower() == "w") or (answer.lower() == "g"):
                playerDict["g"] = answer.lower()
                genderResolved = True
            else:
                print("Bad Gender Input")
            
        #append all ids in matrix
        myIds = [[], []]#[fille, gars]
        for i in playerData:
            if i["id"] < 100:#fille
                myIds[0].append(i["id"])
            else:#gars
                myIds[1].append(i["id"])

        if playerDict["g"] == "w":
            playerDict["id"] = max(myIds[0])+1
        else:
            playerDict["id"] = max(myIds[1])+1
        
        playerDict["gp"] = 0
        playerDict["wins"] = 0
        playerDict["losses"] = 0
        playerDict["elo"] = 1500
        playerDict["t_wins"] = 0
        playerDict["t_losses"] = 0
        playerDict["img"] = "img/players/test.png"
        playerDict["streak"] = 0

        #append and sort
        playerData.append(playerDict)
        playerData.sort(reverse=True, key=lambda x: x["elo"])
        print("Added "+playerDict["name"]+" id("+str(playerDict["id"])+") to databse")
        #dump
        dump_json_file("players", playerData)
        #loop back to main
        main()

    elif choice == "-1":#Database Information

        #json
        playerDATA = load_data('players')
        resultDATA = load_data('results')

        #Print Main Menu
        #Shows keys for data entry
        show_database_information(playerDATA, resultDATA)

    elif choice == "1":#Add Game Result
        
        #Load Database Data
        playerDATA = load_data('players')
        resultDATA = load_data('results')

        #Print Players for entry
        playersPossible = print_database_information()

        #Get and Check Entry
        answers = []
        while len(answers) != 2:#Stop when 2 answers
            myAnswer = input("("+str(len(answers))+")Key: ")
            #If not in database
            if int(myAnswer) < 0 or int(myAnswer) > playersPossible-1:
                print("Wrong Input")
                continue
            answers.append(int(myAnswer))

        #Create Result Array
        match_data = {}
        match_data["winner"] = playerDATA[answers[0]]["name"]
        match_data["loser"] = playerDATA[answers[1]]["name"]
        match_data["score"] = input("Score: ")
        match_data["date"] = get_date()
        match_data["winnerELO"] = playerDATA[answers[0]]["elo"]
        match_data["loserELO"] = playerDATA[answers[1]]["elo"]

        #Add GP + 1 for both players
        for i in range(0, 2):
            playerDATA[answers[i]]["gp"] = playerDATA[answers[i]]["gp"] + 1
        #Add W and L for both players
        playerDATA[answers[0]]["wins"] = playerDATA[answers[0]]["wins"] + 1
        playerDATA[answers[1]]["losses"] = playerDATA[answers[1]]["losses"] + 1
        #Calculate Match Delta
        matchDelta = match_data["winnerELO"]-match_data["loserELO"]

        #Check Gender and Elo Gains
        if playerDATA[answers[0]]["g"] == "w" and playerDATA[answers[1]]["g"] == "g":#If winner is girl and loser is guy
            playerDATA[answers[0]]["elo"] = playerDATA[answers[0]]["elo"]+(get_eloGain(matchDelta)*2)
            match_data["winnerGain"] = get_eloGain(matchDelta)*2
            playerDATA[answers[1]]["elo"] = playerDATA[answers[1]]["elo"]-get_eloGain(matchDelta)
            match_data["loserGain"] = -get_eloGain(matchDelta)
        elif playerDATA[answers[0]]["g"] == "g" and playerDATA[answers[1]]["g"] == "w":#If winner is guy and loser is girl
            playerDATA[answers[0]]["elo"] = playerDATA[answers[0]]["elo"]+(int(get_eloGain(matchDelta)/2))
            match_data["winnerGain"] = int(get_eloGain(matchDelta)/2)
            playerDATA[answers[1]]["elo"] = playerDATA[answers[1]]["elo"]-(int(get_eloGain(matchDelta)/2))
            match_data["loserGain"] = int(-(get_eloGain(matchDelta)/2))
        else:#Same Gender
            playerDATA[answers[0]]["elo"] = playerDATA[answers[0]]["elo"]+get_eloGain(matchDelta)
            match_data["winnerGain"] = get_eloGain(matchDelta)
            playerDATA[answers[1]]["elo"] = playerDATA[answers[1]]["elo"]-get_eloGain(matchDelta)
            match_data["loserGain"] = -(get_eloGain(matchDelta))

        #Streak Winner
        if playerDATA[answers[0]]["streak"] <= 0:
            playerDATA[answers[0]]["streak"] = 1
        else:
            playerDATA[answers[0]]["streak"] = playerDATA[answers[0]]["streak"]+1
        #Streak Loser
        if playerDATA[answers[1]]["streak"] <= 0:
            playerDATA[answers[1]]["streak"] = playerDATA[answers[1]]["streak"]-1
        else:
            playerDATA[answers[1]]["streak"] = -1

        #Append to current results.json
        match_data["msDate"] = get_ms_date()
        resultDATA.append(match_data) 

        #Dump Players
        #Sort by elo
        playerDATA.sort(reverse=True, key=lambda x: x["elo"])
        dump_json_file("players", playerDATA)

        #Dump Result
        #Sort results
        resultDATA.sort(reverse=True, key=lambda x: x["msDate"])
        dump_json_file("results", resultDATA)

        #Loop back to main
        main()

    elif choice =="2":#Add Doubles Result

        #Load Database Data
        playerDATA = load_data('players')
        resultDATA = load_data('results')

        #Print Players for entry
        playersPossible = print_database_information()

        #Get and Check Entry
        answers = []
        while len(answers) != 4:#Stop when 4 answers
            myAnswer = input("("+str(len(answers))+")Key: ")
            #If not in database
            if int(myAnswer) < 0 or int(myAnswer) > playersPossible-1:
                print("Wrong Input")
                continue
            answers.append(int(myAnswer))

        #Create Result Array
        match_data = {}
        match_data["winner"] = playerDATA[answers[0]]["name"]+"/"+playerDATA[answers[1]]["name"]
        match_data["loser"] = playerDATA[answers[2]]["name"]+"/"+playerDATA[answers[3]]["name"]
        match_data["score"] = input("Score: ")
        match_data["date"] = get_date()
        match_data["winnerELO"] = int((playerDATA[answers[0]]["elo"]+playerDATA[answers[1]]["elo"])/2)
        match_data["loserELO"] = int((playerDATA[answers[2]]["elo"]+playerDATA[answers[3]]["elo"])/2)

        #Add GP + 1 for players
        for i in range(0, 4):
            playerDATA[answers[i]]["gp"] = playerDATA[answers[i]]["gp"] + 1

        #Add W and L for both players
        playerDATA[answers[0]]["wins"] = playerDATA[answers[0]]["wins"] + 1
        playerDATA[answers[1]]["wins"] = playerDATA[answers[1]]["wins"] + 1
        playerDATA[answers[2]]["losses"] = playerDATA[answers[2]]["losses"] + 1
        playerDATA[answers[3]]["losses"] = playerDATA[answers[3]]["losses"] + 1
        #Calculate Match Delta
        matchDelta = match_data["winnerELO"]-match_data["loserELO"]

        #Elo Gains
        playerDATA[answers[0]]["elo"] = playerDATA[answers[0]]["elo"] + int(get_eloGain(matchDelta)/3)
        playerDATA[answers[1]]["elo"] = playerDATA[answers[1]]["elo"] + int(get_eloGain(matchDelta)/3)
        playerDATA[answers[2]]["elo"] = playerDATA[answers[2]]["elo"] - int(get_eloGain(matchDelta)/3)
        playerDATA[answers[3]]["elo"] = playerDATA[answers[3]]["elo"] - int(get_eloGain(matchDelta)/3)
        match_data["winnerGain"] = int(get_eloGain(matchDelta)/3)
        match_data["loserGain"] = -int(get_eloGain(matchDelta)/3)
        
        #Streaks

        #Append to current results.json
        match_data["msDate"] = get_ms_date()
        resultDATA.append(match_data)

        #Dump Players
        #Sort by elo
        playerDATA.sort(reverse=True, key=lambda x: x["elo"])
        dump_json_file("players", playerDATA)

        #Dump Result
        #Sort results
        resultDATA.sort(reverse=True, key=lambda x: x["msDate"])
        dump_json_file("results", resultDATA)

        #Loop back to main
        main()

    elif choice == "3":#Add Tournament Result (WIP)
        
        #Create Result Array
        match_data = {}

        #protocol
        #choose team
        #choose player
        
        #loop till done

        #Load
        #Player Data
        playerDATA = load_data('players')

        print(playerDATA)

        #Loop back to main
        main()

    else:#Error

        print("Error, choice is not in menu")
        #Loop back to main
        main()
        
if __name__ == "__main__":
    main()