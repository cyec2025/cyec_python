# Assignment 10: Pig Latin
# Author: CYeC
# Date: 2022-04-30

vowels = "aeiouy"



def ask():
    global words
    # input words to be translated
    words = input("Words: ")

def translate():
    global words
    global pig_words
    global vowels
    # lowercase
    words = words.lower()
    # remove punctuation
    words = words.replace(".","")
    words = words.replace(",","")
    words = words.replace("?","")
    words = words.replace("!","")
    # split words into list
    words = words.split()
    # translate
    for i in range(len(words)):

        if words[i][0] == "y":
            vowels = "aeiou"
        if vowels.find(words[i][0]) > -1:
            # translate vowel starter words
            pig_words.append(words[i]+"way")
        else:
            # translate consonant starter words
            i2 = 0
            first_cons = ""
            while True:
                if words[i][i2] in vowels:
                    break
                else:
                    first_cons += words[i][i2]
                    i2 += 1
            new_word = words[i]
            new_word = new_word.replace(first_cons,"")
            new_word = new_word + first_cons + "ay"
            pig_words.append(new_word)
        vowels = "aeiouy"
def main():
    global pig_words
    print("Pig Latin Machine")
    while True:
        pig_words = []
        # run functions
        ask()
        translate()
        # print results
        readable = ""
        for i in pig_words:
            readable = readable + i + " "
        print(readable)
if __name__ == "__main__":
    main()
