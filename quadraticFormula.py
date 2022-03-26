import math
print("ok hi this quadratic formula solver")
a = input("ok whats the a term? ")
b = input("nice whats the b term? ")
c = input("great whats the c term? ")
print("processing...") # completely unneeded lol
minusBee = float(b) * -1 #camelCase for the win
# i love funny names for vars
beeSquared = float(b) * float(b)
divider = 2.0 * float(a)
fourAcey = 4.0 * float(a) * float(c) #four*a*c four,a,c fouracey
preSkrt = beeSquared-fourAcey # square root is abbreaviated to sqrt, which looks like skrt, a mumble rap thing
#if preskrt is negative
if preSkrt<0 :
 preposSkrt = preSkrt*-1 #always indent stuff inside elifs elses and ifs
 # down here is x sub 1
 posSkrt = math.sqrt(preposSkrt)
 preposAns1 = minusBee + posSkrt
 posansOne = preposAns1 / divider
 #down here is x sub 2
 preposAns2 = minusBee - posSkrt
 posansTwo = preposAns2 / divider
 print("this answer isnt exact, because negative square roots arent a thing")
 print(f"ok x₁ is  {posansOne}") #have no idea why but when you put variables in print you have to do this
 print(f"and x₂ is  {posansTwo}")
#if preSkrt is pos
else:
 Skrt = math.sqrt(preSkrt)
 # down here is x sub 1
 preAns1 = minusBee + Skrt
 ansOne = preAns1 / divider
 #down here is x sub 2
 preAns2 = minusBee - Skrt
 ansTwo = preAns2 / divider
 print(f"ok x₁ is  {ansOne}") #have no idea why but when you put variables in print you have to do this
 print(f"and x₂ is  {ansTwo}")