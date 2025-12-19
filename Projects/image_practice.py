# Section 1 - Your code
from utils import *
set_background("schoolthing")

s2 = create_sprite("teachercool", -100, 75)
s1 = create_sprite("cool_dog", 100, 50)
s2 = create_sprite("alien", -100, 50)
s2 = create_sprite("puppy", -100, -100)
s2 = create_sprite("Dawg", 100, -100)


message1 = create_sprite("alien",-200,200)
message1.color("purple")
message1.write("teach is teaching",font = ("Arial", 40, "normal"))
message1.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()