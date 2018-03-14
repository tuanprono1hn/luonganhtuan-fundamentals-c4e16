from turtle import *
shape("circle")
color("blue")
speed(-1)
canh = 10
for i in range(80):
    for j in range(4):
        forward(canh)
        left(90)
    canh += 5
    left(10)
mainloop()
