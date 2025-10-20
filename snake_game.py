
from turtle import Turtle, Screen


x_position=[-20,0,20]

up=90
down=270
left=180
right=0

class Snake:
   
   def __init__(self):
      
      self.all_snake=[]
      
      self.create_snake()
      
      self.head=self.all_snake[0]


   def create_snake(self):
      
      for snake in range(3):
         new_snake=Turtle(shape="square")
         new_snake.color("white")
         new_snake.penup()
         new_snake.goto(x=x_position[snake],y=0)
         self.all_snake.append(new_snake)
         
         
         
   def move(self):
      
      for i in range(len(self.all_snake)-1,0,-1):
         new_x=self.all_snake[i-1].xcor()
         new_y=self.all_snake[i-1].ycor()
         self.all_snake[i].goto(new_x,new_y)
      self.head.forward(15)  
      
      
   def up(self):
      if self.head.heading()!=down:
      
         self.head.setheading(up)
      
   def down(self):
      if self.head.heading()!=up:
         self.head.setheading(down)
      
   def left(self):
      if self.head.heading()!=right:
         self.head.setheading(left)
      
   def right(self):
      if self.head.heading()!=left:
         self.head.setheading(right)
      
      