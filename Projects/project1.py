import sys
import time

def tuffthingyosammuzzyiscool(text, delay=0.05):

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
        
name = input("What is your name? ")
input()
tuffthingyosammuzzyiscool(f"cool name {name} im a computer.")
animal = input(" Whats your favorite animal? [Just the name] ")
if animal == "dog":
    tuffthingyosammuzzyiscool("My creator has a dog it super cool. ")
else:tuffthingyosammuzzyiscool(f"{animal}'s are cool! ")
schoolfav = input("Whats your favorite school subject? ")
tuffthingyosammuzzyiscool(f"{schoolfav} is pretty cool. ")
age = input("How old are you? ")
tuffthingyosammuzzyiscool(f"dang {age} is unc. ")
sport = input("What sports do you play? ")
tuffthingyosammuzzyiscool(f"{sport} is a cool sport. ")
colorlike = input("Whats your favorite color? ")
tuffthingyosammuzzyiscool(f"{colorlike} is a cool color! ")
tuffthingyosammuzzyiscool(" Hmmmmmmmmmmmmmm should I ask more questions??? ")
tuffthingyosammuzzyiscool("IDK maaaaaaan ")
tuffthingyosammuzzyiscool("welp im gonna ")
goodday = input("How is your day? ")
tuffthingyosammuzzyiscool(f"There was a person named {name}. There favorite animal is a {animal}. They are {age}. There favorite school subject is {schoolfav}. They also play {sport}. There favorite color is {colorlike}. They are having a {goodday} day.")