from turtle import Turtle
from random import random

def random_color():
    return(random(),random(),random())

nibles = Turtle()
nibles.pensize(7)
nibles.speed(1000000000000)
for counter in range(1,200):
    nibles.pencolor(random_color())
    nibles.right(10)
    nibles.forward(150)
    nibles.right(100)
    nibles.left(200)
    nibles.forward(20)
    nibles.left(100)
    nibles.right(20)
    
    
