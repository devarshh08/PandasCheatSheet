from turtle import Turtle, Screen
import random

is_race_on = False
all_turtles = []

screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bet: ", prompt = "Which turtle will win the race? Enter a colour from red, green, yellow, blue, purple or black: ")
print(user_bet)

colors = ['red', 'green', 'yellow', 'blue', 'purple', 'black']
y = -140
for i in range(6):
    tim = Turtle(shape = "turtle")
    tim.color(colors[i])
    tim.pu()
    x = -200
    y+=40
    tim.goto(x,y)
    tim.pd()
    all_turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 200:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} is the winner!")
            else:
                print(f"You've lost:( The {winning_color} is the winner!")

    speed = random.randint(0,10)
    turtlee = random.choice(all_turtles)
    turtlee.pu()
    turtlee.forward(speed)