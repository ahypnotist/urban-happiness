import decimal
import math
print("the cipher shall commence")
l = input("give me the words, no spaces, no numbers")
n = []
for x in l:
   n.append(ord(x) - 96)
y = sum(n)

ans = y
while True :
    if ans == decimal.Decimal(1.0) :
        break
    else :
        z = ans / decimal.Decimal(2)
        oddEven = math.floor(z)
        evenOdd = math.ceil(z)                    
        if oddEven == evenOdd :
            #number is even
            ans = ans / decimal.Decimal(2.0)
        else:
            #number is odd
            preAns = ans * decimal.Decimal(3.0)
            ans = preAns + decimal.Decimal(1.0)
print(ans)
