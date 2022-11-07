#Result
#A-C Forcier - V Lachance d. C Girard - M Marceau 8-3

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

        ##############################################################
        # NEW PROTOCOL
        ##############################################################
        #Edit the database ASAP

        #Create Result Array
        match_data = {}
        match_data["winner"] = playerDATA[answers[0]]["name"]
        match_data["loser"] = playerDATA[answers[1]]["name"]
        match_data["score"] = input("Score: ")
        match_data["date"] = get_date()
        match_data["winnerELO"] = playerDATA[answers[0]]["elo"]
        match_data["loserELO"] = playerDATA[answers[1]]["elo"]

        #Add GP + 1 for both players
        playerDATA[answers[0]]["gp"] = playerDATA[answers[0]]["gp"] + 1
        playerDATA[answers[1]]["gp"] = playerDATA[answers[1]]["gp"] + 1
        #Add W and L for both players
        playerDATA[answers[0]]["wins"] = playerDATA[answers[0]]["wins"] + 1
        playerDATA[answers[1]]["losses"] = playerDATA[answers[1]]["losses"] + 1
        #Calculate Match Delta
        matchDelta = playerDATA[answers[0]]["elo"]-playerDATA[answers[1]]["elo"]

        #Check Gender and Elo Gains
        if playerDATA[answers[0]]["g"] == "w" and playerDATA[answers[1]]["g"] == "g":#If winner is girl and loser is guy
            playerDATA[answers[0]]["elo"] = playerDATA[answers[0]]["elo"]+(get_eloGain(matchDelta)*2)
            match_data["winnerGain"] = get_eloGain(matchDelta)*2
            playerDATA[answers[1]]["elo"] = playerDATA[answers[1]]["elo"]-get_eloGain(matchDelta)
            match_data["loserGain"] = -get_eloGain(matchDelta)
        elif playerDATA[answers[0]]["g"] == "g" and playerDATA[answers[1]]["g"] == "w":#If winner is guy and loser is girl
            playerDATA[answers[0]]["elo"] = playerDATA[answers[0]]["elo"]+(get_eloGain(matchDelta)/2)
            match_data["winnerGain"] = get_eloGain(matchDelta)/2
            playerDATA[answers[1]]["elo"] = playerDATA[answers[1]]["elo"]-(get_eloGain(matchDelta)/2)
            match_data["loserGain"] = -(get_eloGain(matchDelta)/2)
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

        ##############################################################

    elif choice =="2":#Add Doubles Result

        #Load Database Data
        playerDATA = load_players()
        resultDATA = load_results()
        show_database_information(playerDATA, resultDATA)

        #4 players, 2 winners, 2 losers

        #1
        myPlayers = 0
        myPlayer = []
        while myPlayers < 4:
            myPlayer.append(input("Player ("+str(myPlayers)+")"))
            #If not in database
            myPlayers = myPlayers+1

        information = []

    else:#Error
        print("Error, choice is not in menu")
        #Loop back to main
        main()
    
    """ elif choice == "2":#Add Tournament Result (OFFLINE)
        print_tournament_information()
        with open("jsons/t_players.json", "r", encoding='utf8') as f:
            playerDATA = json.load(f)
        with open("jsons/t_results.json", "r", encoding='utf8') as fp:
            resultDATA = json.load(fp)
        winnerDict = int(input("Winner Key: "))
        loserDict = int(input("Loser Key: "))
        score = input("Score: ")
        tournament = input("Tournament (TEAM#AWAY/HOME)")
        information = []#winnerid, loserid,

        #Player Data
        #Winner
        playerDATA[winnerDict]["gp"] = playerDATA[winnerDict]["gp"] + 1
        playerDATA[winnerDict]["wins"] = playerDATA[winnerDict]["wins"] + 1
        #Loser
        playerDATA[loserDict]["gp"] = playerDATA[loserDict]["gp"] + 1
        playerDATA[loserDict]["losses"] = playerDATA[loserDict]["losses"] + 1
        with open("jsons/t_players.json", "w", encoding='utf8') as fr:
            json.dump(playerDATA, fr, indent=4)
        #Match Data
        match_data = {}
        match_data["winner"] = playerDATA[winnerDict]["name"]
        match_data["loser"] = playerDATA[loserDict]["name"]
        match_data["score"] = score
        match_data["date"] = get_date()
        match_data["tourny"] = tournament
        resultDATA.append(match_data)
        with open("jsons/t_results.json", "w", encoding='utf8') as fr:
            json.dump(resultDATA, fr, indent=4)
        main() """
        
if __name__ == "__main__":
    main()