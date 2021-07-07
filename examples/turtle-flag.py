from turtle import *

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

# Inputting the flag dimensions
print("What is the width of your flag? Please enter a whole number.")
try:
    width = int(input("Width = "))
except:
    print("Please enter a whole number.")
    width = int(input("Width = "))
print()

print("What is the height of your flag? Please enter a whole number.")
try:
    height = int(input("Height = "))
except:
    print("Please enter a whole number.")
    height = int(input("Height = "))
print()

# Inputting the number of stripes and their direction
print("How many stripes does your flag have? Please enter a whole number.")
try:
    stripes = int(input("Stripes = "))
except:
    print("Please enter a whole number.")
    stripes = int(input("Stripes = "))
if stripes == 0:
    stripes = 1
print()

print("Are the stripes horizontal or vertical? Please type 'H' or 'V'.")
try:
    orientation = (input("H or V = ")).upper()
except:
    print("Please enter 'H' or 'V'.")
    orientation = (input("H or V = ")).upper()
print()

# Calculating the stripe dimentions and inputting their colours
if orientation == "H":
    horizontal = True
    vertical = False
    segment_width = width
    segment_height = height/stripes
    print("Starting from the BOTTOM, what colour is the first stripe?")
else:
    horizontal = False
    vertical = True
    segment_width = width/stripes
    segment_height = height
    print("Starting from the LEFT, what colour is the first stripe?")

colours = []
for i in range(stripes):
    colour = input("Stripe " + str(i+1) + " = ")
    colours.append(colour)

# Setting the background colour and starting position
bg = 'whitesmoke'
bgcolor(bg)
start_pos(width, height)

# Draw the flag occording to the inputted dimensions & colours
for i in range (len(colours)):
    try:
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
print("Save your flag, then click 'Run' to make another one!")
