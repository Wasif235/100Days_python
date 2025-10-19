from turtle import Turtle, Screen

obj=Turtle()

def move_down():
   obj.backward(100)

def move_left():
   obj.left(10)
def move_right():
   obj.right(10)
def move_up():
   obj.forward(100) 
def clear():
       obj.clear()
       obj.penup()
       obj.home()
       obj.pendown()

       
   
screen=Screen()
screen.listen()
screen.onkey(key="w", fun=move_up)
screen.onkey(key="s", fun=move_down)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
print(obj)