from turtle import *

scr = Screen()
scr.bgcolor('black')

trt = Turtle()
trt.width(3)
trt.shape('turtle')
# trt.color('green')
trt.speed('fastest')

#           0       1        2        3         4         5
colors = ['red', 'green', 'blue', 'orange', 'yellow', 'purple']

for x in range(200):
    trt.color(colors[x % 6])
    trt.forward(x * 2)
    trt.left(58)

done()