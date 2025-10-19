from turtle import Turtle, Screen
import random


screen=Screen()

screen.setup(width=500,height=400 )

user_bet= screen.textinput(title="make you bet", prompt="which turtle will wint the race? Enter a color: ")

print(user_bet)

colors=["red","orange","yellow","green","blue"]

y_postion=[180,100,0,-100,-180]

all_turtle=[]

for turtle_index in range(5):
   new_turtle= Turtle(shape="turtle")
   new_turtle.penup()
   new_turtle.color(colors[turtle_index])
   new_turtle.goto(x=-230, y=y_postion[turtle_index])
   all_turtle.append(new_turtle)
   
is_race_one=False

if user_bet:
   
   is_race_one=True

while is_race_one:
   
   for turtle in all_turtle:
         
         if turtle.xcor()> 230:
            
            is_race_one=False
         
            winning_color = turtle.pencolor()
         
            if winning_color==user_bet:
            
               print(f"You've won! The {winning_color} turtle is the winner!")
         
            else:
               print(f"You've lost! The {winning_color} turtle is the winner!")
         rand_distance = random.randint(0, 10)
         turtle.forward(rand_distance)      
   
screen.exitonclick()
