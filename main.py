from turtle import Turtle, Screen

from snake_game import Snake

import time

from food import Food

from scoreboard import Scoreboard


screen=Screen()

screen.setup(width=600,height=600)

screen.bgcolor("black")

screen.title("Snake Game")

snake=Snake()

food=Food()

score=Scoreboard()
   
game_is_on = True


screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while game_is_on:
   
   time.sleep(0.1)
      
   snake.move()
   
   
   if snake.head.distance(food) < 15:
      
      food.refresh()
      
      score.scores()
      
      print("nom nom nom")
      

screen.exitonclick()