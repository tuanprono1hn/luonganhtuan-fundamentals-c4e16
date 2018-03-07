canh = int(input("May thich bao nhieu canh?"))
goc = 360/canh
from turtle import *
shape('turtle')
speed(-1)
color("blue")
fillcolor("orange")
begin_fill()
for i in range(canh):
    forward(100)
    left(goc)
end_fill()
mainloop()
