# Assignment 6: Wizard Inventory
# Author: CYeC
# Date: 2022-03-22


def grab_item(inventory):
    if len(inventory) > 3:
        print("You're carrying to much!")
    else:
        item = input("Item Name: ")
        inventory.append(item)
def drop_item(inventory):
    item = int(input("Item Number: "))
    if item < 1 or item > len(inventory):
        print("Invalid number...")
    else:
        print(inventory[item-1]+" was dropped")
        inventory.pop(item-1)
def show(inventory):
    if len(inventory) == 0:
        print("You don't have anything!!")
    else: print(inventory)

def main():
    inventory = ["twig that might be magical","t-shirt","sweatpants"]
    while True:
        print("MENU\n")
        print("show - show inventory\ngrab - take an item\ndrop - drop an item\nexit - exit the program\n")
        command = input("COMMAND: ")
        if command == "exit":
            print("\nhave a magic filled day!")
            break
        elif command == "grab":
            grab_item(inventory)
        elif command == "drop":
            drop_item(inventory)
        else: show(inventory)


main()
        
    

