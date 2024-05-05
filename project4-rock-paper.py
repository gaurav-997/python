# here we are playing against computer 
import random
computer = random.choice(["rock","paper","sessior"])
print(computer)

user = input("please choose from rock paper sessior ".lower)

if user == computer:
    print("match tie ")
elif (user == "rock") or (user == "sessior" and computer == "paper"):
    print("user wins")
elif (user == "paper") or  (user == "sessior" and computer == "rock"):
    print("user lost")