'''
------------------------------------------------------------
-------------A-------------EEEEEEEEEE-----YYY-------YYY-----
------------AAA------------EEE-------------YYY-----YYY------
-----------AAAAA-----------EEE--------------YYY---YYY-------
----------AAA-AAA----------EEE---------------YYY-YYY--------
---------AAA---AAA---------EEEEEEEEEE---------YYYYY---------
--------AAA-----AAA--------EEE-----------------YYY----------
-------AAAAAAAAAAAAA-------EEE-----------------YYY----------
------AAA---------AAA------EEE-----------------YYY----------
-----AAA-----------AAA-----EEEEEEEEEE----------YYY----------
------------------------------------------------------------
'''

#The Tosbaga game where you controll the turtle with inputs of WASD movement keys.

import turtle

Jack = turtle.Turtle()  #Name of our turtle

def w():  #The function to move turtle 50 units forward
    Jack.forward(50)
    print('Forward')

def a():  #The function to turn left and move 50 units in the direction
    Jack.left(90)
    Jack.forward(50)
    print('Left')

def s():  #The function to turn backwards and move 50 units in the direction
    Jack.left(180)
    Jack.forward(50)
    print('Backward')

def d():  #The function to turn right and move 50 units in the direction
    Jack.right(90)
    Jack.forward(50)
    print('Right')

color = input('What color will Jack be?\n') #The variable to input color of our turtle
Jack.color(color) #

shape = input('What shape will Jack be?\n') #The variable to input shape of our turtle
Jack.shape(shape) 

size = float(input('How large will Jack be?\n(1-5 is recommended)\n')) #The variable to input size of our turtle
Jack.shapesize(size)


while True: #Our while loop to keep the game rolling until we type exit
    move = input('Move baby move\nMove by typing w/a/s/d\nIf you wanna leave type exit\n\n') #The variable to input movement of our turtle
    if move == 'w':
        w()
    elif move == 'a':
        a()
    elif move == 's':
        s()
    elif move == 'd':
        d()
    elif move == 'exit':
        exit()