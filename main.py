import turtle
from random import randint

screen = turtle.Screen()
screen.title("Catch The Turtle")
screen.bgcolor("light blue")
score_turtle = turtle.Turtle()
countdown_turtle = turtle.Turtle()
FONT = ("Terminal", 22, "normal")

game_over = False
grid_size = 10
turtle_list = []
score = 0
def setup_score_turtle():
    score_turtle.speed(0)
    score_turtle.hideturtle()
    score_turtle.penup()
    top_height = screen.window_height() / 2
    y = top_height * 0.75
    score_turtle.setposition(0, y)
    score_turtle.pendown()
    score_turtle.write(arg="Score: 0", move=False, align="center", font=FONT)

def make_turtle(x, y):
    t = turtle.Turtle()

    def handle_click(x, y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg="Score: {}".format(score), move=False, align="center", font=FONT)
        # print(x, y)

    t.onclick(handle_click)
    t.penup()
    t.speed(0)
    t.shape("turtle")
    t.shapesize(2, 2)
    t.color("green")
    t.setposition(x * grid_size, y * grid_size)
    turtle_list.append(t)

x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [20, 10, 0, -10]


def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

#recursive function
def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        turtle_list[randint(0, 19)].showturtle()
        screen.ontimer(show_turtles_randomly, 500)

def countdown(time):
    global game_over
    countdown_turtle.speed(0)
    countdown_turtle.hideturtle()
    countdown_turtle.penup()
    top_height = screen.window_height() / 2
    y = top_height * 0.90
    countdown_turtle.setposition(0, y)
    countdown_turtle.pendown()
    countdown_turtle.clear()

    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg="Time {}".format(time), move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game over..", move=False, align="center", font=FONT)


turtle.tracer(0)
setup_score_turtle()
setup_turtles()
hide_turtles()
show_turtles_randomly()
countdown(20)
turtle.tracer(1)
# turtle.tracer ile animasyonları göstermeden ekranın istediğimiz hale direkt gelmesini sağladık.
turtle.mainloop()
