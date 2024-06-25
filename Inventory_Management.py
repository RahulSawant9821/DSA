'''Inventory Management:

Simulate a simple inventory system using a list of lists: [[item_name, quantity, price]].
Implement functions to add, remove, update, and search for items in the inventory.'''

Inventory = []

number_of_items = int(input("Enter the number of items in an Inventory :"))

for items in range(number_of_items):
    item_name  = input(f"\n Enter the name of the {items+1} Item:")
    quanity  = int( input(f"\n Enter the quantity of the {items+1} Item:"))
    price  = float(input(f"\n Enter the price of the {items+1} Item:"))
    Inventory.append([item_name,quanity,price])

def add_Stock():
    print("You have entered the add operations -> ")
    item_name = input("Enter the name of the item to be added : ")
    quanity = int( input("Enter the qunatity of the item to be added : "))
    price = float(input("Enter the price of the item to be added : "))
    Inventory.append([item_name,quanity,price])
    print(f"Item {item_name} added successfully !")

def remove_Stock():
    print("You have entered the remove operations -> ")
    item_name = input("Enter the name of the item to be removed : ")
    Inventory.remove([item_name])
    print(f"Item {item_name} removed successfully !")


print("Let's Manipulate your Inventory :")
choice = int(input("\n Enter the numbers you want to perform operations : \n 1: Add \n 2: Remove \n 3:Update \n 4:Search \n"))

match choice :

    case 1 : 
        add_Stock
    case 2: 
        remove_Stock


        


