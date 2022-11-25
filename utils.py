#Modules
import json
import math
import random
import statistics
import sys
import time
from datetime import date
from random import choice

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import qrcode
import xlrd

def my_test():#Test Function
    print(40%2)

def get_ms_date():#Returns MS timestamp (int)
    return round(time.time() * 1000)

def print_main_menu():#Print Main Menu
    print("======== V&O Bra1n ========")
    print("-3) Add Team Player")
    print("-2) Add Player")
    print("-1) Database Information")
    print("0) Quit")
    print("1) Add Result")
    print("2) Add Doubles Result")
    print("3) Add Tournament Result")
    print("===========================")

def load_data(file):#Returns data from database
    with open('jsons/'+file+'.json', 'r', encoding='utf8') as f:
        data = json.load(f)
    return data

def print_database_information():#Print Players Database for Data Entry
    #Load Players
    players = load_data('players')
    #Print Key
    j = 0
    print("NUMBER SHOWN IS KEY")
    for i in players:
        print(str(j)+"| ("+i["g"]+")"+i["name"])
        j = j+1
    return j

def get_date():#Returns Date for Database results.json (str)
    today = date.today()
    d2 = today.strftime("%B %d, %Y")
    return d2

def get_eloGain(matchDelta):#Points lost and gained algorithm (int)
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

def show_teams():#Show teams for data entry
    with open("jsons/teams.json", 'r') as outfile:
        data = json.load(outfile)
    outfile.close()
    j = 0
    for i in data:
        print("("+str(j)+") "+i["team_name"]+" ["+i["team_tag"]+"]")
        j = j + 1
    return j

def standings_bell_curve():#Show bell curve of current standings

    def pdf(x):
        mean = np.mean(x)
        std = np.std(x)
        y_out = 1/(std * np.sqrt(2 * np.pi)) * np.exp( - (x - mean)**2 / (2 * std**2))
        return y_out
        
    x = []#<class 'numpy.ndarray'>
    with open("jsons\players.json", "r") as f:
        data = json.load(f)
    for i in data:
        x.append(i["elo"])

    y = pdf(x)

    plt.style.use('seaborn')
    plt.figure(figsize = (6, 6))
    plt.plot(x, y, color = 'black',
            linestyle = 'dashed')

    plt.scatter( x, y, marker = 'o', s = 25, color = 'red')
    plt.show()

def dump_json_file(file, myData):#Dump to specific file

    with open("jsons/"+file+".json", "w", encoding="utf8") as f:
        json.dump(myData, f, indent=4)
    print("("+file+".json) - dumped")

def create_qr_code():#Create QR Code from data
    # Data to be encoded
    data = ""
    title = "tutorialQR"
    # Encoding data using make() function
    img = qrcode.make(data)
    # Saving as an image file
    img.save('img/qr/'+title+'.png')
