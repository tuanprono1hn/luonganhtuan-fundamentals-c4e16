a = int(input("How many B bacterias are there? "))
b = int(input("How much time in minuntes will we wait? "))
c = b // 2
if a > 0 and b>=0:
    print("After", b, "minuntes, we would have", a * 2 ** c, "bacterias")
