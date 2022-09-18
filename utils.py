import math
import json
import sys
from datetime import date
import pandas as pd
import random
from random import choice

def print_main_menu():
    print("======== V&O Bra1n ========")
    print("0) Show Players Information")
    print("1) Add Result")
    print("2) Add Tournament Result")

def print_database_information():
    players = load_players()
    j = 0
    print("NUMBER SHOWN IS KEY")
    for i in players:
        print(str(j)+"| ("+i["g"]+")"+i["name"])
        j = j+1

def print_tournament_information():
    players = load_tournament()
    j = 0
    print("NUMBER SHOWN IS KEY")
    for i in players:
        print(str(j)+"| ("+i["g"]+")"+i["name"])
        j = j+1

def load_players():
    with open('jsons/players.json', 'r') as f:
        data = json.load(f)
    return data

    with open("results.json", "r") as f:
        resultJSON = json.load(f)
    resultJSON.append(match_data)
    with open("results.json", "w") as fp:
        json.dump(resultJSON, fp, indent = 4)

def load_tournament():
    with open('jsons/t_players.json', 'r') as f:
        data = json.load(f)
    return data

def get_date():
    today = date.today()
    d2 = today.strftime("%B %d, %Y")
    return d2

def get_eloGain(matchDelta):
    if matchDelta > 500:
        eloGain = 20
    elif matchDelta < -500:
        eloGain = 180
    else:
        eloGain = int(((-4/25)*matchDelta)+100)

    return eloGain