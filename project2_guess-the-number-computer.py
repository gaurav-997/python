# Computer has a secret number and we are guessing that 
import random
computer = random.randint(1,10)
user=0
while(user != computer):
    user = int(input("please enter the number between 1 to 10  "))
    if user < computer:
        print("user is low")
    elif user >computer:
        print("user is high")
    
print("both are equal congratualtions")
    