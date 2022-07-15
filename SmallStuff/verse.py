original_verse = "Por lo tanto, pónganse toda la armadura de Dios, para que cuando llegue el día malo puedan resistir hasta el fin con firmeza."
list_verse = original_verse.split()
print(list_verse)

length = int((len(list_verse) / 2.0))

for i in range(length):
    x = int(0)
    list_verse.pop(x)
    x += int(2)

print(list_verse)
