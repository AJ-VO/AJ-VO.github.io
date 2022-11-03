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
    print("0) Quit")
    print("1) Add Result")
    print("2) Add Tournament Result")

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

def playerStreak(currentStreak, ending):#Streak Calculator Algorithm
    if ending == True:
        if currentStreak >= 0:
            return currentStreak+1
        else:
            return 1
    else:
        if currentStreak >= 0:
            return -1
        else:
            return currentStreak-1