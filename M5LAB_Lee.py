#CTI 110
#M5LAB nested loop
#Jeffrey Lee
#17 Oct 2017

#draw nested loop snowflake with turtle

import turtle
wn = turtle.Screen()
art = turtle.Turtle()

wn.bgcolor("black")
art.color("green")
for i in range(10):
    for i in range(2):
        art.forward(40)
        art.right(60)
        art.forward(80)
        art.right(120)
    art.right(36)
art.color("red")
for i in range(10):
    for i in range(2):
        art.forward(80)
        art.right(60)
        art.forward(80)
        art.right(120)
    art.right(72)
art.color("orange")
for i in range(10):
    for i in range(2):
        art.forward(100)
        art.right(60)
        art.forward(80)
        art.right(120)
    art.right(108)

        
        


wn.exitonclick()
    
