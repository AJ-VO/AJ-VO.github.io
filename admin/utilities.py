from tkinter import *
from tkinter import messagebox
from datetime import datetime
import json
import random

def about():
    messagebox.showinfo('About', "Alexandre Jasmin\n514-553-6209")

def get_date():#YYYY-MM-DD HH:MM
    now = datetime.now()
    moshi = now.strftime("%Y-%m-%d %H:%M")
    return moshi

def get_orders():#Returns orders.json
    with open("jsons/orders.json", "r") as f:
        data = json.load(f)
    f.close()
    return data

def dump_orders(mydict):#Dumps orders.json
    with open("jsons/orders.json", "w") as f:
        json.dump(mydict, f, indent=4)
    f.close()

def refresh(self):#Refresh App
    self.refresh()

def checkOrder(client, price):#Check the parameters of the order

    #If name not given?
    if str(client) == "":
        messagebox.showinfo('Erreur', "Missing Client Name")
        return
    #If price is negative or not a number?
    try:
        float(price)
    except:
        messagebox.showinfo('Erreur', "Price is NaN")
        return
    if float(price) < 0:
        messagebox.showinfo('Erreur', "Price is < 0$")
        return

def createOrder(client, price):#Create order dict, returns json
    #Get order.json
    orderJSON = get_orders()
    orderDict = {}
    #Generate random 6 digit ID
    order_id = ""
    for i in range(5):
        tank = str(random.randint(0,9))
        order_id = order_id+tank
    #Get Date
    date_id = get_date()

    orderDict["client_name"] = client
    orderDict["order_id"] = order_id
    orderDict["order_date"] = date_id
    orderDict["price"] = price
    orderDict["payment_status"] = False
    orderJSON.append(orderDict)

    info = {}
    info["id"] = order_id

    return orderJSON, info