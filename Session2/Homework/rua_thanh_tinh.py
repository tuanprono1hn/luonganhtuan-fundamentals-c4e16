from turtle import *

shape("arrow")
color("green")
speed(-1)
fillcolor("pink")
right(30)
begin_fill()
for i in range(4):
    for j in range(2):
        forward(100)
        left(60)
        forward(100)
        left(120)
    left(90)
end_fill()
mainloop()
