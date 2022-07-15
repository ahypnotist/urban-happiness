#multiply 2 words
#make each letter into its number value. a is 1, b is 2, etc.
l = input("give me the first word")
n = []
for x in l:
   n.append(ord(x) - 96)
first = sum(n)

i = input("give me the first word")
j = []
for w in i:
   n.append(ord(w) - 96)
second = sum(n)

multiplicate = first * second
print(multiplicate)

x = [int(a) for a in str(multiplicate)]
print(x)

