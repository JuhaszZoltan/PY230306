from random import randint
from turtle import *

scr = Screen()
scr.bgcolor('black')

trts:list[Turtle] = []
for x in range(6):
    trts.append(Turtle())
    trts[x].speed(0)
    red:int = randint(0, 255)
    green:int = randint(0, 255)
    blue:int = randint(0, 255)
    trts[x].color(f'#{red:02X}{green:02X}{blue:02X}')
    trts[x].width(2)
    h:int = scr.window_height() / 2
    w:int = scr.window_width() / 2
    trts[x].pu()
    trts[x].goto(randint(-w, w), randint(-h, h))
    trts[x].pd()

for x in range(200):
    for t in trts:
        t.fd(x)
        t.lt(56)

done()