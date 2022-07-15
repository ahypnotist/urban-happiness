import re
print("Welcome to Pyþõ, or Thorn Tilde. This project started when i heard that the british abbreviated ough with ō in ww2, to conserve paper. Ive since never been able to prove this (source: dude just trust me), but the idea went on. I then heard that the letter thorn with a strike was sometimes used to abbreviate the, and the letter edh was used for that. I also knew that spanish and french scribes wrote a tilde over a vowel with an n after it. I combined all of these into this, and added more diacritics of my own making. It is not a spelling reform, but merely a word shortener. You may think of it a twitter character limit bypasser, or a text compressor and decompressor.")
de = input("are you going to DECIPHER text or ENCODE text?")
w = input("enter the text: ")
def splity(word):
    return [char for char in word]

checker = w.lower()

if checker != w:
    lowercase = input("do you want to make all characters LOWERCASE or KEEP it as it is? (lowercasing makes it more compressed)")
    if lowercase == "LOWERCASE" :
        y = w.lower()
    elif lowercase == "KEEP" :
        y = w
elif checker == w:
        y = w

one = y.split()
p1 = len(splity(y))
print(f"the original is {p1} characters long.\n")
print(f"{y} \n")
if de == "ENCODE" :
    x = re.findall(r"is|as|us|es|os|and|of|ph|sh|that|the|ing|ar|ir|or|ur|ssi|ng|aa|ee|ii|oo|uu|ll|ed|ck|ch|qu|an|en|in|un|on|wh|th|er|augh|ough|ou|gh|\S|\s", y)
    #i needed the \S and \s to be its own thing or else it would just print the digraphs
    for i in x:
        #this does everything basically
        if i == "ough" :
            indie =  x.index(i)
            x[indie] = "ō"
        elif i == "is" :
            indie =  x.index(i)
            x[indie] = "í"
        elif i == "as" :
            indie =  x.index(i)
            x[indie] = "á"        
        elif i == "us" :
            indie =  x.index(i)
            x[indie] = "ú"        
        elif i == "es" :
            indie =  x.index(i)
            x[indie] = "é"
        elif i == "os" :
            indie =  x.index(i)
            x[indie] = "ó"
        elif i == "ph" :
            indie =  x.index(i)
            x[indie] = "ᵽ"
        elif i == "that" :
            indie =  x.index(i)
            x[indie] = "ð"        
        elif i == "of" :
            indie =  x.index(i)
            x[indie] = "ɵ"        
        elif i == "and" :
            indie =  x.index(i)
            x[indie] = "å"
        elif i == "the" :
            indie =  x.index(i)
            x[indie] = "ꝥ"
        elif i == "ing" :
            indie =  x.index(i)
            x[indie] = "ň"
        elif i == "ar" :
            indie =  x.index(i)
            x[indie] = "ä"
        elif i == "or" :
            indie = x.index(i)
            x[indie] = "ö"
        elif i == "ur" :
            indie =  x.index(i)
            x[indie] = "ü"
        elif i == "ir" :
            indie = x.index(i)
            x[indie] = "ï"
        elif i == "ng" :
            indie =  x.index(i)
            x[indie] = "ŋ"
        elif i == "ssi" :
            indie = x.index(i)
            x[indie] = "ş"
        elif i == "aa" :
            indie =  x.index(i)
            x[indie] = "â"
        elif i == "ee" :
            indie = x.index(i)
            x[indie] = "ê"
        elif i == "ii" :
            indie = x.index(i)
            x[indie] = "î"
        elif i == "oo" :
            indie = x.index(i)
            x[indie] = "ô"
        elif i == "uu" :
            indie = x.index(i)
            x[indie] = "û"
        elif i == "augh" :
            indie =  x.index(i)
            x[indie] = "ā"
        elif i == "gh" :
            indie =  x.index(i)
            x[indie] = "ġ"
        elif i == "ed" :
            indie = x.index(i)
            x[indie] = "ɖ"
        elif i == "ll" :
            indie = x.index(i)
            x[indie] = "ɫ"
        elif i == "ck" :
            indie = x.index(i)
            x[indie] = "ç"
        elif i == "ch" :
            indie = x.index(i)
            x[indie] = "č"
        elif i == "sh" :
            indie = x.index(i)
            x[indie] = "š"
        elif i == "th" :
            indie =  x.index(i)
            x[indie] = "þ"
        elif i == "ou" :
            indie = x.index(i)
            x[indie] = "ø"
        elif i == "wh" :
            indie = x.index(i)
            x[indie] = "ɸ"
        elif i == "er" :
            indie = x.index(i)
            x[indie] = "ë"
        elif i == "an" :
            indie =  x.index(i)
            x[indie] = "ã"
        elif i == "en" :
            indie = x.index(i)
            x[indie] = "ẽ"
        elif i == "in" :
            indie = x.index(i)
            x[indie] = "ĩ"
        elif i == "on" :
            indie = x.index(i)
            x[indie] = "õ"
        elif i == "un" :
            indie = x.index(i)
            x[indie] = "ũ"
        elif i == "qu" :
            indie = x.index(i)
            x[indie] = "ꝗ"
