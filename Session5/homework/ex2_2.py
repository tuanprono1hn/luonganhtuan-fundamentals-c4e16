number = [1, 6, 8, 1, 2, 1, 5, 6]
print(number)
n = int(input("Enter a number: "))
count = {}
for i in number:
    count[i] = count.get(i, 0) + 1
print("{} appears {} times in my list".format(i, count[i]))
