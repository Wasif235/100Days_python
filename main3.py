import turtle
import random
obj_2=turtle.Turtle()
turtle.colormode(255)

def random_color():
   r=random.randint(0,255)
   g=random.randint(0,255)
   b=random.randint(0,255)
   random_color =(r,g,b)
   return random_color
direction=[0,90,180,270]
obj_2.pensize(15)
obj_2.speed("fast")
angle=random.choice(direction)
for _ in range(200):
   obj_2.color(random_color())
   obj_2.forward(1)
   obj_2.setheading(angle)
     




screen=Screen()
screen.exitonclick()