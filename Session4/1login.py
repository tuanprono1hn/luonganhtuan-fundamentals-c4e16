print("Hi, this is a superuser gateway")

count = 0

while True:
    username = input("Username: ")

    if username != "c4e":
        print("You're not a superuser")
    else:
        password = input("Password: ")
        if password != "c4e16":
            print("Incorrect")
        else:
            print("Welcome", username)
            break
    count += 1
    if count == 3:
        print("Go away!!!")
        break
