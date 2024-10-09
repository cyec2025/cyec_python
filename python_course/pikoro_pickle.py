### Pikoro (Pickle) Assignment
### Author - CYeC
### Date: 2022-05-27

import pickle as p

dictionary = {"green":"bread","orange":"crumb"}


def dump(words):
    with open("pickledict.bin","wb") as file:
        p.dump(words,file)

def load():
    with open("pickledict.bin","rb") as file:
        dredge = p.load(file)
    return dredge

def write():
    new_dict = load()
    
    new_choice = input("Erase or Write: ")
    if new_choice.lower() == "erase":
        key = input("Key: ")
        if key in new_dict:
                new_dict.pop(key)
        else: print("Unknown Key")
    elif new_choice.lower() == "write":
        key = input("Key: ")
        value = input("Value: ")
        new_dict[key] = value
    dump(new_dict)

def read():
    new_dict = load()
            
    key = input("Key: ")
    if key in new_dict:
        print("Value:",new_dict[key])
    else: print("Unknown Key")

def read_all():
    new_dict = load()
    for key in new_dict:
        print(key,new_dict[key])

def main():
    print("dictionary machine")
    print("RA: read all, R: read, W: write, Q: quit")
    while True:
        choice = input("RA/R/W/Q: ")
        if choice.lower() == "r":
            read()
        elif choice.lower() == "w":
            write()
        elif choice.lower() == "ra":
            read_all()
        elif choice.lower() == "q":
            break
        else: print("Unknown Input")
    print("bye")

main()
