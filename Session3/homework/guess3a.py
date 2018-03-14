from random import *
characters = list("champion")
# print(characters)
count = 0
playing = True
while playing:
    shuffle(characters)
    print(characters)
    n = input("Guess: ")
    if n == "champion":
        print("Hura!!!")
        playing = False
    count += 1
    if count == 3:
        print("Noober!!!")
        playing = False
# for i in range(len(characters)):
#     n = choice(characters)
#
#     print(n, end=" ")
