import random
#Pig
thisScore = 0
currentScore = 0
print("welcome to pig. you can roll the die an infinite number of times, but if it reaches 1, you lose everything")
while True :
    x = random.randint(1, 6)
    print(x)
    if x == 1 :
        print("woops a one!")
        break
        thisScore = 0
    else :
        thisScore += x
        print(f"your current score is {thisScore} ")
        z = input("would you like to do it again?")
        if z == "no" :
            break
            currentScore += thisScore
            print(f"this is your current score: {currentScore}")

    currentScore += thisScore
    print(f"this is your current score: {currentScore}")
      
