from turtle import *
shape("turtle")
speed(-1)
colors = ["red", "blue", "brown", "yellow", "grey"]
so_canh = 3
for i in range(len(colors)):
    color(colors[i])
    for j in range(so_canh):
        forward(100)
        left(360/so_canh)
    so_canh += 1
mainloop()
