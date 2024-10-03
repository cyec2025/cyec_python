#blazepizza.py
nofp = eval(input("How many pizas do you want:"))
pofp = eval(input("How meech doos ech pizas coost:"))
subtotal = nofp * pofp
tax = 0.06
salestotal = subtotal * tax
total = subtotal + salestotal
print("The total cost is $", total)
print("This includes $", subtotal, "for the pizza and")
print("$", salestotal, "in sales tax.")
