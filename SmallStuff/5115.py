# Ask for enter the number from the use  
num = int(input("Enter the integer number: "))
answer = num
revs_num = 0
def revs() :
    res = [int(x) for x in str(num)]
    revs_num = res.reverse()
    answer = int("".join(map(str, revs_num)))
#thank you stack over flow
while True :
    if answer == 5115 :
        print("a palindrome")
    revs()
    print(answer)
        
