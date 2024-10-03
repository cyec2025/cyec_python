import random

head = {"X":0,"Y":0}
class segment:
    def __init__(self, x, y, num):
        print("sauce")

width = 10

while True:
    space_xl = head["X"]
    space_xr = width - head["X"]

    draw_xl = ""
    add = "o"
    for i in range(1,space_xl):
        draw_xl = draw_xl + add
    draw_xr = ""
    for i in range(1,space_xr):
        draw_xr = draw_xr + add
    print(draw_xl+"O"+draw_xr)
    command = input("prompt:")
    if command == "l" and head["X"] > 0:
        head["X"] = head["X"] - 1
    if command == "r" and head["X"] < width:
        head["X"] = head["X"] + 1
    
        
