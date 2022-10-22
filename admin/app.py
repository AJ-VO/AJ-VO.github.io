import tkinter as tk
import random
from tkinter import *
from tkinter import messagebox

import utilities as U

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        ## Setting up Initial Things
        self.title("Gestion Loisirs Plus")
        self.geometry("720x550")
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

        ## Defining Frames and Packing it
        for F in {HomePage, Validation, Create, ShowOrders}:
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

        label = tk.Label(self, text="GLP - Menu", font=('Times', '20'))
        label.pack(pady=0,padx=0)
        label1 = tk.Label(self, text=U.get_date(), font=('Times', '12'))
        label1.pack(pady=0,padx=0)

        button = tk.Button(self, text="Créer une commande", font=('Times', '20'), command=lambda: parent.show_frame(parent.Create), bg='#6f9da1')
        button.pack(pady=10,padx=10)
        button1 = tk.Button(self, text="Voir les commandes", font=('Times', '20'), command=lambda: parent.show_frame(parent.ShowOrders), bg='#6f9da1')
        button1.pack(pady=10,padx=10)
        button2 = tk.Button(self, text="Terminer une commande", font=('Times', '20'), command=lambda: parent.show_frame(parent.Create), bg='#6f9da1')
        button2.pack(pady=10,padx=10)

        ## ADD CODE HERE TO DESIGN THIS PAGE

    def create_menubar(self, parent):
        menubar = Menu(parent, bd=3, relief=RAISED, activebackground="#80B9DC")

        ## Filemenu
        filemenu = Menu(menubar, tearoff=0, relief=RAISED, activebackground="#026AA9")
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New Project", command=lambda: parent.show_frame(parent.Validation))
        filemenu.add_command(label="Close", command=lambda: parent.show_frame(parent.HomePage))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=parent.quit)  

        ## proccessing menu
        processing_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Validation", menu=processing_menu)
        processing_menu.add_command(label="validate")
        processing_menu.add_separator()

        ## help menu
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=U.about)
        help_menu.add_separator()

        return menubar

#---------------------------------------- Validation PAGE FRAME / CONTAINER ------------------------------------------------------------------------

class Validation(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)

        label = tk.Label(self, text="Validation Page", font=('Times', '20'))
        label.pack(pady=0,padx=0)

        ## ADD CODE HERE TO DESIGN THIS PAGE

    def create_menubar(self, parent):
        menubar = Menu(parent, bd=3, relief=RAISED, activebackground="#80B9DC")

        ## Filemenu
        filemenu = Menu(menubar, tearoff=0, relief=RAISED, activebackground="#026AA9")
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New Project", command=lambda: parent.show_frame(parent.Validation))
        filemenu.add_command(label="Close", command=lambda: parent.show_frame(parent.HomePage))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=parent.quit)  

        ## proccessing menu
        processing_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Validation", menu=processing_menu)
        processing_menu.add_command(label="validate")
        processing_menu.add_separator()

        ## help menu
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=U.about)
        help_menu.add_separator()

        return menubar

#---------------------------------------- Create PAGE FRAME / CONTAINER ------------------------------------------------------------------------

