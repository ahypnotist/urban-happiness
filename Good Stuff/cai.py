f = open("catrachos_aprenden_ingles.txt", "a")

#ew means english word
#sw means spanish word
#p means pronounciation
#s means sentence

def d(ew, sw, p, s, ts):
    f.write("palabra inglesa: " + ew + "n/   " + "palabra espa;ola: " + sw + "n/   " + "pronunciacion: " + p + "n/   " + "oracion: " + s + "n/   " + "oracion traducida:" + ts)

d("cat", "gato", "cat", "i saw a cat today", "hoy vi un gato")

f.close()
      
