import math

#thing that generates names from when you were born
def split(word):
    return [char for char in word]

def Namer(m, d, y):
    name = []
    split(m)
    #first 2 letters of the month appended to babyname 
    name.append(m[0])
    name.append(m[1])
    #do the same for the day
    split(d)
    name.append(d[0])
    name.append(d[1])
    name.append(d[2])
    #check if the year is even or odd
    d2 = y / 2
    r2 = math.floor(d2)
    if r2 == d2:
        name.append("ey")

    name = ''.join(name)
    print(name)

    
Namer("july", "monday", 2008)
