from turtle import Turtle, Screen
import random
obj_2=Turtle()
obj_2.shape("square")
obj_2.pensize(15)
obj_2.speed("fast")
turtle_colors = [
    "alice blue", "antique white", "aqua", "aquamarine", "azure",
    "beige", "bisque", "blanched almond", "blue violet", "burlywood",
    "cadet blue", "chartreuse", "chocolate", "coral", "cornflower blue",
    "cornsilk", "crimson", "cyan", "dark blue", "dark cyan",
    "dark goldenrod", "dark gray", "dark green", "dark khaki", "dark magenta",
    "dark olive green", "dark orange", "dark orchid", "dark red", "dark salmon",
    "dark sea green", "dark slate blue", "dark slate gray", "dark turquoise", "dark violet",
    "deep pink", "deep sky blue", "dim gray", "dodger blue", "firebrick",
    "floral white", "forest green", "gainsboro", "ghost white", "gold",
    "goldenrod", "gray", "green yellow", "honeydew", "hot pink",
    "indian red", "indigo", "ivory", "khaki", "lavender",
    "lavender blush", "lawn green", "lemon chiffon", "light blue", "light coral",
    "light cyan", "light goldenrod yellow", "light gray", "light green", "light pink",
    "light salmon", "light sea green", "light sky blue", "light slate gray", "light steel blue",
    "light yellow", "lime green", "linen", "magenta", "medium aquamarine",
    "medium blue", "medium orchid", "medium purple", "medium sea green", "medium slate blue",
    "medium spring green", "medium turquoise", "medium violet red", "midnight blue", "mint cream",
    "misty rose", "moccasin", "navajo white", "navy", "old lace",
    "olive drab", "orange red", "orchid", "pale goldenrod", "pale green",
    "pale turquoise", "pale violet red", "papaya whip", "peach puff", "peru",
    "pink", "plum", "powder blue", "rosy brown", "royal blue",
    "saddle brown", "salmon", "sandy brown", "sea green", "seashell",
    "sienna", "sky blue", "slate blue", "slate gray", "snow",
    "spring green", "steel blue", "tan", "thistle", "tomato",
    "turquoise", "violet", "wheat", "white smoke", "yellow green"
]
direction=[0,90,180,270]


   
angle=random.choice(direction)
for _ in range(200):
   obj_2.color(random.choice(turtle_colors))
   obj_2.forward(15)
   obj_2.setheading(angle)
     




screen=Screen()
screen.exitonclick()