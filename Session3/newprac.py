menu = ["rau muong", "ga ham thuoc bac", "suong xao chua ngot", "trau gac bep"]
for index, item in enumerate(menu):
    print(index + 1, ". ", item, sep="")
# position = int(input("What do you want to delete? "))
# menu.remove(menu[position - 1])
# for index, item in enumerate(menu):
#     print(index + 1, ". ", item, sep="")
thing = input("What do you want to delete? ")
if thing in menu:
    menu.remove(thing)
else:
    print("not found")
# menu.remove(thing)
for index, item in enumerate(menu):
    print(index + 1, ". ", item, sep="")
# menu.pop(position - 1)
# del (position - 1)
