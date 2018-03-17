dic = {"hc" : "Hoc",
    "ng" : "Nguoi",
    "stt" : "status",
    "any" : "Anh nguoi yeu"
}

# for key in dic:
#     print(key, end="  ")
# print()
while True:
    for key in dic:
        print(key, end="  ")
    print()
    n = input("Your code? ")
    if n in dic:
        print("Code: ", n)
        print("Translation: ", dic[n])
    else:
        m = input("Not found! Do you want to contridute this word? (y/n) ")
        if m == "y":
            o = input("Enter your translation: ")
            print("Updated")
            dic[m] = o
            print("Code: ", n)
            print("Translation: ", o)
            print()
            # for key in dic:
            #     print(key, end="  ")
            # print()
        elif m == "n":
            print("Thanks you!")
            break
        else:
            print("Retry!!!")
