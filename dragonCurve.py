import turtle
import colorsys
import math

# Change how many iterations of dupicating and rotating
iterCount = 12

# Length of line in pixels
lineLen = 5

# This is the list that has all of the directions in order
steps = ['r']

# This for loop creates the list of directions
for i in range(iterCount):
    listLength = len(steps)

    for j in range(listLength-1, -1, -1):
        if (steps[j] == 'r'):
            steps.append('u')
        elif (steps[j] == 'u'):
            steps.append('l')
        elif (steps[j] == 'l'):
            steps.append('d')
        else:
            steps.append('r')

turtle.hideturtle()
turtle.speed("fastest")
for i in range(len(steps)):
    turtle.setheading(90)

    hexColor = colorsys.hsv_to_rgb(i / len(steps), 1.0, 1.0)

    turtle.color(hexColor)

    # Orients the "turtle" according to the corresponding direction in the list
    if (steps[i] == 'r'):
        turtle.right(90)
    elif (steps[i] == 'l'):
        turtle.left(90)
    elif (steps[i] == 'd'):
        turtle.left(180)

    turtle.forward(lineLen)
