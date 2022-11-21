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
    f.close()
    return data

#dump content in file
def dump_file(file, content):
    with open('jsons/'+file+'.json', 'w') as f:
        json.dump(content, f, indent=4)
    f.close()

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
        while tiebreakDone == False:
            winner = event_tracker(serverKey, trackerJSON)

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

        game_score = [0, 0]#game values
        setIsOver = False
        while setIsOver == False:#set is over
            score = [0, 0]#when you win a point, score[i] = score[i]  + 1

            #attribute server
            serverKey = 0

            while (score[0] < 4) and (score[1] < 4):#while the game is playing
                #attribute winner
                winner = event_tracker(serverKey, trackerJSON)#returns 0,1
                score[winner] = score[winner] + 1
                #print_score(score)
                
            #change serving player
            if serverKey == 0:
                serverKey = 1
            else:
                serverKey = 0

            for i in range(len(score)):#print game winner and gameWinnerKey
                if score[i] == 4:
                    #print(players[i]+" won the game")
                    gameWinnerKey = i
                    break
            
            #attribute game
            game_score[gameWinnerKey] = game_score[gameWinnerKey] + 1

            #attribute keys
            if gameWinnerKey == 0:
                gameLoserKey = 1
            else:
                gameLoserKey = 0

            #check if 6-6
            if (game_score[0] == game_score[1]) and sum(game_score) == 12:#6 - 6
                tiebreakWinner = tiebreak(serverKey)
                game_score[tiebreakWinner] = game_score[tiebreakWinner] + 1
                setIsOver = True
            else:#not tiebreak
                if (game_score[gameWinnerKey] == 6) and (game_score[gameLoserKey] < 5):#6 - something
                    setIsOver = True
                elif (game_score[gameWinnerKey] == 7) and (game_score[gameLoserKey] < 6):#7 - 5
                    setIsOver = True
                else:#playing
                    #print(str(game_score[0])+"-"+str(game_score[1]))
                    continue
        
        print(players[gameWinnerKey]+" won the set")
        total_score.append(game_score)#add set to score
        #check and attribute set value
        if game_score[0] > game_score[1]:
            total_sets[0] = total_sets[0] + 1
        else:
            total_sets[1] =total_sets[1] + 1

        #MATCH IS OVER
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

    #First Event
    events = ["a", "f", "re", "rw", "ip"]
    event = random.choice(events)

    returnKey = opposite(serverKey)
    
    #POINT
    #play ends before the rally starts (ace, return error, return winner)
    if (event == "a") or (event == "re") or (event == "rw"):
        if (event == "a") or (event == "re"):
            edit_tracker(str(serverKey)+"-1-"+event+"-s")
            return serverKey
        else:
            edit_tracker(str(returnKey)+"-1-"+event+"-r")
            return returnKey
    #play starts or fault (f, ip)
    else:
        #rally starts
        if event == "ip":
            return in_play("1")
        #second serve
        else:
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
