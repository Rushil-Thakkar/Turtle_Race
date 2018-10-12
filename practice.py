from turtle import *
from random import randint
from tkinter import messagebox

speed(10)
penup()
goto(-140, 140)

for step in range(15):
    write(step)
    right(90)
    forward(10)
    pendown()
    for step1 in range(15):
        forward(10)
        penup()
        forward(5)
        pendown()

    penup()
    backward(235)
    left(90)
    forward(20)

t1 = Turtle()
t1.color('red')
t1.shape('turtle')
t1.penup()
t1.goto(-160, 100)
t1.pendown()

t2 = Turtle()
t2.color('blue')
t2.shape('turtle')
t2.penup()
t2.goto(-160, 60)
t2.pendown()

t3 = Turtle()
t3.color('green')
t3.shape('turtle')
t3.penup()
t3.goto(-160, 20)
t3.pendown()

t4 = Turtle()
t4.color('black')
t4.shape('turtle')
t4.penup()
t4.goto(-160, -20)
t4.pendown()

for turn in range(100):
    t1.forward(randint(1, 5))
    t2.forward(randint(1, 5))
    t3.forward(randint(1, 5))
    t4.forward(randint(1, 5))

x1 = t1.xcor()
x2 = t2.xcor()
x3 = t3.xcor()
x4 = t4.xcor()


if x1>x2 and x1>x3 and x1>x4 :
    messagebox.showinfo("RESULT OF THE MATCH ", " RED TURTLE WINS")

if x2>x1 and x2>x3 and x2>x4 :
    messagebox.showinfo("RESULT OF THE MATCH ", " BLUE TURTLE WINS")

if x3>x1 and x3>x2 and x3>x4 :
    messagebox.showinfo("RESULT OF THE MATCH ", " GREEN TURTLE WINS")

if x4>x1 and x4>x2 and x4>x3 :
    messagebox.showinfo("RESULT OF THE MATCH ", " BLACK TURTLE WINS")




