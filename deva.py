import turtle

s = turtle.Screen()
t = turtle.Turtle()
s.title("My First Turtle Program")

t.pensize(5)
c = ['red','blue','green','yellow']

for i in range(180):
    t.pencolor(c[i%4])
    t.forward(100)
    t.right(30)
    t.forward(20)
    t.left(60)
    t.forward(30)
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.right(30)
    t.right(2)

turtle.mainloop()









