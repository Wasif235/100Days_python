import turtle as t

import random
obj_2=t.Turtle()
t.colormode(255)
obj_2.speed("fastest")
def random_color():
   r=random.randint(0,255)
   g=random.randint(0,255)
   b=random.randint(0,255)
   random_color =(r,g,b)
   return random_color
def draw_spr(size_of_gap):
   for _ in range(int(360/size_of_gap)):

      obj_2.color(random_color())
      obj_2.circle(100)
      cur_head=obj_2.heading()
      obj_2.setheading(cur_head+size_of_gap)
      obj_2.circle(100)
draw_spr(6)


screen=t.Screen()
screen.exitonclick()
