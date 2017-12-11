#CTI 110
#M5T1A drawing square and triangle
#Jeffrey Lee
#17 Oct 2017

#draw shapes using loops





import turtle


def drawSquare(myTurtle, sidelength):
    sides = 4
    angle = 90

    counter = 1

    while counter <= sides:

        art.forward( sidelength )
        art.right( angle )

        counter = counter + 1
        

def drawTriangle(myturtle, sidelength):
    sides = 3
    angle = 45

    counter = 1

    while counter <= sides:
        art.forward( sidelength )
        art.right( angle )

        counter = counter + 1

art = turtle.Turtle()
drawSquare ( art, 200)
drawTriangle (art, 118)
            
