from turtle import *


#we want to make house

#spen 1: draw a square
speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end of square

#drawing a door


forward(70)
color("brown")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()
#end draw door


penup()
goto(200,200)
pendown()


color("red")
begin_fill()

right(150)
forward(200)
left(120)
forward(200)
end_fill()
 #draw windows

penup()
goto(15,100)
left(120)
pendown()
color("yellow")
begin_fill()
forward(40)
left(90)
forward(50)
left(90)
forward(40)
left(90)
forward(50)
left(90)
end_fill()

color("black")
forward(40)
left(90)
forward(50)
left(90)
forward(40)
left(90)
forward(50)
left(90)
forward(20)
left(90)
forward(50)
left(180)
forward(25)
right(90)
forward(20)
left(180)
forward(40)

penup()
goto(145,100)
pendown()
color("yellow")
begin_fill()
forward(40)
left(90)
forward(50)
left(90)
forward(40)
left(90)
forward(50)
left(90)
end_fill()

color("black")
forward(40)
left(90)
forward(50)
left(90)
forward(40)
left(90)
forward(50)
left(90)
forward(20)
left(90)
forward(50)
left(180)
forward(25)
right(90)
forward(20)
left(180)
forward(40)
#end draw windows



#draw door hande
penup()
goto(75,50)
pendown()
left(90)
forward(40)
#end draw door handle


#draw grass
penup()
goto(-100,-100)
pendown()
color("lightgreen")
begin_fill()
forward(200)
right(90)
forward(93)
right(90)
forward(107)
left(90)
forward(214)
left(90)
forward(107)
right(90)
forward(100)
right(90)
forward(200)
right(90)
forward(400)
end_fill()
#end draw grass

#start draw tree
penup()
goto(-80,-80)
pendown()
color("brown")
begin_fill()
right(90)
forward(40)
right(90)
forward(20)
right(90)
forward(40)
right(90)
forward(20)
end_fill()
penup()
right(90)
forward(40)
pendown()
begin_fill()
left(90)
color("green")
forward(30)
right(110)
forward(120)
right(140)
forward(120)
right(110)
forward(60)
end_fill()
#end draw tree


penup()
goto(70,-10)
pendown()
color("gray")
begin_fill()
left(90)
forward(30)
left(90)
forward(60)
left(90)
forward(30)
left(90)
forward(60)
end_fill()

exitonclick()