class Create(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)

        def submitRaket(clientName, price, name_entry, name_entry1,confirmation_label):

            def goBack():
                confirmation_label.config(text="")
                button.pack_forget()
                parent.show_frame(parent.HomePage)

            #If name not given?
            if str(clientName.get()) == "":
                messagebox.showinfo('Erreur', "Missing Client Name")
                return
            #If price is negative or not a number?
            try:
                float(price.get())
            except:
                messagebox.showinfo('Erreur', "Price is NaN")
                return
            if float(price.get()) < 0:
                messagebox.showinfo('Erreur', "Price is < 0$")
                return

            #Get order.json
            orderJSON = U.get_orders()
            orderDict = {}
            #Generate random 6 digit ID
            order_id = ""
            for i in range(5):
                tank = str(random.randint(0,9))
                order_id = order_id+tank
            #Get Date
            date_id = U.get_date()

            orderDict["client_name"] = clientName.get()
            orderDict["order_id"] = order_id
            orderDict["order_date"] = date_id
            orderDict["price"] = price.get()
            orderDict["payment_status"] = False
            orderJSON.append(orderDict)

            U.dump_orders(orderJSON)

            #Main menu
            confirmationStr = "Commande créer!\nId: "+order_id+"\nNom: "+clientName.get()+"\nPrix: "+price.get()

            #Update label
            confirmation_label.config(text = confirmationStr)

            button = tk.Button(self, text="Menu Principal", font=('Times', '15'), command=lambda: goBack())
            button.pack(pady=20,padx=20)

            #Delete Entry Text
            name_entry.delete(0, END)
            name_entry1.delete(0, END)

        name_var=tk.StringVar()
        passw_var=tk.StringVar()

        label = tk.Label(self, text="Créer une commande!", font=('Times', '20'))
        label.pack(pady=0,padx=0)

        name_label = tk.Label(self, text = 'Nom', font=('Times',20, 'bold'))
        name_entry = tk.Entry(self, textvariable = name_var, font=('Times',20,'normal'))
        name_label.pack(pady=10,padx=10)
        name_entry.pack(pady=0,padx=0)

        name_label1 = tk.Label(self, text = 'Prix Total (xx.xx ou xx)', font=('Times',20, 'bold'))
        name_entry1 = tk.Entry(self, textvariable = passw_var, font=('Times',20,'normal'))
        name_label1.pack(pady=10,padx=10)
        name_entry1.pack(pady=0,padx=0)

        button = tk.Button(self, text="Submit", font=('Times', '20'), command=lambda: submitRaket(name_var, passw_var, name_entry, name_entry1, confirmation_label))
        button.pack(pady=20,padx=20)

        confirmation_label = tk.Label(self, text = '', font=('Times',20, 'bold'), fg="red")
        confirmation_label.pack(pady=10,padx=10)

        ## ADD CODE HERE TO DESIGN THIS PAGE

    def create_menubar(self, parent):
        menubar = Menu(parent, bd=3, relief=RAISED, activebackground="#80B9DC")

        ## Filemenu
        filemenu = Menu(menubar, tearoff=0, relief=RAISED, activebackground="#026AA9")
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New Project", command=lambda: parent.show_frame(parent.Validation))
        filemenu.add_command(label="Close", command=lambda: parent.show_frame(parent.HomePage))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=parent.quit)  

        ## proccessing menu
        processing_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Validation", menu=processing_menu)
        processing_menu.add_command(label="validate")
        processing_menu.add_separator()

        ## help menu
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=U.about)
        help_menu.add_separator()

        return menubar

#---------------------------------------- Show Orders PAGE FRAME / CONTAINER ------------------------------------------------------------------------

class ShowOrders(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)

        #Update if new order during use
        def refreshOrders():
            orderJSON = U.get_orders()
            orderStr = ""
            for i in orderJSON:
                orderStr = orderStr+"("+i["order_id"]+") "+i["client_name"]+"\n\n"
            label1.config(text=orderStr)

        label = tk.Label(self, text="Commandes Ouvertes", font=('Times', '20'))
        label.pack(pady=0,padx=0)

        #Refresh Button
        refreshButton = tk.Button(self, text="Refresh", font=('Times', '15'), command=lambda: refreshOrders())
        refreshButton.pack(pady=10,padx=10)

        ## ADD CODE HERE TO DESIGN THIS PAGE
        orderJSON = U.get_orders()
        orderStr = ""
        for i in orderJSON:
            orderStr = orderStr+"("+i["order_id"]+") "+i["client_name"]+"\n\n"

        label1 = tk.Label(self, text=orderStr, font=('Times', '15'))
        label1.pack(pady=10,padx=10)

    def create_menubar(self, parent):
        menubar = Menu(parent, bd=3, relief=RAISED, activebackground="#80B9DC")

        ## Filemenu
        filemenu = Menu(menubar, tearoff=0, relief=RAISED, activebackground="#026AA9")
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New Project", command=lambda: parent.show_frame(parent.Validation))
        filemenu.add_command(label="Close", command=lambda: parent.show_frame(parent.HomePage))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=parent.quit)  

        ## proccessing menu
        processing_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Validation", menu=processing_menu)
        processing_menu.add_command(label="validate")
        processing_menu.add_separator()

        ## help menu
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=U.about)
        help_menu.add_separator()

        return menubar


if __name__ == "__main__":
    app = App()
    app.mainloop()


