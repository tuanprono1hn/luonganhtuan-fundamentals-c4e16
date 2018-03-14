n = [1, 5, 10, 35, 64, 89, 26, 76, 93, 100]
sortedlist = []
while True:
    minnum = min(n)
    sortedlist.append(minnum)
    n.remove(minnum)
    if len(n) == 0:
        break
print(sortedlist)
