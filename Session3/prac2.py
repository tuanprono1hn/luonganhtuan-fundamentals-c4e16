# fd1 = "rau muong"
# fd2 = "com rang rua bo"
# fd3 = "pho"
# fd4 = "suon xao chua ngot"
# fd5 = "ga ham thuoc bac"

menu = ["rau muong", "ga ham thuoc bac", "suong xao chua ngot", "trau gac bep"]
# separator
# print(*menu, sep=", ")
#
# menu.append("bun cha")
# print(*menu, sep=", ")
# lenght
# print(len(menu))
# print(menu[-1])

# for i in range(len(menu)):
#     print(i + 1, ". ", menu[i], sep="")

# for index, item in enumerate(menu):
#     print(index + 1, ". ", item, sep="")

# for item in menu:
#     print(item)
# print("_" * 20)

# menu[0] = "rau ren"
# print(*menu)

print("The list: ")
for index, item in enumerate(menu):
    print(index + 1, ". ", item, sep="")
p = int(input("Position you want to update: "))
if p > len(menu):
    n = input("Ban muon them gi? ")
    menu.append(n)
else:
    m = input("Ban muon sua gi? ")
