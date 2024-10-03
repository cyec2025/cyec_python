#Single-User Dungeon RPG
#By CYeC, June 2020
#

import random

#current prompts: Combat: attack, heal, equipment. Noncombat: north, south, west, east, stat, equipment, wait, heal, take,
equipment = ["H. Potion",]
environment = 0
redy = 0
w_redy = 0
x_pos = 0
y_pos = 0
max_hp = 10
hp = 10
at = 0
df = 0
lv = 1
xp = 0
dg = 0
heal = 0
min_heal = 0
max_heal = 0 
min_dg = 1
max_dg = 3
max_xp = 10
enemy = 0
e_hp = 0
e_df = 0
e_dg = 0
e_min_dg = 0
e_max_dg = 0
e_dis = 0
xp_r = 0
e = 0
w = 0
n = 0
s = 0
enc = 0
regen = 0
gold = random.randint(40,160)
treeloot = []
armor = 0
temp_df = 0
input("Long ago...")
input("the world was in peace")
input("then... A legendary beast")
input("the DRAGON attacked...")
input("the world was thrown out of balance")
input("Who will slay the dragon and free the world...?")
input("Who will embark on the...")
print("")
print("")
print("")
input("""***********
DRAGONQUEST
***********""")
print("prompts: combat: attack, heal, equipment. noncombat: north, south, west, east, stat, equipment, wait, heal, take")



while hp > 0:


#leveling up
    if xp > max_xp-1:
        print("Level up!")
        lv += 1
        xp -= max_xp
        max_xp += 10
        max_hp += random.randint(2, 5)
        hp = max_hp
        at += random.randint(1, 2)
        df += random.randint(0, 1)
        print("Reached level",lv)

#rooms
#y+ north y- south x+ west x- east
    if x_pos == 0 and y_pos == 0:
        print("""You are in a small cabin, there is a field to the east and north, there is a cave to the south""")
        environment = 0
        n = 1
        w = 0
        e = 1
        s = 1
    elif x_pos == 0 and y_pos == 1:
        print("""You are in a large field, there is a cabin to the south, the field continues to the north and west""")
        environment = 1
        n = 1
        w = 1
        s = 1
        e = 0
    elif x_pos == 2 and y_pos == -1:
        print("""A scorched village... Fallen pray to the DRAGON, cave exit to the south""")
        environment = 1
        n = 1
        w = 1
        s = 1
        e = 0
    elif x_pos == 2 and y_pos == 2:
        print("""You are in a large field, in front a huge tree, the field continues to the south and east there is a huge lake to the north""")
        environment = 0
        n = 1
        w = 0
        s = 1
        e = 1
    elif x_pos == 2 and y_pos == 3:
        print("""You are in next to a huge lake, mist surrounds you on all sides...""")
        environment = 4
        n = 1
        w = 1
        s = 1
        e = 1
    elif x_pos == 0 and y_pos == 3:
        print("""You are in a swamp, there are flies buzzing around, the bog is too thick to see through""")
        environment = 3
        n = 0
        w = 1
        s = 1
        e = 0
    elif x_pos == 1 and y_pos == 3:
        print("""You are in a swamp, there are flies buzzing around, the bog is too thick to see through""")
        environment = 3
        n = 0
        w = 1
        s = 1
        e = 1
    elif x_pos == -1 and y_pos == 2:
        print("""You are in a swamp, there are flies buzzing around, the bog is too thick to see through""")
        environment = 3
        n = 0
        w = 1
        s = 0
        e = 0
    elif x_pos == 2 and y_pos == 4:
        print("""You are next to a huge lake, mist surrounds you on all sides...""")
        environment = 4
        n = 1
        w = 1
        s = 1
        e = 1
    elif x_pos == 3 and y_pos == 4:
        print("""You are next to a huge lake, mist surrounds you on all sides...""")
        environment = 4
        n = 0
        w = 0
        s = 1
        e = 1
    elif x_pos == 3 and y_pos == 3:
        print("""You are next to a huge lake, mist surrounds you on all sides...""")
        environment = 4
        n = 1
        w = 0
        s = 0
        e = 1
    elif x_pos == 1 and y_pos == 1:
        print("""You are in a large field, the field continues to the north, east and west""")
        environment = 1
        n = 1
        w = 1
        s = 0
        e = 1
    elif x_pos == 2 and y_pos == 1:
        print("""You are in a large field, the field continues to the east, to the north there is a large tree""")
        environment = 1
        n = 1
        w = 0
        s = 0
        e = 1
    elif x_pos == 0 and y_pos == 2:
        print("""You are in a large field, the field continues to the south and west, to the north and east there is swamplands""")
        environment = 1
        n = 1
        w = 1
        s = 1
        e = 1
    elif x_pos == 1 and y_pos == 2:
        print("""You are in a large field, the field continues to the south and west, to the north and east there is swamplands""")
        environment = 1
        n = 1
        w = 1
        s = 1
        e = 1
    elif x_pos == -1 and y_pos == 0:
        print("""You are in a large field, there is a cabin to the west, the field continues to the south""")
        environment = 1
        n = 0
        w = 1
        s = 1
        e = 0
    elif x_pos == -1 and y_pos == -1:
        print("""You are in a large field, there is a cave to the west, the field continues to the north""")
        environment = 1
        s = 0
        e = 0
        n = 1
        w = 1
    elif x_pos == 0 and y_pos == -1:
        print("""You are in a cave, there is a cabin to the north, a field to the east, the cave continues downward to the south""")
        environment = 2
        w = 0
        n = 1
        s = 1
        e = 1
    elif x_pos == 0 and y_pos == -2:
        print("""You are in a cave, the cave continues to the south, north and west""")
        environment = 2
        n = 1
        e = 0
        s = 1
        w = 1
    elif x_pos == 1 and y_pos == -2:
        print("""You are in a cave, the cave continues to the west, and east""")
        environment = 2
        n = 0
        e = 1
        s = 0
        w = 1   
    elif x_pos == 2 and y_pos == -2:
        print("""You are in a cave, the cave continues to the east, the cave opens up to a town to the north""")
        environment = 2
        n = 1
        e = 1
        s = 0
        w = 0
    elif x_pos == 0 and y_pos == -3:
        print("""You are in a cave, the cave continues to the north, and opens up to the south into some plains""")
        environment = 2
        n = 1
        e = 0
        s = 1
        w = 0
    elif x_pos == 0 and y_pos == -4:
        print("""You are in a barren plains surrounded on all sides with huge cliffs, there is an exit into a cave to the north,
something seems ominous about this place...""")
        environment = 99
        n = 1
        e = 0
        s = 0
        w = 0
    else:
        print("ERROR: Room does not exist")
