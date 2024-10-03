import random

hairc = input("tell me your hair color...:\t")
eyec = input("tell me your eye color...:\t")
age = input("age... :\t\t\t\t")
if age.isnumeric():
    print("youve got a real age...")
else:
    print("stop playing games with me.")
    age = str(random.randint(10,70))
    print("ive decided you seem about "+age+".")
    

if hairc == "blond" or hairc == "blonde":
    if eyec == "blue":
        print("hmm... blond blue etc thing im not writig that")
    else:
        print("crinimal spotted in the bank. suspect is blond and has "+eyec+" eyes.")
elif eyec == "blue":
    print("feeling... BLUE? HAHAHA well at least youve got "+hairc+" hair.")
else:
    print("so youve got "+hairc+" hair and "+eyec+" eyes?\nreminds me of someone else i used to know...")
print("and your "+age+"?")
if int(age) > 40:
    age = str(int(age) - 7)
    print("you seem like your "+age)
else: print("i believe it.")
