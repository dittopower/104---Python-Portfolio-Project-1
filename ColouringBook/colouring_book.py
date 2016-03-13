
#-----Statement of Authorship----------------------------------------#
#
#  By submitting this task the signatories below agree that it
#  represents our own work and that we both contributed to it.  We
#  are aware of the University rule that a student must not
#  act in a manner which constitutes academic dishonesty as stated
#  and explained in QUT's Manual of Policies and Procedures,
#  Section C/5.3 "Academic Integrity" and Section E/2.1 "Student
#  Code of Conduct".
#
#  First student's no:  n8888141
#  First student's name:  James Clelland
#  Portfolio contribution: 90%
#
#  Second student's no: n8857954
#  Second student's name: Damon Jones
#  Portfolio contribution: 10%
#
#  Contribution percentages refer to the whole portfolio, not just this
#  task.  Percentage contributions should sum to 100%.  A 50/50 split is
#  NOT necessarily expected.  The percentages will not affect your marks
#  except in EXTREME cases.
#
#--------------------------------------------------------------------#


#-----Task Description-----------------------------------------------#
#
#  COLOURING BOOK
#
#  In this task you create a children's colouring game in which
#  given pictures can be coloured by tracing around a shape and
#  then filling it. The controls are as follows.
#
#  ARROW KEYS - Move the "brush" (turtle cursor) left, right, up
#               or down by a fixed small amount.
#
#  'z' - Undo the last step.
#
#  'r', 'g', 'b' - Change the brush colour to red, green or blue,
#                  respectively.  (You can define more colours if
#                  you like, but we expect at least these three.)
#
#  SPACE BAR - Toggle the painting mode.  In "move" mode, which is
#              the initial mode, the "brush" (turtle) moves around
#              the screen without drawing.  In "paint" mode the
#              brush leaves a coloured line as it moves.  Most
#              importantly, when the mode is changed from "paint"
#              to "move", the area traced out by the brush is
#              filled with colour.
#
#--------------------------------------------------------------------#


#-----Students' Solution---------------------------------------------#
#
#  Complete the task by filling in the template below.




from turtle import *
bgpic("Colour_A_Plane.gif") # change this to change the picture

# PUT YOUR CODE HERE
######### Controls  ############

def move (direction):
    setheading(direction)
    forward (10)
    
def up ():
    move(90)
    
def left ():
    move(180)
    
def right ():
    move(0)
    
def down():
    move(270)
    
###### End of controls #######

###### Undo Function #######
    
def zundo ():                       #Function was created to allow the undo
    for _ in range (1):             #Function can be changed to undo more at once
        undo()
        


#### Drawing Mode #####
def movemode ():
    penup()
    
def paintmode ():
    if not isdown():
        begin_fill()
        pendown()
    else:
        end_fill()
        penup()

   
    
####### Colours ##############    
def red ():
    color ('red')
    
def green ():
    color ('green')

def blue ():
    color ('blue')
        
## Set up ##

title('Colouring Book')
penup()
color('green')
goto(0,0)

## Controls ##
onkey (up,'Up')
onkey (left,'Left')
onkey (right,'Right')
onkey (down,'Down')

## Colours ##
onkey (red, 'r')
onkey (green, 'g')
onkey (blue, 'b')


## Draw mode  & Undo Mode
onkey (paintmode, 'space')
onkey (zundo, 'z')

listen()
done()

#--------------------------------------------------------------------#
