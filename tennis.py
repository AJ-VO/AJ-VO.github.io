#Imports
import json
import sys
import time
import random

#Functions Library

#load a file
def load_file(file):
    with open('jsons/'+file+'.json', 'r') as f:
        data = json.load(f)
    return data

#dump content in file
def dump_file(file, content):
    with open('jsons/'+file+'.json', 'w') as f:
        json.dump(content, f, indent=4)

#tennis score system conversion
def print_score(currentScore):
    scoreDict = {
        0: "0",
        1: "15",
        2: "30",
        3: "40",
        4: "G"
    }
    print(scoreDict[currentScore[0]]+"-"+scoreDict[currentScore[1]])

#binary
def opposite(player):
    if player == 0:
        return 1
    else:
        return 0

#Main Functions

def main():

    print("Tennis - jaZZ")
    print("starting match...")

    #name of players
    players = ["Alex", "Pascal"]
    #start time
    startTime = 0
    #start match
    my_match(players)

def my_match(players):

    #if tiebreak during set
    def tiebreak(serverKey):

        print("tiebreak")
        tiebreakDone = False
        tiebreakPoints = []
        while tiebreakDone == False:
            winner = event_tracker(serverKey, trackerJSON)
            tiebreakPoints.append(winner)
            #change serve every odd point
            if len(tiebreakPoints)%2 == 1:
                serverKey = opposite(serverKey)

            #stop when someone has at least 7 points and 2 difference
            for i in range(2):
                if tiebreakPoints.count(i) >= 7:
                    if tiebreakPoints.count(i)-tiebreakPoints.count(opposite(i)) > 1:
                        tiebreakDone = True
                        winner = i

        return winner


        #needs to return a 0,1
        return random.randint(0, 1)

    #initialize score values
    total_score = []#all the sets
    total_sets = [0, 0]#set values

    #load an empty tracker
    trackerJSON = load_file("empty_tracker")

    #start the match
    matchIsOver = False
    #while the match is still playing
    while matchIsOver == False:

        #start set
        game_score = [0, 0]#game values (set score)
        setIsOver = False
        while setIsOver == False:

            #points won
            score = [0, 0]
            #attribute player serving
            serverKey = 0

            while (score[0] < 4) and (score[1] < 4):#win 4 points to win the game
                #attribute winner (0,1)
                winner = event_tracker(serverKey, trackerJSON)
                score[winner] = score[winner] + 1
                #print_score(score)
                
            #change serving player when game is done
            serverKey = opposite(serverKey)

            #who won the game (0,1)
            for i in range(len(score)):
                if score[i] == 4:
                    #print(players[i]+" won the game")
                    gameWinnerKey = i
                    gameLoserKey = opposite(gameWinnerKey)
                    break
            
            #add game to score
            game_score[gameWinnerKey] = game_score[gameWinnerKey] + 1

            #check if tiebreak needed
            if (game_score[0] == game_score[1]) and sum(game_score) == 12:#6 - 6
                #run tiebreak function
                tiebreakWinner = tiebreak(serverKey)
                #add game to score
                game_score[tiebreakWinner] = game_score[tiebreakWinner] + 1
                setIsOver = True
            else:#check if match over
                if (game_score[gameWinnerKey] == 6) and (game_score[gameLoserKey] < 5):#6 - <5
                    setIsOver = True
                elif (game_score[gameWinnerKey] == 7) and (game_score[gameLoserKey] < 6):#7 - 5
                    setIsOver = True
                else:#match not over
                    #print(str(game_score[0])+"-"+str(game_score[1]))
                    continue
        
        #set is over
        #print(players[gameWinnerKey]+" won the set")
        total_score.append(game_score)#add set to total score
        #check and attribute set value
        if game_score[0] > game_score[1]:
            total_sets[0] = total_sets[0] + 1
        else:
            total_sets[1] = total_sets[1] + 1

        #check if match is over
        if (total_sets[0] != total_sets[1]) and (sum(total_sets) == 2):#2-0 0-2
            matchIsOver = True
        elif sum(total_sets) == 3:#2-1 1-2
            matchIsOver = True
        else:#1-0 0-1 1-1
            matchIsOver = False

    #end of match
    #dump tracker data
    trackerJSON["match"]["final_score"] = total_score
    for i in range(len(players)):
        trackerJSON["match"]["data"][i]["player_name"] = players[i]
    dump_file("trackers/trackerTest", trackerJSON)

