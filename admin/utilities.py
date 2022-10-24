from tkinter import *
from tkinter import messagebox
from datetime import datetime
import json
import random

#Prix pose = 21$
#100: open
#101: open and payed
#200: closed
#201: closed and payed

def about():
    messagebox.showinfo('About', "Alexandre Jasmin\n514-553-6209")

def id_generator(myAmount):#Generate random x digit ID (str)
    order_id = ""
    for i in range(myAmount):
        tank = str(random.randint(0,9))
        order_id = order_id+tank
    return order_id

def get_date():#YYYY-MM-DD HH:MM
    now = datetime.now()
    moshi = now.strftime("%Y-%m-%d %H:%M")
    return moshi

def get_orders():#Returns orders.json
    #Future change: https://aj-vo.github.io/admin/jsons/orders.json
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
        return False
    #If price is negative or not a number?
    try:
        float(price)
    except:
        messagebox.showinfo('Erreur', "Price is NaN")
        return False
    if float(price) < 0:
        messagebox.showinfo('Erreur', "Price is < 0$")
        return False

def createOrder(client, price, notes, myDate):#Create order dict, returns json
    #Get order.json
    orderId = id_generator(6)
    orderJSON = get_orders()
    orderDict = {}
    orderDict["client_name"] = client
    orderDict["order_id"] = orderId
    orderDict["order_date"] = get_date()
    orderDict["price"] = price
    orderDict["payment_status"] = False
    orderDict["order_notes"] = notes
    orderDict["status"] = "100"
    orderDict["due_date"] = myDate
    orderJSON.append(orderDict)

    info = {}
    info["id"] = orderId

    return orderJSON, info