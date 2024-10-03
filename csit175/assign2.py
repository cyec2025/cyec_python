#!usr/bin/env/python3

### Assignment Shipping Calculator
### Author: CYeC
### Date: 2022-02-19

# variables for organization and future use
costOfItems = ""
shippingCost = 0


print("Shipping Calculator\n")

# ask for cost of items
while True:
    costOfItems = float(input("Cost of items ordered:\t"))
    if costOfItems < 0:
        print(str(costOfItems)+" doesn't really work for this...")
    else:
        print("Got it. "+str(costOfItems)+" bucks, right?")
        break

# calculate shipping cost

if costOfItems > 75:
    shippingCost = 0.00
elif costOfItems >= 50:
    shippingCost = 9.95
elif costOfItems >= 30:
    shippingCost = 7.95
else:
    shippingCost = 5.95
totalCost = costOfItems + shippingCost
print("\nShipping Cost:\t"+str(shippingCost)+"\nTotal Order Cost:\t"+str(totalCost))
print()
print("... Items sent to shipping container ...")


