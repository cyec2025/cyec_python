print("text saver")
with open('texter.txt','r') as load:
            text = load.read()
            load.close()
while True:
    state = input("save or load text?:")
    if state == "save":
        print("save mode")
        text = input("Text: ")
        with open('texter.txt', 'w') as save:
            save.write(str(text))
    if state == "load":
        print("load mode")
        with open('texter.txt','r') as load:
            text = load.read()
            load.close()
        print("Text:",text)
    else: print("use 'save' or 'load'")
