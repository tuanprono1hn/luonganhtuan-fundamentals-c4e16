# from random import *
# while True:
#     a = randint(0, 100):
#     n = input("is {0} your number? ".format(50))
#     if n == "l":
#
#         print("is", a, "your number?")
#         if a >= 50:

# string formatting
# ans = input("is {0} your number? ".format(50))

print("Guess your number game")
input("now think of a number from 0 - 100, then press Enter")
print("""
All you have to is answer to my Guess
'c' if correct
's' if small
'l' if large
""")

low = 0
hight = 100
while True:
    mid = (low + hight) // 2

    ans = input("Is {0} your number? ".format(mid)).lower()

    if ans == "c":
        print("I knew it!")
        break
    elif ans == "l":
        hight = mid
    elif ans == "s":
        low = mid
    else:
        print("Lose")
