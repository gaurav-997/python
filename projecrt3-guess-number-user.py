import random
user = int(input("please enter a number between 1 to 10  "))
computer = 0

while computer != user:
    computer = random.randint(1,10)
    if computer > user :
        computer = computer -1
    elif computer < user:
        computer += 1
print(f"awesom {computer} is equal to {user}")