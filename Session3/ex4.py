# num = 9999
# count = 0
# while True:
#     num = num // 10
#     count += 1
#     break
num = int(input("Enter number: "))
count = 0
while True:
    num = num // 10
    count += 1
    if num == 0:
        break
print(count)
