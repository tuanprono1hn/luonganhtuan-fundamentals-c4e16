from random import randint
# num = 84
# n = int(input("Give me a number: "))
# if n == num:
#     print("YO")
# else:
#     print("Wrong")
num = 84
playing = True
count = 0
while playing:
    guess = int(input("Guess:" ))
    if guess > num:
        print("Large")
    elif guess < num:
        print("Small")
    else:
        print("YO")
        # playing= False
        break
    count += 1
    if count == 7:
        print("Loser!!")
        # playing = False
        break
