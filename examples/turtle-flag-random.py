from turtle import *
from random import randint, choice

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

# Instructions to draw and fill a rectangular flag segment
def rect(w, h):
    begin_fill()
    for i in range(2):
        forward(w)
        left(90)
        forward(h)
        left(90)
    end_fill()

# Instructions to move to the next corner position
def move_y(h):
    penup()
    left(90)
    forward(h)
    right(90)
    pendown()

def move_x(w):
    penup()
    forward(w)
    pendown()

# Instructions to set the starting position, to centrally align the flag
def start_pos(w, h):
    penup()
    backward(w/2)
    left(90)
    backward(h/2)
    right(90)
    pendown()

print("Welcome to the Flag Creator!")
print("This program creates rectangular, striped, flags from your choices.")
print()

# Inputting the flag dimensions
print("What is the width of your flag? Please enter a whole number between 50 & 500.")
try:
    width = abs(int(input("Width = ")))
except:
    width = randint(50,500)
    print("A random width has been chosen for you!")
if not 50 <= width <= 500:
    width = randint(50,500)
    print("A random width has been chosen for you!")
print()

print("What is the height of your flag? Please enter a whole number between 50 & 500.")
try:
    height = abs(int(input("Height = ")))
except:
    height = randint(50,500)
    print("A random height has been chosen for you!")
if not 50 <= height <= 500:
    height = randint(50,500)
    print("A random height has been chosen for you!")
print()

# Inputting the number of stripes and their direction
print("How many stripes does your flag have? Please enter a whole number between 1 & 10.")
try:
    stripes = abs(int(input("Stripes = ")))
except:
    stripes = randint(1,10)
    print("A random number of stripes has been chosen for you!")
if stripes == 0:
    stripes = 1
    print("Stripes has been set to the minimum value of 1")
elif not 0 < stripes <= 10:
    stripes = randint(1,10)
    print("A random number of stripes has been chosen for you!")
print()

print("Are the stripes horizontal or vertical? Please type 'H' or 'V'.")
orient = ['H', 'V']
try:
    orientation = str((input("H or V = "))).upper()
except:
    orientation = choice(orient)
    print("A random orientation has been chosen for you!")
if orientation not in orient:
    orientation = choice(orient)
    print("A random orientation has been chosen for you!")
print()

# Calculating the stripe dimentions and inputting their colours
if orientation == "H":
    horizontal = True
    vertical = False
    segment_width = width
    segment_height = height/stripes
    print("Starting from the BOTTOM, what colour is the first stripe?")
elif orientation == "V":
    horizontal = False
    vertical = True
    segment_width = width/stripes
    segment_height = height
    print("Starting from the LEFT, what colour is the first stripe?")

colours = []
for i in range(stripes):
    colour = input("Stripe " + str(i+1) + " = ")
    if colour == 'random' or colour == '':
        print("A random colour has been chosen for you!")
    colours.append(colour)

# Setting the background colour and starting position
bg = 'whitesmoke'
bgcolor(bg)
start_pos(width, height)

# Draw the flag occording to the inputted dimensions & colours
for i in range (len(colours)):
    try:
        if colours[i] == 'random' or colours[i] == '':
            rand = (randint(0,255), randint(0,255), randint(0,255))
            colormode(255)
            color(rand)
            colormode(1)
        else:
            color(colours[i])
    except:
        print("The colour '" + str(colours[i]) + "' is not recognised, and has been skipped.")
        color('black', bg)
    rect(segment_width, segment_height)
    if horizontal == True:
        move_y(segment_height)
    elif vertical == True:
        move_x(segment_width)

# Hide the turtle to show the final flag
hideturtle()
print()
print("Save your flag, then make another one!")
