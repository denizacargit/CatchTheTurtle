import turtle

turtle_instance = turtle.Turtle()
turtle_instance.hideturtle()
turtle_instance.fillcolor("#0B6623")
def turtle_painter():
    turtle_instance.speed(0)
    turtle_instance.begin_fill()
    turtle_instance.color("#0B6623")
    turtle_instance.penup()
    turtle_instance.goto(0,-20)
    turtle_instance.pendown()
    turtle_instance.circle(20)
    turtle_instance.end_fill()
    turtle_instance.penup()
    turtle_instance.goto(28,-5)
    turtle_instance.pendown()
    turtle_instance.begin_fill()
    turtle_instance.circle(8)
    turtle_instance.end_fill()
    turtle_instance.penup()
    turtle_instance.goto(-14, -14)
    turtle_instance.pendown()
    turtle_instance.right(135)
    turtle_instance.forward(8)
    turtle_instance.penup()
    turtle_instance.goto(14, -14)
    turtle_instance.pendown()
    turtle_instance.left(90)
    turtle_instance.forward(8)
    turtle_instance.penup()
    turtle_instance.goto(14,14)
    turtle_instance.pendown()
    turtle_instance.left(90)
    turtle_instance.forward(8)
    turtle_instance.penup()
    turtle_instance.goto(-14,14)
    turtle_instance.pendown()
    turtle_instance.left(90)
    turtle_instance.forward(8)
