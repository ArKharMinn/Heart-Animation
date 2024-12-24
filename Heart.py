import math
import turtle as t

def hearta(k):
    return 15 * math.sin(k)**3

def heartb(k):
    return 12 * math.cos(k)-5 * math.cos(2*k)-2*math.cos(3*k)-math.cos(4*k)

t.speed(0)
t.bgcolor('black')

for i in range(10000):
    x = hearta(i)*20
    y = heartb(i)*20
    t.goto(x,y)
    for j in range(5):
        t.color('#f73487')
        t.goto(x,0)
t.done()