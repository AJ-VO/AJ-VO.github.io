from ctypes import alignment
import tkinter as tk
import random
from tkinter import *
from tkinter import messagebox
from tkinter import font

#Hyperlink
import webbrowser

#Local
import utilities as U

global myFont, mainButonColor
myFont = 'Copperplate Gothic Bold'
mainButonColor = '#918f89'

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        ## Setting up initial things
        self.title("GLP - Boutique")
        self.geometry("720x600")
        self.resizable(True, True)
        self.iconphoto(False, tk.PhotoImage(file="assets/title_icon.png"))
    
        ## Creating a container
        container = tk.Frame(self, bg="#8AA7A9")
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        ## Initialize Frames
        self.frames = {}
        self.HomePage = HomePage
        self.Validation = Validation
        self.Create = Create
        self.ShowOrders = ShowOrders
        self.Done = Done

        ## Defining Frames and Packing it
        for F in {HomePage, Validation, Create, ShowOrders, Done}:
            frame = F(self, container)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")    
           
        self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        menubar = frame.create_menubar(self)
        self.configure(menu=menubar)
        frame.tkraise()                         ## This line will put the frame on front

#---------------------------------------- HOME PAGE FRAME / CONTAINER ------------------------------------------------------------------------

class HomePage(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)

        #Home Labels
        label = tk.Label(self, text="GLP - Menu", font=(myFont, '20'))
        label.pack(pady=0,padx=0)
        label1 = tk.Label(self, text=U.get_date()[:10], font=(myFont, '12'))
        label1.pack(pady=0,padx=0)

        #Home Buttons
        button = tk.Button(self, width=20, height=3, 
            text="Créer une commande", font=(myFont, '20'), command=lambda: parent.show_frame(parent.Create), bg=mainButonColor)
        button.pack(pady=10,padx=10)
        button1 = tk.Button(self, width=20, height=3, 
            text="Voir les commandes", font=(myFont, '20'), command=lambda: parent.show_frame(parent.ShowOrders), bg=mainButonColor)
        button1.pack(pady=10,padx=10)
        button2 = tk.Button(self, width=20, height=3, 
            text="Terminer une commande", font=(myFont, '20'), command=lambda: parent.show_frame(parent.Done), bg=mainButonColor)
        button2.pack(pady=10,padx=10)

        ## ADD CODE HERE TO DESIGN THIS PAGE

        myLinkStr = "Comment prendre une commande?"
        myLink = Label(self, text=myLinkStr, cursor="hand2", fg="blue", underline=len(myLinkStr)-1)
        myLink.pack()
        myLink.bind("<Button-1>", lambda event: webbrowser.open("https://github.com/AJ-VO/AJ-VO.github.io/tree/main/admin"))

    def create_menubar(self, parent):
        menubar = Menu(parent, bd=3, relief=RAISED, activebackground="#80B9DC")

        ## Filemenu
        filemenu = Menu(menubar, tearoff=0, relief=RAISED, activebackground="#026AA9")
        menubar.add_cascade(label="Fichier", menu=filemenu)
        filemenu.add_command(label="Nouvelle commande", command=lambda: parent.show_frame(parent.Create))
        filemenu.add_command(label="Fermer", command=lambda: parent.show_frame(parent.HomePage))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=parent.quit)  

        ## proccessing menu
        processing_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Validation", menu=processing_menu)
        processing_menu.add_command(label="validate")
        processing_menu.add_separator()

        ## help menu
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Aide", menu=help_menu)
        help_menu.add_command(label="Contact", command=U.about)
        help_menu.add_separator()

        return menubar

#---------------------------------------- Validation PAGE FRAME / CONTAINER (MODEL PAGE) ------------------------------------------------------------------------

