n= int(input("Nhap so canh: "))
for i in range(n):
    for j in range(n):
        if j >= n - 1 - i:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()
