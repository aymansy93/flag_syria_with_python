#!/usr/bin/python3
from turtle import *

# speed(0)
Screen().bgcolor("#6B929D")
goto(-150,-50)
flag_color= ("green", "white", "black")

for i in range(3):
    color(flag_color[i])
    begin_fill()
    for j in range(4):
        forward(200-50*(j%2)*(i+1))
        left(90)
    end_fill()
up()
goto(-135, 15)
down()

color('red')
left(36)
for i in range(3):
    begin_fill()
    for i in range(5):
        forward(20)
        left(144)
    end_fill()
    right(36)
    up()
    forward(80)
    down()
    left(36)
up()
goto(-135,-90)
down()
color('black')
left(45)
write("by: Ayman kanawi",move=False, align='center', font=('Arial', 20, 'normal'))
hideturtle()
mainloop()

