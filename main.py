# from colorgram import extract
# ext = extract('image.jpg',30)
# colors = []
# for color in ext:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r,g,b)
#     colors.append(rgb)

from turtle import Turtle, Screen
import random
leo = Turtle()
screen = Screen()
screen.colormode(255)

rgb_colors = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57),
              (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174),
              (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42),
              (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203),
              (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]


leo.hideturtle()
leo.up()
leo.setpos(-250,-250)
leo.speed(0)
def spot_painting(turtle,row,col):
    for i in range(row):
        turtle.setx(-250)
        for j in range(col):
            turtle.down()
            turtle.dot(25,random.choice(rgb_colors))
            turtle.up()
            turtle.setx(leo.xcor() + 50)
        turtle.sety(leo.ycor() + 50)
spot_painting(leo,10,10)


screen.exitonclick()