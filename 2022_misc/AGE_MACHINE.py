print("- AGE MACHINE -\n")

age = int(input("ENTER AGE:\t"))
print("\nCOMPARING AGE ... ")
print("\n...\n...\n...\n")
print("COMPUTATION COMPLETE\n")
agemachine = 100 - age
if age < 100:
    agemachine = 100 - age
    print("YOUR AGE IS LESS THAN 100 BY EXACTLY "+str(agemachine)+" YEARS.")
    print("END PROGRAM")
elif age > 100:
    agemachine = age - 100
    print("YOU ARE VERY OLD hHAHHAHA. BY EXACTLY "+str(agemachine)+" YEARS.")
    print("END POGAM")
else:
    print("YOU ARE A PERFECT BEING.")



