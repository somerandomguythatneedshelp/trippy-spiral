from turtle import *

hideturtle()
speed(0)
bgcolor("black")
colormode(255)
color((78,253,84))

for i in range(155):
    right(i)
    circle(125, i)
    forward(i)
    right(90)

done()    