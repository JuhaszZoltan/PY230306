from turtle import *

scr = Screen()
scr.bgcolor('black')

trt = Turtle()
trt.width(3)
trt.shape('turtle')
trt.speed('fastest')

#           0       1        2        3         4         5
colors = ['red', 'green', 'blue', 'orange', 'yellow', 'purple']

trt.color('white')

for x in range(4):
    trt.fd(200)
    trt.lt(90)

trt.lt(90)
trt.fd(200)

trt.color('firebrick')

trt.rt(30)
trt.fd(200)
trt.rt(120)
trt.fd(200)

done()
