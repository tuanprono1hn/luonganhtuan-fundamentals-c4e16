from random import *
wordlist = ["kimochi", "impossible", "anime", "biological", "animation"]

count = 0
playing = True
for i in range(3):
    word = choice(wordlist)
    characters = list(word)
    while playing:
        shuffle(characters)
        print(characters)
        n = input("Guess: ")
        if n == word:
            print("Hura!!!")
            playing = False
        count += 1
        if count == 3:
            print("Noober!!!")
            playing = False
