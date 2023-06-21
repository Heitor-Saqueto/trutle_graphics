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

def pick_color():
    colors = ["red", "blue", "yellow", "green", "purple", "white",  "orange", "darkgreen", "magenta4", "black", "gray", "pink", "lightblue", "darkred"]
    random.shuffle(colors)
    return colors[0]

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
    teddy.color(pick_color())
    teddy.pensize(20)
    teddy.speed(0)
    teddy.forward(20)


for _ in range(100):
    num = random.choice(degree)
    random_move_f(num)




screen = Screen()
screen.exitonclick()
