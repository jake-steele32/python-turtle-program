import turtle
import random
ting = input("turtle , arrow, circle, classic. choose your shape")
ting2 = float (input ("choose pensize: from 10-20"))
ting3 = float (input ("choose speed: from 10-10000"))
ting4 = str (input ("choose ONE colour for the outside"))
ting5 = str (input ("choose ONE colour for the outer outer middle"))
ting6 = str (input ("choose ONE colour for the outer middle"))
ting7 = str (input ("choose ONE colour for the middle middle"))
ting8 = str (input ("choose ONE colour for the inner middle"))
ting9 = str (input ("choose ONE colour for the inner inner middle"))
ting10 = str (input ("choose ONE colour for the inside"))
ting11 = str (input ("choose ONE colour for the very inside"))

bob = turtle.Turtle()


bob.shape(ting)

bob.pensize(ting2)

bob.speed(ting3)

colours = [ting4, ting4]

for num_shapes in range (0,100):
    for side in range(0,6):
        bob.forward(175)
        bob.right(60)

        if side == 5:
            bob.color(colours [random.randint(0,1)])

        else:
            bob.color(colours [random.randint(0,0)])


    bob.right(5)




colours = [ting5, ting5]

for num_shapes in range (0,100):
    for side in range(0,6):
        bob.forward(150)
        bob.right(60)

        if side == 5:
            bob.color(colours [random.randint(0,1)])

        else:
            bob.color(colours [random.randint(0,0)])


    bob.right(5)


colours = [ting6, ting6]

for num_shapes in range (0,100):
    for side in range(0,6):
        bob.forward(125)
        bob.right(60)

        if side == 5:
            bob.color(colours [random.randint(0,1)])

        else:
            bob.color(colours [random.randint(0,0)])


    bob.right(5)

colours = [ting7, ting7]

for num_shapes in range (0,100):
    for side in range(0,6):
        bob.forward(100)
        bob.right(60)

        if side == 5:
            bob.color(colours [random.randint(0,1)])

        else:
            bob.color(colours [random.randint(0,0)])


    bob.right(5)
    
colours = [ting8, ting8]

for num_shapes in range (0,100):
    for side in range(0,6):
        bob.forward(75)
        bob.right(60)

        if side == 5:
            bob.color(colours [random.randint(0,1)])

        else:
            bob.color(colours [random.randint(0,0)])


    bob.right(5)

colours = [ting9, ting9]

for num_shapes in range (0,100):
    for side in range(0,6):
        bob.forward(50)
        bob.right(60)

        if side == 5:
            bob.color(colours [random.randint(0,1)])

        else:
            bob.color(colours [random.randint(0,0)])


    bob.right(5)

colours = [ting10, ting10]

for num_shapes in range (0,100):
    for side in range(0,6):
        bob.forward(25)
        bob.right(60)

        if side == 5:
            bob.color(colours [random.randint(0,1)])

        else:
            bob.color(colours [random.randint(0,0)])


    bob.right(5)

colours = [ting11, ting11]

for num_shapes in range (0,100):
    for side in range(0,6):
        bob.forward(5)
        bob.right(60)

        if side == 5:
            bob.color(colours [random.randint(0,1)])

        else:
            bob.color(colours [random.randint(0,0)])


    bob.right(5)
