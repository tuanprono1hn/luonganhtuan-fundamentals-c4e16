from turtle import *
shape("arrow")
speed(-1)
colors = ["red", "blue", "brown", "yellow", "grey"]
rong = 50
dai = 125
for i in range(len(colors)):
    color(colors[i])
    begin_fill()
    for j in range(2):
        right(90)
        forward(rong)
        right(90)
        forward(dai)
    dai -= 25
    end_fill()
mainloop()
