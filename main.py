import turtle
from turtle import Turtle, Screen
import random
# here is where we import the Turtle and the screen from the lib turtle...
teddy = Turtle()
# we are going to call it teddy ...
# https://docs.python.org/3/library/turtle.html
# above you can check the turtle library to see what you can do with it.
# I truly recommend You to do that!!!
# GUI is the same of Graphical User Interface
teddy.shape("classic")
# This block of code will draw a dash line.
# for _ in range(50):
#   teddy.forward(5)
#   teddy.penup()
#   teddy.forward(5)
#   teddy.pendown()
# the calcul to know the angle is 360° / number of lines... triangle 360/3 = 120 <-
#------CHALLENGE TO  DRAW SOME FORMS AS TRIANGLE ETC WITH DIFERENT COLORS-----------

##------------BETTER WAY TO DO IT---------------------------------------------

turtle.colormode(255)

#def random_color generate a random number and returns a tuple o rgb

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         teddy.forward(100)
#         teddy.left(angle)


# for shape_side_n in range(3, 11):
#     teddy.color(pick_color())
#     draw_shape(shape_side_n)
##----------------------------------------------------------------------------

##----------------A WAY TO DO IT----------------------------------------------
# this block of code will draw a triangle
# teddy.color(pick_color())
# for _ in range(3):
#     teddy.right(120)
#     teddy.forward(100)
# teddy.color(pick_color())
# this block will draw a square
# for _ in range(4):
#     teddy.right(90)
#     teddy.forward(100)
# teddy.color(pick_color())
# this block will draw a pentagon
# for _ in range(5):
#     teddy.right(72)
#     teddy.forward(100)
# teddy.color(pick_color())
# this block will draw a hexagon
# for _ in range(6):
#     teddy.right(60)
#     teddy.forward(100)
# teddy.color(pick_color())
# this block will draw octagon
# for _ in range(8):
#     teddy.right(45)
#     teddy.forward(100)
# teddy.color(pick_color())
# this block will draw a nonagon
# for _ in range(9):
#     teddy.right(40)
#     teddy.forward(100)
# teddy.color(pick_color())
# this block will draw a decagon
# for _ in range(10):
#     teddy.right(36)
#     teddy.forward(100)
# teddy.color(pick_color())
##--------------------------------------------------------------
##------CHALLENGE DRAW A RANDOM WALK WITH COLORS
degree = [0, 90, 180, 270]

def random_move_f(random_n):
    teddy.setheading(random_n)
    teddy.color(random_color())
    teddy.pensize(20)
    teddy.speed('fastest')
    teddy.forward(50)

for _ in range(500):
    num = random.choice(degree)
    random_move_f(num)

screen = Screen()
screen.exitonclick()
