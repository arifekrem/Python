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

#Changing the colors of a Circle in Tkinter

from tkinter import * #Import Tkinter so we can use it to create our panel with buttons and a screen

root = Tk() #Creates the window
root.wm_title('Colored Circles') #Sets the title that will appear in the top left
root.config(background = '#FFFFFF')

def redCircle(): #The function to draw the Red Circle
    circleCanvas.create_oval(20, 20, 80, 80, width=0, fill='red') #Draws an empty circle with Red edges
    colorLog.insert(0.0, 'Red\n') #Fills in the circle with color Red

def yelCircle(): #The function to draw the Yellow Circle
    circleCanvas.create_oval(20, 20, 80, 80, width=0, fill='yellow') #Draws an empty circle with Yellow edges
    colorLog.insert(0.0, 'Yellow\n') #Fills in the circle with color Yellow

def grnCircle(): #The function to draw the Green Circle
    circleCanvas.create_oval(20, 20, 80, 80, width=0, fill='green') #Draws an empty circle with Green edges
    colorLog.insert(0.0, 'Green\n') #Fills in the circle with color Green

#Right Frame and its contents
rightFrame = Frame(root, width=200, height = 600)
rightFrame.grid(row=0, column=1, padx=10, pady=2) #Location of where the frame is located in the Tkinter window

#Screen that shows the circles
circleCanvas = Canvas(rightFrame, width=100, height = 100, bg='white')
circleCanvas.grid(row=0, column=0, padx=10, pady=2) #Location of where the screen is located in the Tkinter window

#Frame where all the buttons are located
btnFrame = Frame(rightFrame, width=200, height = 100)
btnFrame.grid(row=1, column=0, padx=10, pady=2) #Location of where the frame is located in the Tkinter window

#The panel where names of the colors are typed in the bottom as an output
colorLog = Text(rightFrame, width=30, height = 10, takefocus=0)
colorLog.grid(row=2, column=0, padx=10, pady=2) #Location of where the panel is located in the Tkinter window

#The button that activates the redCircle() function
redBtn = Button(btnFrame, text='Red', command=redCircle)
redBtn.grid(row=0, column=0, padx=10, pady=2) #Location of where the button is located in the Tkinter window

#The button that activates the yelCircle() function
yellowBtn = Button(btnFrame, text='Yellow', command=yelCircle)
yellowBtn.grid(row=0, column=1, padx=10, pady=2) #Location of where the button is located in the Tkinter window

#The button that activates the grnCircle() function
greenBtn = Button(btnFrame, text='Green', command=grnCircle)
greenBtn.grid(row=0, column=2, padx=10, pady=2) #Location of where the button is located in the Tkinter window

root.mainloop() #start monitoring and updating the GUI