from turtle import *
shape("turtle")
color("red")
speed(-1)
canh = 6
for i in range(3, canh + 1):
    if i == 3 or i == 5:
        color("blue")
    else:
        color("red")
    for j in range(i):
        forward(100)
        left(360/i)

mainloop()
