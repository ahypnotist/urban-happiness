print("hi ill convert some temporal units into others") #i dont like code thats so unfriendly and robotic
fromTime = input("Ok hours, minutes, or seconds?") #aight so fromtime is the measurement that your gonna convert from
frTime = int(input("How many?")) #how much of the fromtime
toTime = input ("Nice and what do you want to convert it to?") #and totime is what you gonna convert it to
#down here is the ones that start iwth hours
if fromTime == "hours" and toTime == "seconds" :
    answer = frTime * 3600
elif fromTime == "hours" and toTime == "minutes" :
    answer = frTime * 60
#here it starts with minutes
elif fromTime == "minutes" and toTime == "seconds" :
    answer = frTime * 60
elif fromTime == "minutes" and toTime == "hours" :
    answer = frTime / 60
#here it starts with seconds
elif fromTime == "seconds" and toTime == "minutes" :
    answer = frTime / 60
elif fromTime == "seconds" and toTime == "hours" :
    answer = frTime / 3600
if fromTime == toTime :
    print("bruh what")
else :
    print(f"Nice {frTime} {fromTime} is {answer} {toTime} .")