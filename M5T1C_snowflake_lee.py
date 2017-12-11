#CTI 110
#M5T1C drawing snowflake
#Jeffrey Lee
#17 Oct 2017

#draw snowflake with turtle

import turtle
wn = turtle.Screen()
art = turtle.Turtle()
wn.bgcolor("grey")
art.color("blue")

for i in range(10):
    for i in range(2):
        art.forward(80)
        art.right(60)
        art.forward(80)
        art.right(120)
    art.right(36)


        


wn.exitonclick()
    



