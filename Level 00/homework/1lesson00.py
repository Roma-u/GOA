from turtle import *
#We wanna build a house
#step 1:draw a square
# 
shape("turtle")
width(6)
speed(4)
color("cyan")
begin_fill()
forward(150)
left(90)
forward(150)
left(90)
forward(150)
left(90)
forward(150)
left(90)
end_fill()
#step 2: a door
forward(60)
color("white")
begin_fill()
left(90)
forward(65)
right(90)
forward(40)
right(90)
forward(65)
end_fill()
#step 3: a floor
penup()
goto(150,150)
pendown()
color("black")
begin_fill()
right(150)
forward(150)
left(120)
forward(150)
end_fill()
#step 4: windows
color("black")
left(120)
forward(30)
right(90)
color("cyan")
forward(30)
color("black")
begin_fill()
left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(25)
end_fill()
penup()
goto(150,150)
pendown()
color("black")
right(90)
forward(50)
color("cyan")
left(90)
forward(30)
color("black")
begin_fill()
left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(25)
end_fill()


exitonclick()
