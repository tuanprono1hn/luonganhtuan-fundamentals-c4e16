n = int(input("Enter number: "))
for i in range(n):
    for j in range(n):
        print(1 - ((i+j)% 2), end=' ')
    print()
# if n % 2 == 0:
#     for l in range(1, int(n/2) + 1):
#         for i in range(1, int(n/2)+1):
#             for j in range(0, 2):
#                 for k in range(1, 2):
#                     print(j*k, end="\t")
#         print("\n")
#         # for m in range(1, int(n/2)+1):
#         #     for p in range(1, -1, -1):
#         #         for q in range(1, 2):
#         #             print(q*p, end="\t")
# for l in range(1, n + 1):
#     for i in range(4):
#         print("1","\t","0", end = "\t")
#     for k in range(4):
#         print("0","\t","1", end = "\t")
