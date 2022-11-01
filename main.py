import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make Your Bet', prompt='Which Turtle is going to win the race? Enter a color: ')
colors = ['red','orange','yellow', 'green', 'blue','purple']

turtles = []


y_cor = -100
for i in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_cor)
    y_cor += 50
    turtles.append(new_turtle)

new_turtle.speed('fastest')
if user_bet:
    is_race_on = True

while is_race_on:
    for item in turtles:
        if item.xcor() > 230:
            is_race_on = False
            winning_color = item.pencolor()
            if winning_color == user_bet:
                print(f"You've Won! The {winning_color} turtle is the winner")
            else:
                print(f"You've Lost! The {winning_color} turtle is the winner")
        random_dist = random.randint(0, 10)
        item.forward(random_dist)



screen.exitonclick()