from http import client
import math
import json
import random
from datetime import datetime
import sys
from tabnanny import check
from difflib import SequenceMatcher
from this import d

def print_main_menu():
    print("MENU")
    print("0) Quit")
    print("1) Create Order")
    print("2) Complete Order")
    print("3) Take Payment")
    print("ADMIN")
    print("-1) Add Client")
    print("-2) Add Raket")

def get_date():#YYYY-MM-DD HH:MM
    now = datetime.now()
    moshi = now.strftime("%Y-%m-%d %H:%M")
    return moshi

def show_orders():#Prints Orders

    with open("jsons/clients.json", "r") as outfile:
        clientJSON = json.load(outfile)
    outfile.close()

    with open("jsons/orders.json", "r") as f:
        data = json.load(f)
    f.close()

    for x in data:#for every order
        currentRaket = x["raket_id"]
        for i in clientJSON:#for every client
            for k in i["rakets"]:
                if i["rakets"][k]["id"] == currentRaket:
                    print("Order ("+x["order_id"]+") - ("+currentRaket+") - "+i["name"])

def get_orders():#Returns orders.json
    with open("jsons/orders.json", "r") as f:
        data = json.load(f)
    f.close()
    return data

def get_clients():#Returns clients.json
    with open("jsons/clients.json", "r") as f:
        data = json.load(f)
    f.close()
    return data

def list_clients():#Returns list of clients
    myL = []
    clientJSON = get_clients()
    for i in clientJSON:
        myL.append(i["name"])
    return myL

def list_clients_id():#Returns list of clients ids
    myL = []
    clientJSON = get_clients()
    for i in clientJSON:
        myL.append(i["client_id"])
    return myL

def show_clients():#Prints Clients
    clientJSON = get_clients()
    for i in clientJSON:
        print("("+i["client_id"]+")"+i["name"])

########TEST

def get_list_of_rakets():
    
    return

def check_admin_status():#Checks if person is admin
    print("Hello")