class Validation(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)

        label = tk.Label(self, text="Validation Test Page Page", font=(myFont, '20'))
        label.pack(pady=0,padx=0)

        ## ADD CODE HERE TO DESIGN THIS PAGE

    def create_menubar(self, parent):
        menubar = Menu(parent, bd=3, relief=RAISED, activebackground="#80B9DC")

        ## Filemenu
        filemenu = Menu(menubar, tearoff=0, relief=RAISED, activebackground="#026AA9")
        menubar.add_cascade(label="Fichier", menu=filemenu)
        filemenu.add_command(label="Nouvelle commande", command=lambda: parent.show_frame(parent.Create))
        filemenu.add_command(label="Fermer", command=lambda: parent.show_frame(parent.HomePage))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=parent.quit)  

        ## proccessing menu
        processing_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Validation", menu=processing_menu)
        processing_menu.add_command(label="validate")
        processing_menu.add_separator()

        ## help menu
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Aide", menu=help_menu)
        help_menu.add_command(label="Contact", command=U.about)
        help_menu.add_separator()

#---------------------------------------- Create PAGE FRAME / CONTAINER ------------------------------------------------------------------------

class Create(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)

        def quitRefresh():
            confirmation_label.config(text="")
            #Delete Entry Text
            name_entry.delete(0, END)
            name_entry1.delete(0, END)
            name_entry2.delete(0, END)
            parent.show_frame(parent.HomePage)

        def submitRaket(clientName, price, name_entry, name_entry1, confirmation_label, note_var):

            myStatus = U.checkOrder(clientName.get(), price.get())

            if myStatus == False:
                #Don't keep going
                return

            orderJSON, order_id= U.createOrder(clientName.get(), price.get(), note_var.get())

            U.dump_orders(orderJSON)

            #Main menu
            global confirmationStr
            confirmationStr = "Commande créer!\nId: "+order_id["id"]+"\nNom: "+clientName.get()+"\nPrix: "+price.get()
            #Update label
            confirmation_label.config(text = confirmationStr)

            #Delete Entry Text
            name_entry.delete(0, END)
            name_entry1.delete(0, END)
            name_entry2.delete(0, END)

        #Entry Variables
        name_var=tk.StringVar()
        passw_var=tk.StringVar()
        note_var=tk.StringVar()

        label = tk.Label(self, text="Créer une commande!", font=(myFont, '20')).pack(pady=10,padx=10)

        name_label = tk.Label(self, text = 'Nom*', font=(myFont,15, 'bold'))
        name_label.pack(pady=5,padx=5)
        name_entry = tk.Entry(self, textvariable = name_var, font=('Times',14,'normal'))
        name_entry.pack(pady=5,padx=5)

        name_label1 = tk.Label(self, text = 'Prix Total (xx.xx ou xx)*', font=(myFont,15, 'bold'))
        name_label1.pack(pady=5,padx=5)
        name_entry1 = tk.Entry(self, textvariable = passw_var, font=('Times',14,'normal'))
        name_entry1.pack(pady=5,padx=5)

        name_label2 = tk.Label(self, text = 'Notes', font=(myFont,15, 'bold'))
        name_label2.pack(pady=5,padx=5)
        name_entry2 = tk.Entry(self, textvariable = note_var, font=('Times',14,'normal'))
        name_entry2.pack(pady=5,padx=5)

        confirmation_label = tk.Label(self, text = '', font=(myFont,10, 'bold'), fg="red")
        confirmation_label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Soumettre", 
            font=(myFont, '20'), command=lambda: submitRaket(name_var, passw_var, name_entry, name_entry1, confirmation_label, note_var))
        button.pack(pady=20,padx=20)

        #Menu Button
        button1 = tk.Button(self, text="Menu", 
            font=(myFont, '12'), command=lambda: quitRefresh())
        button1.pack(pady=5,padx=5)

        ## ADD CODE HERE TO DESIGN THIS PAGE

    def create_menubar(self, parent):
        menubar = Menu(parent, bd=3, relief=RAISED, activebackground="#80B9DC")

        ## Filemenu
        filemenu = Menu(menubar, tearoff=0, relief=RAISED, activebackground="#026AA9")
        menubar.add_cascade(label="Fichier", menu=filemenu)
        filemenu.add_command(label="Nouvelle commande", command=lambda: parent.show_frame(parent.Create))
        filemenu.add_command(label="Fermer", command=lambda: parent.show_frame(parent.HomePage))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=parent.quit)  

        ## proccessing menu
        processing_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Validation", menu=processing_menu)
        processing_menu.add_command(label="validate")
        processing_menu.add_separator()

        ## help menu
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Aide", menu=help_menu)
        help_menu.add_command(label="Contact", command=U.about)
        help_menu.add_separator()