def event_tracker(serverKey, trackerJSON):

    #tracker
    returnKey = opposite(serverKey)

    #event vocabulary
    eventDict = {
        "a": "Ace",
        "re": "Return Error",
        "rw": "Return Winner",
        "ip": "In Play",
        "f": "Fault",
        "df": "Double Fault",
        "wi": "Winner",
        "ue": "Unforced Error",
        "fe": "Forced Error"
    }
    #event scenes on serve
    eventScenes = {
        "1st": ["a", "f", "re", "rw", "ip"],
        "2nd": ["a", "df", "re", "rw", "ip"],
        "IP": []
    }


    #ball is in play function
    def in_play(serve):
        #six events
        events = [str(serverKey)+"wi", str(serverKey)+"ue", str(serverKey)+"fe", str(returnKey)+"wi", str(returnKey)+"ue", str(returnKey)+"fe"]
        event = random.choice(events)
        if (event == events[0]) or (event == events[2]) or (event == events[4]):#serving winner
            edit_tracker(str(serverKey)+"-"+serve+"-"+event+"-s")
            return 0
        else:#receiving winner
            edit_tracker(str(returnKey)+"-"+serve+"-"+event+"-r")
            return 1

    #edit trackerJSON after point
    def edit_tracker(eventString):
        #string to parse
        #(winning player-serve-event-(on what))
        event = eventString.split("-")
        if len(event) != 4:
            print("Error")
        winningPlayer = event[0]
        serve = event[1]
        ending = event[2]
        serveStatus = event[3]
        print(event)

    #check how point started
    def check_point_start(myCurrentServe):
        #play ends before the rally starts (ace, return error, return winner)
        if (event == "a") or (event == "re") or (event == "rw"):
            #if server won the point
            if (event == "a") or (event == "re"):
                edit_tracker(str(serverKey)+"-1-"+event+"-s")
                return serverKey
            #if receiver won the point
            else:
                edit_tracker(str(returnKey)+"-1-"+event+"-r")
                return returnKey
        else:
            return False

    #new protocol

    #enter first serve
    currentMenu = eventScenes["1st"]
    event = random.choice(currentMenu)
    startOfPoint = check_point_start("1")



    #start of point
    events = ["a", "f", "re", "rw", "ip"]
    event = random.choice(events)

    #play ends before the rally starts (ace, return error, return winner)
    if (event == "a") or (event == "re") or (event == "rw"):
        #if server won the point
        if (event == "a") or (event == "re"):
            edit_tracker(str(serverKey)+"-1-"+event+"-s")
            return serverKey
        #if receiver won the point
        else:
            edit_tracker(str(returnKey)+"-1-"+event+"-r")
            return returnKey
    #play starts or fault (f, ip)
    else:
        #rally starts
        if event == "ip":
            #in play function will return winner
            return in_play("1")
        #fault, second serve
        else:
            #same events as first server but "df"
            events = ["a", "df", "re", "rw", "ip"]
            event = random.choice(events)
            #play ends before rally
            if (event == "a") or (event == "re") or (event == "rw"):
                if (event == "a") or (event == "re"):
                    edit_tracker(str(serverKey)+"-2-"+event+"-s")
                    return serverKey
                else:
                    edit_tracker(str(returnKey)+"-2-"+event+"-r")
                    return returnKey
            #play starts or double fault
            else:
                #rally starts
                if event == "ip":
                    return in_play("2")
                else:
                    #double fault
                    edit_tracker(str(returnKey)+"-2-"+event+"r-")
                    return returnKey

if __name__ == "__main__":
    main()
