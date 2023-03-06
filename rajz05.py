from turtle import *

scr = Screen()
scr.bgcolor('black')

trt = Turtle()
trt.width(3)
trt.shape('turtle')
trt.speed('fastest')

trt.color('blue', 'darkgreen')

trt.circle(100, 180)
trt.lt(90)
trt.fd(300)

trt.write('tojásos nokedli', font=('Times New Roman', 40, 'bold'))

done()