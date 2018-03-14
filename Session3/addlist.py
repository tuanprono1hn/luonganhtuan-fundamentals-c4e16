print("Hi, Dude!!! List the things that you love:")
menu = ["anime", "game", "sport", "book"]
print(*menu, sep=", ")
n = input("Do you need to add sthg?")
print()
menu.append(n)
print(*menu, sep=", ")
