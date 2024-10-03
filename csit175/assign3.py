### Assignment Three - tip calculator with loops
### Author: CYeC
### Date: 2022-02-27


print("Tip Calculator")

while True:
    # input meal cost
    cost = round(float(input("\nCost of meal:\t")),2)
    # calculate tip amount at different tip percents
    for i in range(15,30,5):
        
        tip = round(cost * (i / 100), 2)
        total = round(cost + tip, 2)
        
        print(str(i)+"%")
        print("Tip Amount:\t",tip)
        print("Total Amount:\t",total)
    # check if the user wants to run it again
    loop = input("\nContinue?:\t")
    if loop.lower() == "y" or loop.lower() == "yes":
        print("Repeating...\n")
    else:
        print("Okay, see you later!")
        break
print("\n\nend")
    
    
