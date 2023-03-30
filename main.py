Turtle Party Project
By Hans Bisong
03/30/2023

import turtle

turtle.color("red")

size = 100

#Repeat 3 times

def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()




def square(side):
  

  for i in range(4):
    
    turtle.forward(size)
    turtle.left(90)
    
square(100)
back(125)

back(50)
