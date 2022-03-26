import random
import math
x = 1 #x is the score
#rock paper scissors lizard spock
print("hi welcome to rock paper scissors lizard spock!")
#this is just what will be printed in the end thing
#EMOJIS: 👊🖖✋✌🤏. rock, spock, paper, scissors, lizard
win = " you win!"
lose = " i win!"
tie = " woops, a tie!"
#explanations
#paper
pR = "paper covers rock!"
pC = "scissors cuts paper!"
pL = "lizards eat paper!"
pS = "paper disproves spocks theory!"
#rock
rS = "spock vaporises rock!"
rL = "rock smashes lizard!"
rC = "rock smashes scissors!"
#scissors
cL = "scissors decapitates lizard!"
cS = "spock vaporizes scissors!"
#spock
sL = "lizard poisons spock!"
#tie
tieexplained = "2 of the same equals a tie!"
#now the actual code begins
while True :
     #THE ENEMY
     enemyRps = random.randint(1, 5) #the generator has to be inside the loop otherwise the enemy has the same thing every times
     #the printvalues
     if enemyRps == 1 :
          printvalue = "👊 rock!"
     elif enemyRps == 2 :
          printvalue = "✋ paper!"
     elif enemyRps == 3 :
          printvalue = "✌ scissors!"
     elif enemyRps == 4 :
          printvalue = "🤏 lizard!"
     elif enemyRps == 5 :
          printvalue = "🖖 spock!"
     #YOU
     rps = int(input("do you play rock, or paper, or scissors? answer with 1 for rock, 2 for paper, 3 for scissors, 4 for lizard, and 5 for spock"))
     #rock
     if rps == 1.0 :
          if enemyRps == 2.0 :
               result = lose
               explanation = pR
          elif enemyRps == 3.0 :
               result = win
               explanation = rC
          elif enemyRps == 4.0 :
               result = win
               explanation = rL
          elif enemyRps == 5.0 :
               result = lose
               explanation = rS
     #paper
     elif rps == 2.0 :
          if enemyRps == 3.0 :
               result = lose
               explanation = pC
          elif enemyRps == 1.0 :
               result = win
               explanation = pR
          elif enemyRps == 4.0 :
               result = lose
               explanation = pL
          elif enemyRps == 5.0 :
               result = win
               explanation = pS
     #scissors
     elif rps == 3.0 :
          if enemyRps == 2.0 :
               result = win
               explanation = pC
          elif enemyRps == 1.0 :
               result = lose
               explanation = rC
          elif enemyRps == 4.0 :
               result = win
               explanation = cL
          elif enemyRps == 5.0 :
               result = lose
               explanation = cS
     #lizard
     elif rps == 4.0 :
          if enemyRps == 1.0 :
               result = lose
               explanation = rL
          elif enemyRps == 2.0 :
               result = win
               explanation = pL
          elif enemyRps == 3.0 :
               result = lose
               explanaion = cL
          elif enemyRps == 5.0 :
               result = win
               explanation = sL
     elif rps == 5.0 :
          if enemyRps == 1.0 :
               result = win
               explanation = rS
          elif enemyRps == 2.0 :
               result = lose
               explanation = pS
          elif enemyRps == 3.0 :
               result = win
               explanation = cS
          elif enemyRps == 4.0 :
               result = lose
               explanation = sL
     #tie
     elif rps == enemyRps :
          result = tie
          explanation = tieexplanation
     
     print(printvalue)
     print(explanation)
     print(result)
     #this prints your score
     if result == win :
          x = x + 1
     elif result == lose :
          x = x - 1
     elif result == tie :
          x = x + 0
     print(f"this is your score : {x}")
     play = input("do you wanna play again? answer with yes or no ")
     if play == "no" :
          print("goodbye")
          break
