from turtle import *
speed(50*100)
bgcolor("black")
color("red")
i = 5
while i <= 200:
    circle(i)
    print(i * "==")
    i = i + 1
    left(5)
    backward(10)