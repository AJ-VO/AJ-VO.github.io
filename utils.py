import math
import json
import sys
from datetime import date
import pandas as pd
import random
from random import choice
import time
import xlrd
import statistics

def print_main_menu():
    print("======== V&O Bra1n ========")
    print("0) Show Players Information")
    print("1) Add Result")
    print("2) Add Tournament Result")
    print("3) ")

def current_milli_time():
    return str(round(time.time() * 1000))

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