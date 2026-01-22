import turtle, time, random
from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 = -200
y1 = 200
x2 = -200
y2 = 100
x3 = -201
y3 = -100
x4 = -200
y4 = -200


# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("skislope")
t1 = create_sprite("ski4",x1,y1)
t2 = create_sprite("ski3",x2,y2)
t3 = create_sprite("ski2",x3,y3)
t4 = create_sprite("ski1",x4,y4)


# # Section 3 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # TODO - explain here which sprites are faster or slower
for i in range(30):
     x1 += random.randint(10,25)
     x2 += random.randint(10,25)
     x3 += random.randint(10,25)
     x4 += random.randint(10,25)

     t1.goto(x1, y1)
     t2.goto(x2, y2)
     t3.goto(x3, y3)
     t4.goto(x4, y4)

     window.update()
     time.sleep(0.1)


# # Section 4 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
if x1 >= x2 and x1 >= x3 and x1 >= x4:
     print("player 1 wins!")
elif x1 <= x2 and x2 >= x3 and x2 >= x4 :
     print("player 2 wins!")
elif x1 <= x3 and x3 >=x2 and x3 >= x4 :
     print("player 3 wins!")
elif x1 <= x4 and x4 >=x2 and x4 >= x3 :
     print("player 4 wins!")


turtle.exitonclick()