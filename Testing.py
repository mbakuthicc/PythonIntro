import turtle
import random


t1=turtle.Turtle()
t1.color("red")
t1.left(90)
t1.write(t1.position())

t2=turtle.Turtle()
t2.color("orange")
t2.penup()
t2.goto(50, 0)
t2.left(90)
t2.pendown()
t2.write(t2.position())

t3=turtle.Turtle()
t3.color("gold")
t3.penup()
t3.goto(-50, 0)
t3.left(90)
t3.pendown()
t3.write(t3.position())

t4=turtle.Turtle()
t4.color("green")
t4.penup()
t4.goto(100, 0)
t4.left(90)
t4.pendown()
t4.write(t4.position())

t5=turtle.Turtle()
t5.color("blue")
t5.penup()
t5.goto(-100, 0)
t5.left(90)
t5.pendown()
t5.write(t5.position())

t6=turtle.Turtle()
t6.color("purple")
t6.penup()
t6.goto(150, 0)
t6.left(90)
t6.pendown()
t6.write(t6.position())

t7=turtle.Turtle()
t7.color("pink")
t7.penup()
t7.goto(-150, 0)
t7.left(90)
t7.pendown()
t7.write(t7.position())

t8=turtle.Turtle()
t8.color("spring green")
t8.penup()
t8.goto(200, 0)
t8.left(90)
t8.pendown()
t8.write(t8.position())

t9=turtle.Turtle()
t9.color("blue violet")
t9.penup()
t9.goto(-200, 0)
t9.left(90)
t9.pendown()
t9.write(t9.position())

turtles=[t1,t2,t3,t4,t5,t6,t7,t8,t9]

for i in range(100):
    t1.forward(random.randint(0, 5))
    t2.forward(random.randint(0, 5))
    t3.forward(random.randint(0, 5))
    t4.forward(random.randint(0, 5))
    t5.forward(random.randint(0, 5))
    t6.forward(random.randint(0, 5))
    t7.forward(random.randint(0, 5))
    t8.forward(random.randint(0, 5))
    t9.forward(random.randint(0, 5))

t1.write(t1.position())
t2.write(t2.position())
t3.write(t3.position())
t4.write(t4.position())
t5.write(t5.position())
t6.write(t6.position())
t7.write(t7.position())
t8.write(t8.position())
t9.write(t9.position())

turtle.exitonclick()
