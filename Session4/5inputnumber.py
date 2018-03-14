n = input("Nhap day so: ")
n = n.split(" ")
# cha = list(n)
sortedlist = []
for i in n:
    sortedlist.append(int(i))
issorted = True
for j in range(len(sortedlist)-1):
    if sortedlist[j] > sortedlist[j+1]:
        issorted = False
        break
if issorted:
    print("sorted")
else:
    print("not sorted")
