print("Minecraft 1.18 custom floor crafting generator")
print("Version 3")
print("by yok")
print()
while True:

    print()
    print("would you like the simple or advanced form?")
    simple = input("answer with 's' or 'a':")
    
    if simple == "s":
        print("using simple form!")
        print()

        
        print("first ingredient time!")
        print()
        item1 = input("minecraft item:")
        is_tag1 = input("wanna use a custom tag? (y/n):")
        print()
        if is_tag1 == "y":
            print("Okay! using a tag!")
            tag1 = input("what is the name of your tag?:")
            tag1 = ",tag:{"+tag1+":1b}"
        elif is_tag1 == "n":
            print("Okay! not using a tag!")
            tag1 = ""
        else:
            print("uhh idk what that means so im gonna guess you want no tag")
            is_tag1 = "n"
            tag1 = ""

        
        print()
        print("second ingredient time!")
        print()
        item2 = input("minecraft item:")
        is_tag2 = input("wanna use a custom tag? (y/n):")
        print()
        if is_tag2 == "y":
            print("Okay! using a tag!")
            tag2 = input("what is the name of your tag?:")
            tag2 = ",tag:{"+tag2+":1b}"
        elif is_tag2 == "n":
            print("Okay! not using a tag!")
            tag2 = ""
        else:
            print("uhh idk what that means so im gonna guess you want no tag")
            is_tag2 = "n"
            tag2 = ""
        print()
        print("result item time!")
        print()
        item3 = input("minecraft item:")
        is_tag3 = input("wanna use a custom tag? (y/n):")
        print()
        if is_tag3 == "y":
            print("Okay! using a tag!")
            tag3 = input("what is the name of your tag?:")
            tag3 = ",tag:{"+tag3+":1b}"
        elif is_tag3 == "n":
            print("Okay! not using a tag!")
            tag3 = ""
        else:
            print("uhh idk what that means so im gonna guess you want no tag")
            is_tag3 = "n"
            tag3 = ""
        print()
        is_name = input("hey, wanna give your result item a custom name? (y/n):")
        if is_name == "y":
            name = input("Okay! What name?:")
            name = ',display:{Name:\'[{"text":"'+name+'","italic":false}]\'}'
        elif is_name == "n":
            print("No name! Got it!")
            name = ""
        else:
            print("no name i guess?")
            name  = ""
        print()
        prt = input("do you want a particle effect to appear when the item is crafted? (y/n):")
        if prt == "y":
            print("quick note: for the particle type,")
            print("if you're using something like dust that has extra requirements")
            print("make sure to include that here.")
            prt_t = input("With that in mind, what type of particle is it?:")
        elif prt == "n":
            print("Okay! Not using particles!")
        else: print("ummmmm i assume that means no particles?")
        
        
        print("Okay, time to generate!")
        input("Ready?")
        print()
        print("instructions: stack each command block on top of each other, facing up, following the command block type given")
        print()
        

        print("repeating, unconditional, always active")
        print('execute at @e[type=item,nbt={Item:{id:"minecraft:'+item1+'",Count:1b'+tag1+'}}] at @e[type=item,distance=..1,nbt={Item:{id:"minecraft:'+item2+'",Count:1b'+tag2+'}}] run summon item ~ ~ ~ {Item:{id:"minecraft:'+item3+'",Count:1b'+tag3+name+'}}')
        print()
        print("chain, conditional, always active")
        print('execute at @e[type=item,nbt={Item:{id:"minecraft:'+item3+'",Count:1b'+tag3+'}}] run kill @e[type=item,distance=..1,nbt={Item:{id:"minecraft:'+item1+'",Count:1b'+tag1+'}}]')
        print()
        print("chain, conditional, always active")
        print('execute at @e[type=item,nbt={Item:{id:"minecraft:'+item3+'",Count:1b'+tag3+'}}] run kill @e[type=item,distance=..1,nbt={Item:{id:"minecraft:'+item2+'",Count:1b'+tag2+'}}]')
        if prt == "y":
            print()
            print("chain, conditional, always active")
            print('execute at @e[type=item,nbt={Item:{id:"minecraft:'+item3+'",Count:1b'+tag3+'}}] run particle '+prt_t+' ~ ~ ~ 0.2 0.2 0.2 0.2 50')
        print()
        input()
    elif simple == "a":
        print()
        print("sorry, this doesnt exist yet")
    else: print("i dont understand that")
