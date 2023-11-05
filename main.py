import turtle

draw = turtle.Turtle()

#for i in range (4):
    #draw.forward(100)
    #draw.right(90)

#num_sides = 50
#side_leght = 60
#angle = 360.0 / num_sides

#for i in range(num_sides):
   # draw.forward(side_leght)
    #draw.right(angle)



#window = turtle.Screen()
#window.bgcolor("pink")
#window.title("My window For Turtle")

#draw.color("yellow")

#def shapefun(size, sides):
    #for i in range(sides):
        #draw.fd(size)
        #draw.left(360.0 / sides)

        #size = size * 1

#shapefun(150, 4)
#shapefun(130, 4)
#shapefun(110, 4)
#shapefun(90, 4)
#shapefun(70, 4)
#shapefun(50, 4)
#shapefun(30, 4)
#shapefun(10, 4)
#shapefun(-10, 4)
#shapefun(-30, 4)
#shapefun(-50, 4)
#shapefun(-70, 4)
#shapefun(-90, 4)
#shapefun(-110, 4)
#shapefun(-130, 4)
#shapefun(-150, 4)

#window2 = turtle.Screen()
#pen = turtle.Pen()
#pen.penup()
#pen.goto(-220, 50)
#penpendown
#colors = ['aliceblue','antiquewhite','aqua','aquamarine','azure','beige','bisque','blanchedalmond','blue','blueviolet','brick','brown', 'burlywood', 'burntsienna', 'burntumber', 'cadetblue', 'cadmiumorange', 'cadmiumyellow' ]
#window2.bgcolor('black')


#for i in range(1234):
    #pen.pencolor(colors[i%19])
    #pen.width(i/100 + 1)
    #pen.forward(i)
    #pen.left(60)



window2 = turtle.Screen()
pen = turtle.Pen()
pen.penup()
pen.goto(-220, 50)
pen.pendown()

def drawI():
    pen.forward(100)
    pen.backward(50)
    pen.left(90)
    pen.forward(100)
    pen.right(90)
    pen.forward(50)
    pen.left(180)
    pen.forward(100)
    pen.right(180)


    pen.penup()
    pen.goto(-120, 50)
    pen.pendown()
    pen.penup()
    pen.forward(50)
    pen.pendown()
drawI()

def drawO():
    pen.left(90)
    pen.forward(70)
    pen.penup()
    pen.goto(-70, 110)
    pen.pendown()
    for i in range(12):

        pen.forward(10)
        pen.right(180 / 12)
    pen.forward(20)
drawO()



turtle.done()
turtle.exitonclick()