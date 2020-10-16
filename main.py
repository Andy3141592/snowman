import turtle as turtle
turtle.color("gray")
turtle.penup()
turtle.goto(130,150)
turtle.pendown()
turtle.right(90)
def cloud():
  for i in range(6):
    turtle.circle(12.5,180)
    turtle.right(120)
turtle.begin_fill()
cloud()
turtle.end_fill()
turtle.penup()
turtle.goto(75,180)
turtle.pendown()
turtle.right(180)
turtle.begin_fill()
cloud()
turtle.end_fill()
turtle.penup()
turtle.goto(0,200)
turtle.pendown()
turtle.begin_fill()
cloud()
turtle.end_fill()
turtle.penup()
turtle.goto(-75,190)
turtle.pendown()
turtle.begin_fill()
cloud()
turtle.end_fill()
turtle.penup()
turtle.goto(-150,210)
turtle.pendown()
turtle.begin_fill()
cloud()
turtle.end_fill()





def snow():
  turtle.begin_fill()
  turtle.circle(2)
  turtle.end_fill()
  turtle.penup()
  turtle.forward(20)
  turtle.pendown()
def row_of_snow():
  for i in range(18):
    snow()
y = 130
turtle.right(90)
while y > 70:      
  
  turtle.penup()
  turtle.goto(-190,y)
  turtle.pendown()
  row_of_snow()
  turtle.penup()
  turtle.goto(-180,y -10)
  turtle.pendown()
  row_of_snow()
  y = y - 20