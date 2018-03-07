from turtle import *
shape("turtle")
color("red")
speed(-1)
canh = 6
for i in range(canh):
    if canh == 3 or canh == 5:
        color("blue")
    else:
        color("red")
    for i in range(canh):
        forward(100)
        left(360/canh)
    canh -= 1

mainloop()
