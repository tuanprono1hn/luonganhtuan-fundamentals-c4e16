n = int(input("Nhap n: "))
from turtle import *
speed(-1)
for i in range(0, n, 10):
    forward(10+i)
    left(90)
mainloop()
