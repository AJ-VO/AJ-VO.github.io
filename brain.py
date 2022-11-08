#Result

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

    elif choice == "-1":#Database Information

        #Load Database Data
        playerDATA = load_players()
        resultDATA = load_results()

        #Print Main Menu
        #Shows keys for data entry
        show_database_information(playerDATA, resultDATA)

    elif choice == "1":#Add Game Result
        
        #Load Database Data
        playerDATA = load_players()
        resultDATA = load_results()

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
        with open("jsons/players.json", "w", encoding='utf8') as fr:
            json.dump(playerDATA, fr, indent=4)

        #Dump Result
        #Sort results
        resultDATA.sort(reverse=True, key=lambda x: x["msDate"])
        with open("jsons/results.json", "w", encoding='utf8') as fp:
            json.dump(resultDATA, fp, indent = 4)

        #Loop back to main
        main()

    elif choice =="2":#Add Doubles Result

        #Load Database Data
        playerDATA = load_players()
        resultDATA = load_results()

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
        with open("jsons/players.json", "w", encoding='utf8') as fr:
            json.dump(playerDATA, fr, indent=4)

        #Dump Result
        #Sort results
        resultDATA.sort(reverse=True, key=lambda x: x["msDate"])
        with open("jsons/results.json", "w", encoding='utf8') as fp:
            json.dump(resultDATA, fp, indent = 4)

        #Loop back to main
        main()

    elif choice == "3":#Add Tournament Result
        
        #Create Result Array
        match_data = {}

        #Load Tourament Data
        tournamentPlayersData = load_tournament()
        tournamentResultsData = load_tournament_matches()
        myTeams = load_teams()
        
        #Ask Team
        #jsons/teams.json
        teamsPossible = show_teams()

        #Get and Check Entry
        j = 0
        while j == 0:
            myAnswer = input("Team Key: ")
            #If not in database
            if int(myAnswer) < 0 or int(myAnswer) > teamsPossible-1:
                print("Wrong Input")
                continue
            else:
                teamVS = (int(myAnswer))#Team's Key
                j=j+1

        #Ask Location
        #Home/Away
        j = 0
        while j == 0:#Stop when 1 answers
            myAnswer = input("Home/Away?: ")
            if myAnswer.lower() != "home" and myAnswer.lower() != "away":
                print("Wrong Input")
                continue
            else:
                myLocation = myAnswer.upper()#Location
                j=j+1

        #Create Tournament
        match_data["tourny"] = myTeams[teamVS]["team_tag"]+"#"+myLocation
        #YYYY-MM-DD
        match_data["date"] = "YYYY-MM-DD"
        
        #Get Matches Played

        #Create Entry Loop

        #Loop back to main
        main()

    else:#Error

        print("Error, choice is not in menu")
        #Loop back to main
        main()
        
if __name__ == "__main__":
    main()