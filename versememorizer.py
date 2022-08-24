verse = "For we are God’s handiwork, created in Christ Jesus to do good works,
which God prepared in advance for us to do. Romans 2:10"

#the verse split into a list
splitverse = verse.split()

#the verse, with every other word replaced by "_"
down_verse = []

#the verse, with the only words being the words replace by "_"
up_verse = []


switch = 0

for i in splitverse:
    if switch == 0:
        down_verse.append(i)
        switch = 1
    elif switch == 1:
        down_verse.append("_")
        up_verse.append(i)
        switch = 0

print(down_verse)

#number off words missing
nowm = len(up_verse)
nowm_good = 0
nowm_bad = []
nowm_should = []

answer = input("Enter the missing words! No commas, just spaces")
answer = answer.split()

for f, b in zip(up_verse, answer):
    if f == b:
        nowm_good += 1
    if f != b:
        nowm_bad.append(f)
        nowm_should.append(b)

print(f"You got {nowm_good} words out of {nowm} correct!")

if len(nowm_bad) != 0:
    print(f"You messed up {nowm_bad} and you wrote them as {nowm_should}, respectively.")
