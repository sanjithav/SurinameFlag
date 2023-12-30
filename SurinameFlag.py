# File: SurinameFlag.py
# Student: Sanjitha Venkata
# UT EID: sv28325
# Course Name: CS303E
# 
# Date: 11/14/2023
# Description of Program: Draws the flag of Suriname with Turtle Graphics

from turtle import *

#define colors
myGreen = (0.224, 0.494, 0.247) 
myRed = (0.706, 0.043, 0.18)
myYellow= (0.925, 0.784, 0.11) 

#define turtle
t=Turtle()
t.pensize(1)
t.speed(0)

#rectangle methods
def drawRectangle(x1,y1, x2,y2, x3,y3, x4,y4, color):
    t.up()
    t.goto(x1,y1)
    t.down()
    t.fillcolor(color)
    t.begin_fill()
    t.goto(x2,y2)
    t.goto(x3,y3)
    t.goto(x4,y4)
    t.goto(x1,y1)
    t.end_fill()

def drawRectWithoutFill(x1,y1, x2,y2, x3,y3, x4,y4):
    t.up()
    t.goto(x1,y1)
    t.down()
    t.goto(x2,y2)
    t.goto(x3,y3)
    t.goto(x4,y4)
    t.goto(x1,y1)
    
#star method
def drawStar(x1,y1, length, color):
    t.up()
    t.goto(x1,y1)
    t.down()
    t.begin_fill()
    t.fillcolor(color)
    t.left(-108)
    t.forward(length)
    for i in range(5):
        t.left(-72)
        t.forward(length)
        t.left(144)
        t.forward(length)
    t.end_fill()


#top green box
drawRectangle(-300, 300, 300, 300, 300, 220, -300, 220, myGreen)
#bottom green box
drawRectangle(-300, -100, -300, -20, 300, -20, 300, -100, myGreen)
#middle red box
drawRectangle(-300, 180, -300, 20, 300, 20, 300, 180, myRed)
#outer box
drawRectWithoutFill(-300, 300, 300, 300, 300, -100, -300, -100)
#star
drawStar(0,175, 60, myYellow)


t.hideturtle()
turtle.done()
