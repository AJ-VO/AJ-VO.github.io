#Libraries
import math
import json
import sys
import random
import time
import xlrd
import statistics
import json
import pandas as pd
from datetime import date
from random import choice

def my_test():#Test Function
    l = []
    l.append(1)
    print(len(l))

def get_ms_date():#Returns MS timestamp (int)
    return round(time.time() * 1000)

def print_main_menu():#Print Main Menu
    print("======== V&O Bra1n ========")
    print("-1) Database Information")
    print("0) Quit")
    print("1) Add Result")
    print("2) Add Doubles Result")
    print("===========================")

def load_players():#Returns players from database (json)
    with open('jsons/players.json', 'r', encoding='utf8') as f:
        data = json.load(f)
    return data

def load_tournament():#Returns players on tournament from database (json)
    with open('jsons/t_players.json', 'r', encoding='utf8') as f:
        data = json.load(f)
    return data

def load_results():#Returns results from database (json)
    with open("jsons/results.json", "r", encoding='utf8') as fp:
        data = json.load(fp)
    return data

def print_database_information():#Print Players Database for Data Entry
    #Load Players
    players = load_players()
    #Print Key
    j = 0
    print("NUMBER SHOWN IS KEY")
    for i in players:
        print(str(j)+"| ("+i["g"]+")"+i["name"])
        j = j+1
    return j

def print_tournament_information():#Print Tournaments Database for Data Entry
    players = load_tournament()
    j = 0
    print("NUMBER SHOWN IS KEY")
    for i in players:
        print(str(j)+"| ("+i["g"]+")"+i["name"])
        j = j+1

def get_date():#Returns Date for Database results.json (str)
    today = date.today()
    d2 = today.strftime("%B %d, %Y")
    return d2

def get_eloGain(matchDelta):#Points lost and gained algorithm
    if matchDelta > 500:
        eloGain = 20
    elif matchDelta < -500:
        eloGain = 180
    else:
        eloGain = int(((-4/25)*matchDelta)+100)
    return eloGain

def updateImages():#Update Images (End of November)

    with open("jsons/players.json", "r", encoding='utf8') as f:
        data = json.load(f)
    f.close()

    for i in data:
        myKey = str(i["id"])
        i["img"] = "img/players/"+myKey+".png"

    with open("jsons/players.json", "w", encoding='utf8') as f:
        json.dump(data, f, indent=4)

def show_database_information(playerInformation, resultInformation):#Shows current database information
    
    #Printing information
    print("============================================")
    print("========== Database Information ============")
    print("============================================")
    print("Matches Played: "+str(len(resultInformation)))
    print("Players: "+str(len(playerInformation)))

    myPlayers = 0
    for i in playerInformation:
        if i["gp"] > 0:#Player has played more than 0 matches
            myPlayers = myPlayers+1
        else:
            continue
    rate = myPlayers/len(playerInformation)*100#Rate
    print("Players that played at least one match: "+str(myPlayers)+" ("+str(rate)+"%)")

    allElos = []
    for i in playerInformation:
        if i["elo"] == 0 or i["elo"] == 1500:
            continue
        else:
            allElos.append(i["elo"])
    meanElo = sum(allElos)/len(allElos)
    print("Mean Elo: "+str(meanElo))
    top = 0
    bottom = 0
    for i in allElos:
        if i >= meanElo:
            top = top + 1
        else:
            bottom = bottom + 1
    print("Players in top 50%: "+str(top))
    print("Players in bottom 50%: "+str(bottom))
    print("============================================")