#loot
    if y_pos == 2 and x_pos == 2:
        if w_redy == "take":
            print("took",treeloot,)
            treeloot.clear
#loot tables
#loot IDs: 1-H. potion 2-sword 3-chainmail 4-axe 5-hammer 6-special potion 7-platemail 8-XP ring 9-GOLD ring 10-LV ring

        
        
#non combat commands
    print (x_pos, y_pos)
    w_redy = input("What do you do?:")
    if w_redy == "east" and e == 1:
        x_pos -= 1
        enc = random.randint(0,5)
    elif w_redy == "west" and w == 1:
        x_pos += 1
        enc = random.randint(0,5)
    elif w_redy == "north" and n == 1:
        y_pos += 1
        enc = random.randint(0,5)
    elif w_redy == "south" and s == 1:
        y_pos -= 1
        enc = random.randint(0,5)
    elif w_redy == "equipment":
        print(equipment)
        enc = random.randint(0,5)
    elif w_redy == "stat":
        print("HP:",hp,"/",max_hp,"LV:",lv,"XP:",xp,"/",max_xp,"ATK:",at,"DEF:",df, "GOLD:",gold,)
        enc = random.randint(0,5)
    elif w_redy == "wait" or w_redy == "w":
        print("...")
        enc = random.randint(0,5)
    elif w_redy == "heal":
            if "H. Potion" in equipment:
                
                heal = random.randint(4, 10)
                print("you healed", heal, "Hit points!")
                hp += heal
                equipment.remove("H. Potion")
#natural regen
    if hp < max_hp:
        regen = random.randint(0,1)
        hp += regen
        