elif de == "DECIPHER" :
    x = re.findall(r"í|á|ú|é|ó|å|ᵽ|š|ɵ|ð|ꝥ|ň|ä|ï|ö|ü|ş|ŋ|â|ê|î|ô|û|ɫ|ɖ|ç|č|ꝗ|ã|ẽ|ĩ|ũ|õ|ɸ|þ|ë|ā|ō|ø|ġ|\S|\s", y)
    for i in x:
        #this does everything basically
        if i == "ō" :
            indie =  x.index(i)
            x[indie] = "ough"
        elif i == "í" :
            indie =  x.index(i)
            x[indie] = "is"
        elif i == "á" :
            indie =  x.index(i)
            x[indie] = "as"        
        elif i == "ú" :
            indie =  x.index(i)
            x[indie] = "us"        
        elif i == "é" :
            indie =  x.index(i)
            x[indie] = "es"
        elif i == "ó" :
            indie =  x.index(i)
            x[indie] = "os"
        elif i == "ᵽ" :
            indie =  x.index(i)
            x[indie] = "ph"
        elif i == "ð" :
            indie =  x.index(i)
            x[indie] = "that"           
        elif i == "ɵ" :
            indie =  x.index(i)
            x[indie] = "of"        
        elif i == "å" :
            indie =  x.index(i)
            x[indie] = "and"
        elif i == "ꝥ" :
            indie =  x.index(i)
            x[indie] = "the"
        elif i == "ň" :
            indie =  x.index(i)
            x[indie] = "ing"
        elif i == "ä" :
            indie =  x.index(i)
            x[indie] = "ar"
        elif i == "ö" :
            indie = x.index(i)
            x[indie] = "or"
        elif i == "ü" :
            indie =  x.index(i)
            x[indie] = "ur"
        elif i == "ï" :
            indie = x.index(i)
            x[indie] = "ir"
        elif i == "ŋ" :
            indie =  x.index(i)
            x[indie] = "ng"
        elif i == "ş" :
            indie = x.index(i)
            x[indie] = "ssi"
        elif i == "â" :
            indie =  x.index(i)
            x[indie] = "aa"
        elif i == "ê" :
            indie = x.index(i)
            x[indie] = "ee"
        elif i == "î" :
            indie = x.index(i)
            x[indie] = "ii"
        elif i == "ô" :
            indie = x.index(i)
            x[indie] = "oo"
        elif i == "û" :
            indie = x.index(i)
            x[indie] = "uu"
        elif i == "ā" :
            indie =  x.index(i)
            x[indie] = "augh"
        elif i == "ġ" :
            indie =  x.index(i)
            x[indie] = "gh"
        elif i == "ɖ" :
            indie = x.index(i)
            x[indie] = "ed"
        elif i == "ɫ" :
            indie = x.index(i)
            x[indie] = "ll"
        elif i == "ç" :
            indie = x.index(i)
            x[indie] = "ck"
        elif i == "č" :
            indie = x.index(i)
            x[indie] = "ch"
        elif i == "š" :
            indie = x.index(i)
            x[indie] = "sh"
        elif i == "þ" :
            indie =  x.index(i)
            x[indie] = "th"
        elif i == "ø" :
            indie = x.index(i)
            x[indie] = "ou"
        elif i == "ɸ" :
            indie = x.index(i)
            x[indie] = "wh"
        elif i == "ë" :
            indie = x.index(i)
            x[indie] = "er"
        elif i == "ã" :
            indie =  x.index(i)
            x[indie] = "an"
        elif i == "ẽ" :
            indie = x.index(i)
            x[indie] = "en"
        elif i == "ĩ" :
            indie = x.index(i)
            x[indie] = "in"
        elif i == "õ" :
            indie = x.index(i)
            x[indie] = "on"
        elif i == "ũ" :
            indie = x.index(i)
            x[indie] = "un"
        elif i == "ꝗ" :
            indie = x.index(i)
            x[indie] = "qu"
#basically, if find "X", turn it into Y.


x = ''.join(x) #turn it all into one string
print(f"{x} \n")

two = x.split()

p2 = len(splity(x))
print(f"the length of the new one is {p2} \n")

quotient = p2 / p1

percent = quotient * 100
percent2 = 100 - percent
print(f"the new version is {percent2} percent shorter than the length of the original")

count = 0
for f, b in zip(one, two):
    if f != b:
        count += 1
print(f"{count} words were altered")
