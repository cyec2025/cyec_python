# Assignment 7: reading and writing files
# Author: CYeC
# Date: 2022-04-07

import csv



# gaming variable: lets the program know when you are running it
gaming = 1

#i couldnt figure out how to test if the text file is on the computer already so my work around
#is to uncomment these four lines below this if you dont have the file yet \/ \/ \/

#contacts = [["Eric Idle","eric@ericidle.com","+44 20 7946 0958"],["Guido van Rossum","guido@python.org","+31 0474 33 88 26"],["Lord Tums III","tums@gobo.com","+1 222 223 2224"]]
#with open("contacts.csv","w") as file:
#    writer = csv.writer(file)
#    writer.writerows(contacts)


# list function using old english spelling because regular turns purple for some reason
def liste():
    with open("contacts.csv","r") as file:
        reader = csv.reader(file)
        i = 1
        for row in reader:
            print(str(i)+".",row[0])
            i += 1
            
# view a specific contact
def view():
    index = int(input("Number: "))
    with open("contacts.csv","r") as file:
        reader = csv.reader(file)
        i = 1
        readable = []
        for row in reader:
            readable.append(row)
            i += 1
        print("Name: ",readable[index-1][0])
        print("Email: ",readable[index-1][1])
        print("Phone: ",readable[index-1][2],"\n")

# leave program
def exit():
    print("\nToodles...")
    global gaming
    gaming = 0

# add new contact
def add():
    new_contact = [[]]
    new_contact[0].append(input("Name: "))
    new_contact[0].append(input("Email: "))
    new_contact[0].append(input("Phone: "))
    with open("contacts.csv","a") as file:
        writer = csv.writer(file)
        writer.writerows(new_contact)
# the menu
def menu():
    print("COMMAND MENU\n\nlist - Display contacts\nview - View a contact\nadd - Add a contact\nexit - Exit pogram")
    command = input("\nCommand: ")
    if command.lower() == "list":
        liste()
    elif command.lower() == "exit":
        exit()
    elif command.lower() == "add":
        add()
    elif command.lower() == "view":
        view()
    else: print("huh?")

def main():
    while gaming == 1:
        menu()

if __name__ == "__main__":
    main()
