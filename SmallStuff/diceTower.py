import random
#watch the numberphile dice tower video
#one robot makes the dice and stacks them and add them
#the other one guesses the final number
d1t = random.randint(1, 6) #d is dice
d1b = 7 - d1t #the second number is the dice
d2t = random.randint(1, 6) #and the third letter is t or b for top or bottom
d2b = 7 - d2t
d3t = random.randint(1, 6)
d3b = 7 - d3t
finalNumber = d1b + d2t + d2b + d3b + d3t
print(f"ROLLER ; The final number is {finalNumber}")
print("GUESSER : what is the number on top?")
print(f"ROLLER : {d1t}")
#now its the geusser bot
guesserd1b = 7 - d1t
guesserAnswer = guesserd1b + 14
print(f"GUESSER : the final answer is {guesserAnswer}")
if guesserAnswer == finalNumber :
    print("ROLLER : true")
else :
    print("ROLLER : false")