#encounters
    if enc == 5:
        if environment == 1:
                enemy = random.randint(1,2)
                if enemy == 1:
                    print("a squishy-looking slime attacks!")
                else: print("a goblin with an evil grin on its face attacks!")
        if environment == 2:
                enemy = random.randint(3,4)
                if enemy == 3:
                    print("a screeching cave bat attacks!")
                else: print("a slow, grumbling, stone golem attacks!")
        if environment == 3:
                enemy = random.randint(5,7)
                if enemy == 5:
                    print("a greasy troll attacks!")
                elif enemy == 6:
                    print("an tough-looking orc attacks!")
                else: print("a slimey swamp monster attacks!")
        if environment == 4:
                enemy = random.randint(8,9)
                if enemy == 7:
                    print("a terrifying sea monster attacks!")
                else: print("a gigantic squid attacks!")
        if environment == 99:
                enemy = 10
                print("the huge, snarling, legendary dragon attacks!")
            
        
#enemies
    if enemy == 1:
        e_dis = "slime"
        e_hp = random.randint(2, 4)
        e_df = 0
        e_min_dg = 1
        e_max_dg = 2
        xp_r = 4
        gold_r = random.randint(10,15)
    if enemy == 2:
        e_dis = "goblin"
        e_hp = random.randint(3, 7)
        e_df = 0
        e_min_dg = 1
        e_max_dg = 3
        xp_r = 7
        gold_r = random.randint(20,30)
    if enemy == 3:
        e_dis = "cave bat"
        e_hp = random.randint(5, 8)
        e_df = 0
        e_min_dg = 2
        e_max_dg = 3
        xp_r = 9
        gold_r = random.randint(5,10)
    if enemy == 4:
        e_dis = "lesser stone golem"
        e_hp = random.randint(9, 12)
        e_df = 1
        e_min_dg = 1
        e_max_dg = 2
        xp_r = 12
        gold_r = random.randint(6,15)
    if enemy == 5:
        e_dis = "troll"
        e_hp = random.randint(12, 16)
        e_df = 2
        e_min_dg = 5
        e_max_dg = 8
        xp_r = 30
        gold_r = random.randint(10,50)
    if enemy == 6:
        e_dis = "orc"
        e_hp = random.randint(9, 11)
        e_df = 1
        e_min_dg = 4
        e_max_dg = 7
        xp_r = 20
        gold_r = random.randint(20,50)
    if enemy == 7:
        e_dis = "swamp monster"
        e_hp = random.randint(8, 16)
        e_df = 5
        e_min_dg = 5
        e_max_dg = 8
        xp_r = 40
        gold_r = random.randint(10,30)
    if enemy == 8:
        e_dis = "sea monster"
        e_hp = random.randint(15, 25)
        e_df = 5
        e_min_dg = 6
        e_max_dg = 8
        xp_r = 60
        gold_r = random.randint(50,70)
    if enemy == 9:
        e_dis = "giant squid"
        e_hp = random.randint(20, 30)
        e_df = 5
        e_min_dg = 6
        e_max_dg = 10
        xp_r = 70
        gold_r = random.randint(55,65)   
    if enemy == 10:
        e_dis = "legendary dragon"
        e_hp = random.randint(60, 80)
        e_df = 8
        e_min_dg = 1
        e_max_dg = 15
        xp_r = 500
        gold_r = random.randint(1000,2250)

#combat
    while enemy > 0:
        print ("Enemy:",e_dis)
        redy = input("input:")
        if redy == "attack":
            print ("you attack!")
            dg = random.randint(min_dg, max_dg) + at
            dg -= e_df
            if dg < 1:
                dg = 0
            print ("you deal", dg, "damage!")
            e_hp -= dg
            if e_hp < 1:
                print("You win!")
                xp += xp_r
                gold += gold_r
                print("you gained",xp_r,"xp, and", gold_r, "gold!" )
                if enemy == 10:
                    input("You freed the land of the terrible dragon...")
                    input("Everyone rejoiced and a huge feast was held in your honor.")
                    print("THE END")
                    input("""***********
DRAGONQUEST
***********""")
                    exit()
                enc = 0
                enemy = 0
                break
        if redy == "heal":
            if "H. Potion" in equipment:
                
                heal = random.randint(4, 10)
                print("you healed", heal, "Hit points!")
                hp += heal
                equipment.remove("H. Potion")
            else: print("You don't have a potion!")
        if redy == "equipment":
            print(equipment)
        print(e_dis, "attacks!")
        e_dg = random.randint(e_min_dg, e_max_dg)
        e_dg -= (df+temp_df)
        if e_dg < 1:
            e_dg = 0
        print(e_dis, "deals", e_dg, "damage!")
        hp -= e_dg
        if hp < 1:
            print("You died!")
            break
        if hp > max_hp:
            hp = max_hp
        print("HP:",hp,"/",max_hp)
