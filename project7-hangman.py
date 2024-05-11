""" hangman is a game where one player comes with a word and other have to guess the latters of this word,
here number of latters are placed initially with dash and space between them ( e.g INDIA :- _ _ _ _ _)
now if second player choose the correct word its written on dashes , if wrong word then hangman body will start making
Hnagman body has 6 parts :- head , 2 arms , 1 body , 2 legs   if second player guess 6 wrong then game lost
wrong words guess is written in saperate list
"""
import random
from nouns import words
print( " you have 6 chnaces to guess the word correctly ")
chances = 6
gameover = False 
phrase = random.choice(words).lower()
phrase = list(phrase)
print(phrase)

correct_list = []
for latter in phrase:
    correct_list += '_'
print(correct_list)
 
   
while chances:
    guess_latter = input("guess a latter from a to z \t ").lower()
    for position in range(len(phrase)):
        if phrase[position] == guess_latter:
            correct_list[position] = guess_latter
            print(correct_list)
            if correct_list == phrase:
                gameover = True
                print( "you won")
    if guess_latter not in phrase:
        chances -=1
        print(f" you have {chances} left")
        
# if word match break the while loop 
    if gameover == True:
        break 
# if user lost then print the actual word 
    if chances == 0:
        print(phrase, "and you lose")





    
    