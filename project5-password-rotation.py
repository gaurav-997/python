import random
import subprocess
import string

current_password = input("please enter your current password \t ")
alpha = string.ascii_letters  # it will print a to Z 
print("alpha", alpha)
num = string.digits   # it will print 0 to 9 
print(num,type(num))
new_password = ''.join(random.choice(alpha + num) for i in range(15))  # it will take 15 random num + alphabats
print(new_password)

""" now change the old password with new , first give the current username & password 
then alter with new """

#subprocess.run(['mysql','-u','root','-p' + current_password , '-e' ,f"ALTER_USER 'root'@'localhost' IDENTIFIED BY '{new_password}';"])