#---------------------------------------- Show Orders PAGE FRAME / CONTAINER ------------------------------------------------------------------------

class ShowOrders(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)

        #Update if new order during use
        def refreshOrders():
            myList.delete(0, END)
            orderJSON = U.get_orders()
            for i in orderJSON:
                myList.insert(END, f"{i['order_id']:10}{i['order_date']:25}{i['client_name']:10}")

        def go(event):
            cs = myList.curselection()
            myS = str(myList.get(cs)[:6])#OrderId (str)
            orderJSON = U.get_orders()
            statusLoop = False
            for i in orderJSON:
                if myS == i["order_id"]:
                    messagebox.showinfo('About', i["order_notes"])
                    statusLoop = True
            if statusLoop == False:
                messagebox.showinfo('Error', 'Order Not Found')


        label = tk.Label(self, text="Commandes Ouvertes", font=(myFont, '20'))
        label.pack(pady=0,padx=0)

        refreshButton = tk.Button(self, text="Refresh", font=(myFont, '15'), command=lambda: refreshOrders())
        refreshButton.pack(pady=10,padx=10)

        #Scrollbar
        scrollbar = Scrollbar(self)
        scrollbar.pack(side = RIGHT, fill = Y)
        #Can we make listbox align? change font?
        myList = Listbox(self, yscrollcommand = scrollbar.set, width=55, height=10, font=('Times', '18'))

        #Create String
        orderJSON = U.get_orders()
        for i in orderJSON:
            myList.insert(END, f"{i['order_id']:10}{i['order_date']:25}{i['client_name']:10}")

        myList.bind('<Double-1>', go)
        myList.pack()
        scrollbar.config(command = myList.yview)

        #Menu Button
        button1 = tk.Button(self, text="Menu", 
            font=(myFont, '12'), command=lambda: parent.show_frame(parent.HomePage))
        button1.pack(pady=5,padx=5)

        ## ADD CODE HERE TO DESIGN THIS PAGE

    def create_menubar(self, parent):
        menubar = Menu(parent, bd=3, relief=RAISED, activebackground="#80B9DC")

        ## Filemenu
        filemenu = Menu(menubar, tearoff=0, relief=RAISED, activebackground="#026AA9")
        menubar.add_cascade(label="Fichier", menu=filemenu)
        filemenu.add_command(label="Nouvelle commande", command=lambda: parent.show_frame(parent.Create))
        filemenu.add_command(label="Fermer", command=lambda: parent.show_frame(parent.HomePage))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=parent.quit)  

        ## proccessing menu
        processing_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Validation", menu=processing_menu)
        processing_menu.add_command(label="validate")
        processing_menu.add_separator()

        ## help menu
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Aide", menu=help_menu)
        help_menu.add_command(label="Contact", command=U.about)
        help_menu.add_separator()

#---------------------------------------- Done PAGE FRAME / CONTAINER (MODEL PAGE) ------------------------------------------------------------------------

class Done(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)

        label = tk.Label(self, text="Done", font=(myFont, '20'))
        label.pack(pady=0,padx=0)

        ## ADD CODE HERE TO DESIGN THIS PAGE

    def create_menubar(self, parent):
        menubar = Menu(parent, bd=3, relief=RAISED, activebackground="#80B9DC")

        ## Filemenu
        filemenu = Menu(menubar, tearoff=0, relief=RAISED, activebackground="#026AA9")
        menubar.add_cascade(label="Fichier", menu=filemenu)
        filemenu.add_command(label="Nouvelle commande", command=lambda: parent.show_frame(parent.Create))
        filemenu.add_command(label="Fermer", command=lambda: parent.show_frame(parent.HomePage))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=parent.quit)  

        ## proccessing menu
        processing_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Validation", menu=processing_menu)
        processing_menu.add_command(label="validate")
        processing_menu.add_separator()

        ## help menu
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Aide", menu=help_menu)
        help_menu.add_command(label="Contact", command=U.about)
        help_menu.add_separator()


if __name__ == "__main__":
    app = App()
    app.mainloop()


