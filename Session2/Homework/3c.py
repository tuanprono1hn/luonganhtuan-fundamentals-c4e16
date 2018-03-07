n = int(input("Input number: "))
for i in range(1, n):
    for j in range(1, n):
        print(i * j, end="\t")
    print("\n")
