import math
x = 2
while True :
    if ans == 1.0 :
        print("eventually, all reaches 1")
        x += 1
        print(f"now this is with the number {ans}")
    else :
        if (ans % 2.0) == 0 :
            #number is even
            ans = ans / 2.0
        else:
            #number is odd
            preAns = ans * 3.0
            ans = preAns + 1.0
        print(ans)
    ans = x

