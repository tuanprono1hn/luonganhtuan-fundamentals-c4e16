n = int(input("Enter a number: "))
if n % 2 == 0:
    print(int(n/2) * "1 0 ")
else:
    print(int((n-1)/2)*" 1 0","1")
# for i in range(0, n):
#     print(i*"0 1 ", end = "")
# for i in range(0, n):
#     for j in range(0, 2):
#         print(j, end=" ")

    # for i in range(1, n + 1, 1):
    # for j in range(1, 2):
    #     for k in range(0, 1):
    #         print(j, k, end = " ")
