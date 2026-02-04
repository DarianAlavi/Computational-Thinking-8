import turtle, time, random
from utils import *

# Section 1 - setup
set_background("moutianbikepark")

sawyers = 0

bicycle = 0
# TODO - set a background using set_background()

# TODO - create at least two variables and set their starting value. ex: cookies = 0


# OPTIONAL: use this invisible alien to say a message
message_sprite = create_sprite("cat", -300,270)
message_sprite.hideturtle()

sawyerlist = []

# Section 2 - controls
def Make_sawyer():
    global sawyers, sawyerlist
    sawyers += 1
    x = random.randint(-300,300)
    y = random.randint(-250,250)
    s1 = create_sprite("sawyerlockedin", x, y)
    sawyerlist.append(s1)

window.onkeypress(Make_sawyer, "space")


def buy_motorcycle():
    global bicycle, sawyers, sawyerlist
    if sawyers > 30:
        bicycle += 1
        sawyers -= 30
        for i in range (30):
            s1 = sawyerlist.pop()
            s1.hideturtle()
   
        x = random.randint(-350,300)
        y = random.randint(-350,250)
        create_sprite("coolbike", x, y)

window.onkeypress(buy_motorcycle, "b")


# TODO - define an action. ex: def my_control()

# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")

# TODO - make a second control





# Section 3 - game loop
window.listen()
for i in range(100000000000000):
    
    if i % 100 == 0:
        for x in range(bicycle):
            sawyers += 1
            x = random.randint(-300,300)
            y = random.randint(-250,250)
            s1 = create_sprite("sawyerlockedin", x, y)
            sawyerlist.append(s1)
            

    # TODO - put any automatic actions here


    # OPTIONAL - use the message sprite to say a message
    message_sprite.clear()
    message_sprite.write(f"sawyer amount = {sawyers} bicycle amount = {bicycle}")

    time.sleep(0.01)
    window.update()