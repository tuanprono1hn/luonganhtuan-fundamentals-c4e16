# # # for i in range(5, 1, -1):
# # #     print(i)
# # # font = int(input("Enter font size: "))
# # # cao = int(font * 1.5)
# # # for k in range(cao, (cao - 2), 1):
# # #     print(k)
# # # for i in range(10):
# # #     print(i * "* ")
# # # print("**  **  **")
# # # print("****  ****")
# # font = int(input("Enter font size: "))
# # cao = int(font * 1.5)
# # if font < 6:
# #     print("Fail")
# # else:
# #     print(font * "* ", 3 * "  ", font * "* ", 3 * "  ", (font - 2) * "* ", 5 * "  ", font * "* ")
# #     for i in range(1, 3, 1):
# #         print(1 * "* ",(font + 2) * "  ", 1 * "* ",(font - 3) * "  ", 1 * "* ", 3 * "  ", 1 * "* ", (font + i - 5) * "  ", 1 * "* ", (5 - i) * "  ", 1 * "* ")
# #     for j in range(3, int(cao/2 - 1), 1):
# #         print(1 * "* ",(font + 2) * "  ", 1 * "* ",(font - 3) * "  ", 1 * "* ", 3 * "  ", 1 * "* ", (font - 3) * "  ", 1 * "* ", 3 * "  ", 1 * "* ")
# #     for k in range(int(cao/2 - 1), int(cao/2), 1):
# #         print(1 * "* ",(font + 2) * "  ", 1 * "* ",(font - 3) * "  ", 1 * "* ", 3 * "  ", 1 * "* ", (font - 3) * "  ", 1 * "* ", 3 * "  ", font * "* ")
# #     for l in range(int(cao/2), (cao - 2), 1):
# #         print(1 * "* ",(font + 2) * "  ", 1 * "* ",(font - 3) * "  ", 1 * "* ", 3 * "  ", 1 * "* ", (font - 3) * "  ", 1 * "* ", 3 * "  ", 1 * "* ")
# #     for m in range(cao, (cao - 2), -1):
# #         print(1 * "* ",(font + 2) * "  ", 1 * "* ",(font - 3) * "  ", 1 * "* ", 3 * "  ", 1 * "* ", (font - 3 + m - cao) * "  ", 1 * "* ", (font + 3 - font - m + cao) * "  ", 1 * "* ")
# #     print(font * "* ", 3 * "  ", font * "* ", 3 * "  ", (font - 2) * "* ", 5 * "  ", font * "* ")
# side = 2*int(input('Input the size: '))+1
# # print CODE
# for i in range(side):
#     if i==0 or i==side-1:
#         for j in range(side):
#             print("* ", end=(''))
#         print(' ',end=(''))
#         for j in range(side):
#             print("* ", end=(''))
#         print(' ',end=(''))
#         for j in range(int(side/2)+1):
#             print("* ", end=(''))
#         for j in range(side - int(side/2)-1):
#             print('  ', end=(''))
#         print(' ',end=(''))
#         for j in range(side):
#             print("* ", end=(''))
#         print()
#     elif i==int(side/2):
#         print('* ',end=(''))
#         for j in range(side-1):
#             print('  ', end=(''))
#         print(' ', end=(''))
#         for f in range(2):
#             for j in range(side):
#                 if j==0 or j==side-1:
#                     print('* ',end=(''))
#                 else:
#                     print('  ',end=(''))
#             print(' ', end=(''))
#         for j in range(int(side/2)+1):
#             print('* ',end=(''))
#         for j in range(side-int(side/2)-1):
#             print('  ', end=(''))
#         print()
#     else:
#         #C
#         print('* ', end=(''))
#         for j in range(side-1):
#             print('  ', end=(''))
#         print(' ', end=(''))
#         #O
#         for j in range(side):
#             if j==0 or j==side-1:
#                 print('* ', end=(''))
#             else:
#                 print('  ', end=(''))
#         print(' ', end=(''))
#         #D
#         if i<int(side/2):
#             for j in range(side):
#                 if j==0 or j==side-1 + i - int(side/2):
#                     print('* ', end=(''))
#                 else:
#                     print('  ', end=(''))
#             print(' ', end=(''))
#         else:
#             for j in range(side):
#                 if j==0 or j==side-1 - i + int(side/2):
#                     print('* ', end=(''))
#                 else:
#                     print('  ', end=(''))
#             print(' ', end=(''))
#         #E
#         print('*')
from turtle import *

shape('arrow')
color('red')
speed(-1)

penup()
goto(-100,100)
pendown()

for i in range(4):
    for j in range(2):
        forward(50)
        left(45)
        forward(50)
        left(135)
    left(90)

penup()
goto(100,-100)
pendown()

so_canh = 6
lenght = 100
for l in range(so_canh):
    if so_canh == 5 or so_canh == 3:
        color('blue')
    else:
        color('red')
    for l in range(so_canh):
        forward(lenght)
        left(360/so_canh)
    so_canh -= 1













mainloop()
