import decimal
#1+0.5+0.25.... = 2
y = decimal.Decimal(1)
ans = y
while True :
    y = y / decimal.Decimal(2)
    ans += y
    print(ans)
    if ans == decimal.Decimal(2):
        print("done")
        break
