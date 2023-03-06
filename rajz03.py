from turtle import *

scr = Screen()
scr.bgcolor('black')

trt = Turtle()
trt.width(3)
trt.shape('turtle')
trt.speed('fastest')

for x in range(256):
    trt.color(f'#{255-x:02X}0000', 'green')
    trt.lt(58)
    trt.fd(x)

done()