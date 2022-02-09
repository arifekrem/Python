import turtle
'''

'''


Jack = turtle.Turtle()  #Name of our turtle

def w():  #What will happen when we press w
    Jack.forward(50)
    print('Forward')

def a():  #What will happen when we press a
    Jack.left(90)
    Jack.forward(50)
    print('Left')

def s():  #What will happen when we press s
    Jack.left(180)
    Jack.forward(50)
    print('Backward')

def d():  #What will happen when we press d
    Jack.right(90)
    Jack.forward(50)
    print('Right')

color = input('What color will Jack be?\n')
Jack.color(color)

shape = input('What shape will Jack be?\n')
Jack.shape(shape)

size = float(input('How large will Jack be?\n(1-5 is recommended)\n'))
Jack.shapesize(size)


while True:
    move = input('Move baby move\nMove by typing w/a/s/d\nIf you wanna leave type exit\n\n')
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