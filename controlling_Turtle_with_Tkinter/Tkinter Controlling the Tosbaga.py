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

# The Tosbaga game where you controll the turtle with the buttons from tkinter


import tkinter as tk #imports tkinter as tk so you type tk to call tkinter
from turtle import * #imports everything from turtle so you don't need to type turtle before its methods

Jack = Turtle() #The turtle that we will control

color = textinput("Color", "What color will Jack be?\n") #The window to input color of our turtle
try:
    Jack.color(color)
except:
    color = textinput("Color", "What color will Jack be?\n") #The window to input color of our turtle
    Jack.color(color)

shape = textinput("Shape", "What shape will Jack be?") #The window to input shape of our turtle
try:
    Jack.shape(shape)
except:
    shape = textinput("Shape", "What shape will Jack be?") #The window to input shape of our turtle
    Jack.shape(shape)

size = float(textinput("Size","How large will Jack be?\n(1-5 is recommended)\n")) #The window to input size of our turtle
try:
    Jack.shapesize(size)
except:
    size = float(textinput("Size","How large will Jack be?\n(1-5 is recommended)\n")) #The window to input size of our turtle
    Jack.shapesize(size)

class Tosbaga(tk.Frame): #The class that holds all our functions
    def __init__(self,master=None): #This function runs the whole class (Tosbaga)
        super().__init__(master)
        self.master = master
        self.title = master.title("Photo Gallery")
        self.pack()
        self.create_widgets()
        
    def w(self): #The function to move turtle 50 units forward
        Jack.forward(50)
        print("Forward")

    def a(self): #The function to turn left and move 50 units in the direction
        Jack.left(90)
        Jack.forward(50)
        print("Left")

    def s(self): #The function to turn backwards and move 50 units in the direction
        Jack.left(180)
        Jack.forward(50)
        print("Backward")

    def d(self): #The function to turn right and move 50 units in the direction
        Jack.right(90)
        Jack.forward(50)
        print("Right")

    def create_widgets(self): #The that creates buttons
        self.button1 = tk.Button(self) #The button to go forward
        self.button1["text"] = "Forward" #The text on the button
        self.button1["fg"]= "orange" #Color of that text
        self.button1["command"] = self.w #What the button activates
        self.button1.grid(row=2,column=2,sticky="W") #Location of the button on tkinter window

        self.button2 = tk.Button(self) #The button to go left
        self.button2["text"] = "Left"
        self.button2["fg"]= "orange"
        self.button2["command"] = self.a 
        self.button2.grid(row=3,column=1,sticky="E")
    
        self.button3 = tk.Button(self) #The button to go backwards
        self.button3["text"] = "Backward"
        self.button3["fg"]= "orange"
        self.button3["command"] = self.s
        self.button3.grid(row=3,column=2,sticky="W")
        
        self.button4 = tk.Button(self) #The button to go right
        self.button4["text"] = "Right"
        self.button4["fg"]= "orange"
        self.button4["command"] = self.d
        self.button4.grid(row=3,column=3,sticky="W")

        self.button5 = tk.Button(self) #The exit button
        self.button5["text"] = "EXIT"
        self.button5["fg"]= "red"
        self.button5["command"] = self.master.destroy
        self.button5.grid(row=1,column=4,sticky="W")
        
root = tk.Tk(); app = Tosbaga(master=root); app.mainloop()