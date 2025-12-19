friedchiken_point = 0
sandwhich_point = 0
cookies_point = 0

Answear1 = input("Do you like A Subway, B Seoul Bowl, C Batch Bakery ")
if Answear1 == "A" or Answear1  == "a" :
    sandwhich_point += 1
elif Answear1 == "B" or Answear1 == "b":
    friedchiken_point += 1
elif Answear1 == "C" or Answear1 == "c":
    cookies_point += 1

answear2 = input("Do you like A Jimmy Jhons, B KFC, C Starbucks ")
if answear2 == "A" or answear2 == "a":
    sandwhich_point += 1
elif answear2 == "B" or answear2 == "b" :
    friedchiken_point += 1
elif answear2 == "C" or answear2 == "c" : 
    cookies_point +=1

answear3 = input("Do you like A Panera, B Daves Hot Chiken, C Murcury Coffe ")
if answear3 == "A" or answear3 == "a" :
    sandwhich_point += 1
elif answear3 == "B" or answear3 == "b" :
    friedchiken_point += 1
elif answear3 == "C" or answear3 == "c" :
    cookies_point += 1

answear4 = input("Do you like A Honyhole sandwich, B Honeybee fried chiken, C Byrek ")
if answear4 == "A" or answear4 == "a":
    sandwhich_point += 1
elif answear4 == "B" or answear4 == "b":
    friedchiken_point += 1
elif answear4 == "C" or answear4 == "c":
    cookies_point

answear5 = input("Do you like A Slab Sandwhiches, B Maono Fried Chiken, C Molly moons ")
if answear5 == "A" or Answear1 == "a":
    sandwhich_point += 1
elif answear5 == "B" or answear5 == "b":
    friedchiken_point += 1
elif answear5 == "C" or answear5 == "c" :
    cookies_point += 1

print(f"your score is {friedchiken_point} fried chiken, {cookies_point} Bakery, and {sandwhich_point} sandwhich")
if friedchiken_point > sandwhich_point and friedchiken_point > cookies_point :
    print("Son you kinda like fried chiken")
elif sandwhich_point > friedchiken_point and sandwhich_point > cookies_point :
    print("Why do u like sandwhich")
elif cookies_point > sandwhich_point and cookies_point > friedchiken_point :
    print("you like bakerys bru")
else:
    print("why do u like everything son")

print("676767")


print(f"your score is {friedchiken_point} fried chiken, {cookies_point} Bakery, and {sandwhich_point} sandwhich")
if friedchiken_point > sandwhich_point and friedchiken_point > cookies_point :
    print("Son you kinda like fried chiken")
elif sandwhich_point > friedchiken_point and sandwhich_point > cookies_point :
    print("Why do u like sandwhich")
elif cookies_point > sandwhich_point and cookies_point > friedchiken_point :
    print("you like bakerys bru")
else:
    print("why do u like everything son")