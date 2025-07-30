import turtle
import time
from datetime import datetime

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Beautiful Analog Clock")
screen.tracer(0)

face_drawer = turtle.Turtle()
face_drawer.hideturtle()
face_drawer.speed(0)
face_drawer.pensize(3)

def draw_clock_face(drawer):
    drawer.clear()
    drawer.penup()
    drawer.goto(0, -210)
    drawer.pendown()
    drawer.color("white")
    drawer.circle(210)

    drawer.penup()
    drawer.goto(0, 0)
    drawer.pencolor("white")
    drawer.setheading(90)
    for _ in range(12):
        drawer.forward(180)
        drawer.pendown()
        drawer.pensize(5)
        drawer.forward(30)
        drawer.penup()
        drawer.goto(0, 0)
        drawer.right(30)

    drawer.penup()
    drawer.goto(0, 0)
    drawer.pencolor("gray")
    drawer.setheading(90)
    for _ in range(60):
        drawer.forward(195)
        drawer.pendown()
        drawer.pensize(2)
        drawer.forward(15)
        drawer.penup()
        drawer.goto(0, 0)
        drawer.right(6)

    drawer.penup()
    drawer.pencolor("white")
    drawer.goto(0, 0)

    drawer.setheading(90)
    drawer.forward(160)
    drawer.write("12", align="center", 
                 font=("Arial", 18, "bold"))
    drawer.goto(0, 0)
    drawer.right(30)

    for hour in range(1, 12):
        drawer.forward(160)
        if hour == 11:
            drawer.setx(drawer.xcor() - 4)  
        drawer.write(str(hour),
        align="center", font=("Arial", 18, "bold"))
        drawer.goto(0, 0)
        drawer.right(30)

    drawer.penup()
    drawer.goto(0, 0)
    drawer.dot(15, "white")

second_hand = turtle.Turtle()
second_hand.shape("arrow")
second_hand.color("red")
second_hand.shapesize(stretch_wid=0.5, stretch_len=18)
second_hand.penup()
second_hand.goto(0, 0)
second_hand.speed(0)

minute_hand = turtle.Turtle()
minute_hand.shape("arrow")
minute_hand.color("skyblue")
minute_hand.shapesize(stretch_wid=0.7, stretch_len=14)
minute_hand.penup()
minute_hand.goto(0, 0)
minute_hand.speed(0)

hour_hand = turtle.Turtle()
hour_hand.shape("arrow")
hour_hand.color("lime")
hour_hand.shapesize(stretch_wid=0.9, stretch_len=10)
hour_hand.penup()
hour_hand.goto(0, 0)
hour_hand.speed(0)

def update_clock():
    now = datetime.now()
    sec = now.second
    min = now.minute
    hr = now.hour % 12

    sec_angle = 90 - (sec * 6)
    min_angle = 90 - (min * 6 + sec * 0.1)
    hr_angle = 90 - (hr * 30 + min * 0.5)

    second_hand.setheading(sec_angle)
    minute_hand.setheading(min_angle)
    hour_hand.setheading(hr_angle)

    screen.update()
    screen.ontimer(update_clock, 1000)

draw_clock_face(face_drawer)
update_clock()

turtle.done()
