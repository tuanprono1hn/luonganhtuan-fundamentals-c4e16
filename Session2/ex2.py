hang = int(input("Nhap so hang: "))
print()
if hang >= 1:
    for i in  range(hang + 1):
        print((hang-i) * " ", i * "* ")
    print()
