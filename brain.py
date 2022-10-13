from utils import *

def main():

    print_main_menu()
    choice = input("Input: ")
    if choice == "0":
        print_database_information()
        main()
    elif choice == "1":
        with open("jsons/players.json", "r", encoding='utf8') as f:
            playerDATA = json.load(f)
        with open("jsons/results.json", "r", encoding='utf8') as fp:
            resultDATA = json.load(fp)

        print_database_information()
        
        winnerDict = int(input("Winner Key: "))
        loserDict = int(input("Loser Key: "))

        information = []#[winnerId(0), loserId(1), winnerELO(2), loserELO(3), winnerG(4), loserG(5), winnerGain(6), loserGain(7), winnerName(8), loserName(9)]
        information.append(playerDATA[winnerDict]["id"])#0
        information.append(playerDATA[loserDict]["id"])#1
        information.append(playerDATA[winnerDict]["elo"])#2
        information.append(playerDATA[loserDict]["elo"])#3
        information.append(playerDATA[winnerDict]["g"])#4
        information.append(playerDATA[loserDict]["g"])#5

        matchDelta = information[2]-information[3]

        eloGain = get_eloGain(matchDelta)

        if information[4] == information[5]:
            information.append(eloGain)#W6
            information.append(eloGain*-1)#L7
        else:
            if information[4] == "w":
                information.append(eloGain*2)#W6
                information.append(eloGain*-1)#L7
            else:
                information.append(eloGain*0.5)#W6
                information.append(eloGain*-0.5)#L7

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
        
        #Change ELO
        playerDATA[winnerDict]["elo"] = playerDATA[winnerDict]["elo"]+information[6]
        playerDATA[loserDict]["elo"] = playerDATA[loserDict]["elo"]+information[7]
        #Add win and losses
        playerDATA[winnerDict]["wins"] = playerDATA[winnerDict]["wins"] + 1
        playerDATA[winnerDict]["gp"] = playerDATA[winnerDict]["gp"] + 1
        playerDATA[loserDict]["losses"] = playerDATA[loserDict]["losses"] + 1
        playerDATA[loserDict]["gp"] = playerDATA[loserDict]["gp"] + 1
        #Dump player information
        playerDATA.sort(reverse=True, key=lambda x: x["elo"])
        with open("jsons/players.json", "w", encoding='utf8') as fr:
            json.dump(playerDATA, fr, indent=4)
        #Create Result
        match_data = {}
        match_data["winner"] = information[8]
        match_data["loser"] = information[9]
        match_data["score"] = input("Score: ")
        match_data["date"] = get_date()
        match_data["winnerELO"] = information[2]
        match_data["loserELO"] = information[3]
        match_data["winnerGain"] = information[6]
        match_data["loserGain"] = information[7]
        resultDATA.append(match_data)
        with open("jsons/results.json", "w", encoding='utf8') as fp:
            json.dump(resultDATA, fp, indent = 4)
        main()
    elif choice == "2":
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
        main()
    else:
        main()
        
if __name__ == "__main__":
    main()