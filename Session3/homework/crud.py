items = ["T-shirt", "Sweater"]
def read():
    print("Our items: ", end = "")
    print(*items, sep=", ")
    print()
def creat():
    new = input("Enter new item: ")
    items.append(new)
    read()
def update():
    pos = int(input("Update position: "))
    if pos <= len(items):
        new = input("Enter new item: ")
        items[pos - 1] = new
        read()
    else:
        print("Out of range! Enter position again...")
def delete():
    pos = int(input("Delete position: "))
    if pos <= len(items):
        del items[pos - 1]
        read()
    else:
        read()
i = True
while i:
    n = input("Welcome to our shop, what do you want? (C R U D) ")
    if n == "C":
        creat()
        print("To exit, enter E")
    elif n == "U":
        update()
        print("To exit, enter E")
    elif n == "D":
        delete()
        print("To exit, enter E")
    elif n == "R":
        read()
        print("To exit, enter E")
    elif n == "E":
        print("Thanks for shopping")
        i = False
    else:
        print("You're noob!!!")
