from tkinter import *
from tkinter import messagebox
from datetime import datetime
import json

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