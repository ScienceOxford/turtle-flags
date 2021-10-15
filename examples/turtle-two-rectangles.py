from turtle import *
bgcolor('whitesmoke')

color('blue', 'pink')
height = 100
width = 200

begin_fill()
for i in range(2):
    forward(width)
    left(90)
    forward(height)
    left(90)
end_fill()

penup()
left(90)
forward(height)
right(90)
pendown()

color('green', 'yellow')
begin_fill()
for i in range(2):
    forward(width)
    left(90)
    forward(height)
    left(90)
end_fill()
