noc = int(input("How many circles do you want? "))
radius = float(input("Enter the radius, please: "))
goc = 360/noc
from turtle import *
shape("turtle")
color('green')
speed(-1)
fillcolor("pink")
begin_fill()
for i in range(noc):
    circle(radius)
    left(goc)
end_fill()
mainloop()
