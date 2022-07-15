y = "thehypotenuse"

def splity(word):
    return [char for char in word]
    #this splity function is from geeks for geeks :|
    #this had to be splity because i used another function named split.

x = splity(y)
length = len(x)

n = []

for i in x:
    n.append(ord(i) - 96)

print(n)

for j in n:
    if j == -64 :
        b = n.index(j)
        del n[b]

m = [c * length for c in n]

print(m)

f = []

king = 1

for g in m :
    if king == 1 :
        q = m[0] + m[1]
        f.append(q)
        del m[0]
        del m[0]
        king += 1
    elif king == 2 :
        q = m[0] - m[1]
        f.append(q)
        del m[0]
        del m[0]
        king -= 1

print(f)