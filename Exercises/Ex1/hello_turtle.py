#################################################################
# FILE : hello_turtle.py
# WRITER : Linor Cohen , linorcohen , 318861226
# EXERCISE : intro2cse ex1 2021
# DESCRIPTION: A simple program that to draws three flowers using turtle module
# STUDENTS I DISCUSSED THE EXERCISE WITH: NONE
# WEB PAGES I USED: NONE
# NOTES: NONE
#################################################################
import turtle


def draw_petal():
    """
    This function draws a single petal.
    """
    # the next lines draw a petal
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)


def draw_flower():
    """
    This function draws a single flower.
    """
    # the next lines turns the turtle head four times and draws a petal
    # in each time
    turtle.left(45)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(135)
    turtle.forward(150)


def draw_flower_and_advance():
    """
    This function draws a single flower and  and moves the head of
    the turtle to different spot.
    """
    draw_flower()

    # the next lines move the turtles head to a different spot
    turtle.right(90)
    turtle.up()
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.down()


def draw_flower_bed():
    """
    This function draws three flower.
    """
    # the next lines place the turtle head on the canvas
    turtle.up()
    turtle.forward(200)
    turtle.left(180)
    turtle.down()
    # the next functions that are called draws the three flowers
    # one next to the other
    draw_flower_and_advance()
    draw_flower_and_advance()
    draw_flower_and_advance()


if __name__ == "__main__":
    draw_flower_bed()
    turtle.done()
