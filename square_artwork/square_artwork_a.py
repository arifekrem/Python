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

#Drawing letter "A" with any amount of squares by painting some of them

import turtle #Import Turtle so we can draw on the Turtle panel
from math import * #Import Math so we can do complicated calculations easily

array = int(turtle.textinput("Array","How many blocks do you want side by side? (Minimum 4)")) #The number of squares in each rows
a = turtle.Turtle() #The variable that we assign Turtle to
a.speed(0) #Setting the speed of turtle to 0 (which is the fastest speed setting)
a.pu() #Pen Up (not drawing anything)
a.goto(-250,-250) #Teleports the pen of the turtle to the bottom left corner of the screen because we are going to draw towards up-right
a.pd() #Pen Down (starts drawing)
side = int(turtle.textinput("Length","The length of the side of your square\n")) #Length of the smaller squares (Larger ones would be more visible)

if array%2 == 0: #If statement to check if array is even
    def sq(side): #Our function that draws the smaller squares
        for i in range(4): #Draws the edges of the squares
            a.left(90) #Turtle turns left 90 degrees
            a.forward(side) #Turtle moves forward for the lengt of input 'side'
        if b<array/2 and c == 1 or b<array/2 and c == array or b > array/2 and c == b - array/2 or b > array/2 and c ==(array - (b - array/2)) + 1 or b == array/2: #Checks which small squares we are drawing
            a.fillcolor("red") #Color of the fillment of our squares
            a.begin_fill() #Starts filling the squares that we are going to draw
            for i in range(4): #Draws the edges of the squares
                a.left(90) #Turtle turns left 90 degrees
                a.forward(side) #Turtle moves forward for the lengt of input 'side'
            a.end_fill() #Ends filling squares

else: #If array is odd
    def sq(side): #Our function that draws the smaller squares
        for i in range(4): #Draws the edges of the squares
            a.left(90) #Turtle turns left 90 degrees
            a.forward(side) #Turtle moves forward for the lengt of input 'side'
        if b < int(array/2) and c == 1 or b < int(array/2) and c == array or b > int(array/2) and c == int(b - array/2) or b > int(array/2) and c ==(array - int((b - array/2))) + 1 or b == int(array/2) or b == int(array/2) + 1 and c == 1 or b == int(array/2) + 1 and c == array or b == array and c == int(array/2) + 1: #Checks which small squares we are drawing
            a.fillcolor("red") #Color of the fillment of our squares
            a.begin_fill() #Starts filling the squares that we are going to draw
            for i in range(4): #Draws the edges of the squares
                a.left(90) #Turtle turns left 90 degrees
                a.forward(side) #Turtle moves forward for the lengt of input 'side'
            a.end_fill() #Ends filling squares
c = 1 #Number of columns we are on   
b = 1 #Number of rows we are on
for i in range(array): #The loop to repeat drawing each rows
    for i in range(array): #Starts drawing each rows
        a.forward(int(sqrt(side))) #Goes forward to start drawing
        sq(side) #Calls the function that draws mini squares
        c = c + 1 #Increases the count of columns that we are on
        if c != array + 1: #Checks if we are on the last column
            a.forward(side - int(sqrt(side))) #If we aren't on the last column, jumps to the next square
    a.pu() #Pen Up (not drawing anything)
    a.goto(-250,side * b -250) #Goes to the location where first mini-square of the each row should be drawn
    a.pd() #Pen Down (starts drawing)
    b = b + 1 #Increases the count of rows that we are on
    c = 1 #Resets the count of columns to 1 (because we are on the first column)