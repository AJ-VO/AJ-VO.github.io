from utils import *

def main():

    #Database Entry Script
    print_main_menu()

    #Answers Possibles
    options = ["0", "1"]
    #Answer
    choice = input("Input: ")
    #Check

    #Menu
    if choice == "0":#Quit
        #Exits Script
        sys.exit(0)
    elif choice == "1":#Add Game Result
        
        #Load Database Data
        playerDATA = load_players()
        print("Current Players: ")
        resultDATA = load_results()
        print("Matches Played: ")

        #Print Main Menu
        #Shows keys for data entry
        print_database_information()

        #Get and Check Answers
        answers = []
        while len(answers) != 2:#Stop when 2 answers
            myAnswer = input("("+str(len(answers))+")Key: ")
            answers.append(int(myAnswer))
        #Attribute keys
        winnerDict = answers[0]
        loserDict = answers[1]

        #Protocol
        #1 Get Players Ids
        #2 Get Current Elos
        #3 Get Current Genders
        #4 Calculate Match Delta
        #5 Calculate Elo Gains
        #6 Get Names
        #7 Get Streak
        #8 

        #[winnerId(0), loserId(1), winnerELO(2), loserELO(3), winnerG(4), loserG(5), winnerGain(6), loserGain(7), winnerName(8), loserName(9)]
        #List of values needed for changes
        information = []
        information.append(playerDATA[winnerDict]["id"])#0
        information.append(playerDATA[loserDict]["id"])#1
        information.append(playerDATA[winnerDict]["elo"])#2
        information.append(playerDATA[loserDict]["elo"])#3
        information.append(playerDATA[winnerDict]["g"])#4
        information.append(playerDATA[loserDict]["g"])#5

        #Points System
        #Calculate Match Delta
        matchDelta = information[2]-information[3]
        #Attribute Elo Gains
        eloGain = get_eloGain(matchDelta)

        #Check Gender
        if information[4] == information[5]:#If Same
            #Normal attribution
            information.append(eloGain)#W6
            information.append(eloGain*-1)#L7
        else:#If Different
            if information[4] == "w":#If winner is a girl
                #Double Girl Gain
                information.append(eloGain*2)#W6
                information.append(eloGain*-1)#L7
            else:#If winner is a guy
                #Half Girl Loss
                information.append(int(eloGain*0.5))#W6
                #Half Guy Gain
                information.append(int(eloGain*-0.5))#L7

        #Append more values
        information.append(playerDATA[winnerDict]["name"])#8
        information.append(playerDATA[loserDict]["name"])#9
        information.append(playerDATA[winnerDict]["streak"])#10
        information.append(playerDATA[loserDict]["streak"])#11

        #Create Streak
        streaks = []
        for i in range(10, 12):#10-11
            if i == 10:
                ending = True
            else:
                ending = False
            currentStreak = information[i]
            newStreak = playerStreak(currentStreak, ending)
            streaks.append(newStreak)
        playerDATA[winnerDict]["streak"] = streaks[0]
        playerDATA[loserDict]["streak"] = streaks[1]
        
        #Attribute Elo Gains in Database
        playerDATA[winnerDict]["elo"] = playerDATA[winnerDict]["elo"]+information[6]
        playerDATA[loserDict]["elo"] = playerDATA[loserDict]["elo"]+information[7]
        #Add Win, Loss, and Game Played in Database
        playerDATA[winnerDict]["wins"] = playerDATA[winnerDict]["wins"] + 1
        playerDATA[winnerDict]["gp"] = playerDATA[winnerDict]["gp"] + 1
        playerDATA[loserDict]["losses"] = playerDATA[loserDict]["losses"] + 1
        playerDATA[loserDict]["gp"] = playerDATA[loserDict]["gp"] + 1
        
        #Dump player information
        #Sort by elo
        playerDATA.sort(reverse=True, key=lambda x: x["elo"])
        with open("jsons/players.json", "w", encoding='utf8') as fr:
            json.dump(playerDATA, fr, indent=4)

        #Create Result Array
        match_data = {}
        match_data["winner"] = information[8]
        match_data["loser"] = information[9]
        match_data["score"] = input("Score: ")
        match_data["date"] = get_date()
        match_data["winnerELO"] = information[2]
        match_data["loserELO"] = information[3]
        match_data["winnerGain"] = information[6]
        match_data["loserGain"] = information[7]
        match_data["msDate"] = get_ms_date()
        #Append to current results.json
        resultDATA.append(match_data)

        #Dump results
        #Sort results
        resultDATA.sort(reverse=True, key=lambda x: x["msDate"])
        with open("jsons/results.json", "w", encoding='utf8') as fp:
            json.dump(resultDATA, fp, indent = 4)

        #Loop back to main
        main()
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