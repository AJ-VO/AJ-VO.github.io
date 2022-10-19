from tkinter import E
from utilities import *

def main():

    print_main_menu()
    choice = input("Choix: ")
    if choice == "1":#Create Order
        #Create dict
        data = {}

        #Generate random 6 digit ID
        order_id = ""
        for i in range(6):
            tank = str(random.randint(0,9))
            order_id = order_id+tank
        data["order_id"] = order_id
        #Enter Raket ID

        #Get rakets
        
        """ confirmed_raket = False
        while confirmed_raket == False:
            raquet_id = input("Racquet information: ") """

        #Check if id exists, or main()
        raquet_id = input("Racquet information: ")
        data["raket_id"] = raquet_id

        #Generate Time
        data["order_date"] = get_date()
        #Generate Status
        data["status"] = 100
        #Generate payment_status
        data["payment_status"] = False
        #Generate balance
        total_price = 0
        while total_price == 0:
            data["due_balance"] = input("Price: ")

        #Dump in orders.json
        with open("jsons/orders.json", "r") as outfile:
            orderJSON = json.load(outfile)
        outfile.close()
        orderJSON.append(data)
        with open("jsons/orders.json", "w") as outfile:
            json.dump(orderJSON, outfile, indent=4)
        outfile.close()
        main()
    elif choice == "2":#Complete Order
        orders = get_orders()
        ordersL = []
        for i in orders:
            ordersL.append(i["order_id"])
        #Show current orders
        show_orders()
        #Choose order done
        order_confirmed = False
        while order_confirmed == False:
            order_done = str(input("Id of order done: "))#String
            print(order_done)
            for x in orders:
                if order_done == str(x["order_id"]):
                    order_confirmed = True

        #Add to completed.json
        with open("jsons/completed.json", "r") as f:
            completedJSON = json.load(f)
            for i in orders:
                if order_done == i["order_id"]:
                    completedJSON.append(i)
        f.close()
        with open("jsons/completed.json", "w") as f:
            json.dump(completedJSON, f, indent=4)
        f.close()

        #Change data (my_list.pop(idx))
        for i in range(len(ordersL)):
            if order_done == ordersL[i]:
                orders.pop(i)

        with open("jsons/orders.json", "w") as f:
            json.dump(orders, f, indent=4)

        main()
    elif choice == "0":#Quit
        sys.exit(0)
    elif choice == "3":#Take Payment
        print()
        main()
    elif choice == "-1":#Add client
        clientJSON = get_clients()
        name = str(input("Name: "))
        notes = str(input("Any notes?: "))
        client = {}
        
        #CHECK NAME
        listClients = list_clients()
        for i in range(len(listClients)):
            myRatio = SequenceMatcher(a=name,b=listClients[i]).ratio()
            if myRatio > 0.9:
                answer = input("Found Client("+listClients[i]+") [Inputed ("+name+")], still add? (Y/N): ")
                if answer.lower() == "y":
                    client["name"] = name
                else:
                    main()
            else:
                client["name"] = name

        client["name"] = name
        #Generate random 5 digit ID
        order_id = ""
        for i in range(5):
            tank = str(random.randint(0,9))
            order_id = order_id+tank
        #Enter Raket ID
        client["client_id"] = order_id
        client["rakets"] = {}
        client["past_orders"] = {}
        client["notes"] = notes
        clientJSON.append(client)
        with open("jsons/clients.json", "w") as f:
            json.dump(clientJSON, f, indent=4)
        f.close()
        main()
    elif choice == "-2":#Add raket
        #Choose client
        #Information, raket_id, description(type), tension, Xcords, Ycords, pattern
        show_clients()
        myClient = input("Enter Client ID (ID) - Name")
        



        



if __name__ == "__main__":
    main()