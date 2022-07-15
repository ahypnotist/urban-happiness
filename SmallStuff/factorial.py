#factorial
y = 1.0 # this is just the only way i could think og
x = int(input("what number will you make a factorial?"))
ans = x #by making ans equal x only at the start, we can do the *
while True :
    if y == x : #by putting this in the beginning we can ake sure no infinite loops happen.
       break
    ans = ans * y #this is the *. it returns upon itself every loop. if i made it ans = x * y, it would be the same every loop. but since it references itself it updates itself
    y += 1.0 #adds one to y ever loop
print(ans)
