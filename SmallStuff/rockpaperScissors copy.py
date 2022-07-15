from ast import If
from random import seed
from random import randint#rock paper scissors
print("hi rock paper scissor!")
rps = int(input("do you play rock, or paper, or scissors? answer with 1 for rock, 2 for paper, or 3 for scissors"))
print("great")
#genrator
seed(1)
# generate some integers
for _ in range(1):
	enemyRps = randint(1, 3) # generates a random number from 1 to three
#this is just what will be printed in the end thing
win = " i win!"
lose = " you win!"
tie = " woops, a tie!"
if enemyRps == 1 :
     printvalue = "rock."
elif enemyRps == 2 :
    printvalue = "paper."
elif enemyRps == 3 :
    printvalue = "scissors."
if rps == 1 :
    if enemyRps == 2 :
        result = lose
    elif enemyRps == 3 :
        result = win
elif rps == 2 :
    if enemyRps == 3 :
        result = lose
    elif enemyRps == 1 :
        result = win
elif rps == 3 :
    if enemyRps == 2 :
        result = win
    elif enemyRps == 1 :
        result = lose
elif rps == enemyRps :
    result = tie
print(printvalue+result)