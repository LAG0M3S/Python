import turtle

t=turtle.Turtle("turtle")
ecra=turtle.getscreen()
t.penup()
t.goto(0,0)
t.pendown()
t.begin_fill()
t.color("black", "red")
for i in range(2):
    t.forward(250)
    t.left(90)
    t.forward(150)
    t.left(90)
t.end_fill()
t.penup()
t.goto(80,85)
t.pendown()
t.begin_fill()
t.color("green", "green")
for i in range(0, 5):
    t.fd(100)
    t.right(144)
t.end_fill()
#Ignorar estes passos
t.penup()
t.forward(1000)
t.pendown()
ecra.mainloop()