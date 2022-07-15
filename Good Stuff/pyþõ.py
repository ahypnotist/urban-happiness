import re

print("Welcome to Pyþõ, or Thorn Tilde. ")
print("It is not a spelling reform, but merely a word shortener. ")
print("You may think of it a twitter character limit bypasser, or a text compressor and decompressor.")
title_of_text = input("what is the title of this text?")
decipher_or_encode = input("are you going to DECIPHER text or ENCODE text?")
text = input("enter the text: ")


def splity(word):
    return [char for char in word]
    #this splity function is from geeks for geeks :|
    #this had to be splity because i used another function named split.


lowercase_text = text.lower()
#lowercase_text exists to turn text into lowercase, to check if its the same lower or not
if lowercase_text == text:
    y = text
    #y is used after this ifelse statement so i had to to do this
    lc = "LOWERCASE"
    #the thing didnt detect that it was lowercase
    #i wrote this after lc = input line
else:
    lc = input(
        "do you want to make all characters LOWERCASE or KEEP it as it is? (lowercasing makes it more compressed)")
    if lc == "LOWERCASE":
        y = text.lower()
    elif lc == "KEEP":
        y = text

one = y.split()
p1 = len(splity(y))
print(f"the original is {p1} characters long.\n")
print(f"{y} \n")


def ev(word):
    n = x.index(i)
    x[n] = word
    #this is literally the most used function in the whole script
    #since refindall divides the text into digraphs, this checks where that is, then replaces it
    #word is the diacriticized (is that a word?) shortening
    #the original copy felt boilerplatey (although thats not the definition of the word definitely feels like it


if decipher_or_encode == "ENCODE":
    x = re.findall(
        r"have|with|is|as|us|es|os|and|of|ph|sh|that|the|ing|ar|ir|or|ur|ssi|ng|aa|ee|ii|oo|uu|ll|ed|ck|ch|qu|an|en|in|un|on|wh"
        r"|th|er|augh|ough|ou|gh|\S|\s",
        y)
    # i needed the \S and \s to be its own thing or else it would just print the digraphs
    for i in x:
        if i == "ough":
            ev("ō")
        elif i == "have":
            ev("ɦ")
        elif i == "with":
            ev("ɰ")
        elif i == "is":
            ev("í")
        elif i == "as":
            ev("á")
        elif i == "us":
            ev("ú")
        elif i == "es":
            ev("é")
        elif i == "os":
            ev("ó")
        elif i == "ph":
            ev("ᵽ")
        elif i == "that":
            ev("ð")
        elif i == "of":
            ev("ɵ")
        elif i == "and":
            ev("&")
        elif i == "the":
            ev("ꝥ")
        elif i == "ing":
            ev("ň")
        elif i == "ar":
            ev("ä")
        elif i == "or":
            ev("ö")
        elif i == "ur":
            ev("ü")
        elif i == "ir":
            ev("ï")
        elif i == "ng":
            ev("ŋ")
        elif i == "ssi":
            ev("ş")
        elif i == "aa":
            ev("â")
        elif i == "ee":
            ev("ê")
        elif i == "ii":
            ev("î")
        elif i == "oo":
            ev("ô")
        elif i == "uu":
            ev("û")
        elif i == "augh":
            ev("ā")
        elif i == "gh":
            ev("ġ")
        elif i == "ed":
            ev("ɖ")
        elif i == "ll":
            ev("ɫ")
        elif i == "ck":
            ev("ç")
        elif i == "ch":
            ev("č")
        elif i == "sh":
            ev("š")
        elif i == "th":
            ev("þ")
        elif i == "ou":
            ev("ø")
        elif i == "wh":
            ev("ɸ")
        elif i == "er":
            ev("ë")
        elif i == "an":
            ev("ã")
        elif i == "en":
            ev("ẽ")
        elif i == "in":
            ev("ĩ")
        elif i == "on":
            ev("õ")
        elif i == "un":
            ev("ũ")
        elif i == "qu":
            ev("ꝗ")
elif decipher_or_encode == "DECIPHER":
    x = re.findall(r"ɦ|ɰ|í|á|ú|é|ó|å|ᵽ|š|ɵ|ð|ꝥ|ň|ä|ï|ö|ü|ş|ŋ|â|ê|î|ô|û|ɫ|ɖ|ç|č|ꝗ|ã|ẽ|ĩ|ũ|õ|ɸ|þ|ë|ā|ō|ø|ġ|\S|\s", y)
    for i in x:
        # this does everything basically
        if i == "ō":
            ev("ough")
        elif i == "ɰ":
            ev("with")
        elif i == "ɦ":
            ev("have")
        elif i == "í":
            ev("is")
        elif i == "á":
            ev("as")
        elif i == "ú":
            ev("us")
        elif i == "é":
            ev("es")
        elif i == "ó":
            ev("os")
        elif i == "ᵽ":
            ev("ph")
        elif i == "ð":
            ev("that")
        elif i == "ɵ":
            ev("of")
        elif i == "å":
            ev("&")
        elif i == "ꝥ":
            ev("the")
        elif i == "ň":
            ev("ing")
        elif i == "ä":
            ev("ar")
        elif i == "ö":
            ev("or")
        elif i == "ü":
            ev("ur")
        elif i == "ï":
            ev("ir")
        elif i == "ŋ":
            ev("ng")
        elif i == "ş":
            ev("ssi")
        elif i == "â":
            ev("aa")
        elif i == "ê":
            ev("ee")
        elif i == "î":
            ev("ii")
        elif i == "ô":
            ev("oo")
        elif i == "û":
            ev("uu")
        elif i == "ā":
            ev("augh")
        elif i == "ġ":
            ev("gh")
        elif i == "ɖ":
            ev("ed")
        elif i == "ɫ":
            ev("ll")
        elif i == "ç":
            ev("ck")
        elif i == "č":
            ev("ch")
        elif i == "š":
            ev("sh")
        elif i == "þ":
            ev("th")
        elif i == "ø":
            ev("ou")
        elif i == "ɸ":
            ev("wh")
        elif i == "ë":
            ev("er")
        elif i == "ã":
            ev("an")
        elif i == "ẽ":
            ev("en")
        elif i == "ĩ":
            ev("in")
        elif i == "õ":
            ev("on")
        elif i == "ũ":
            ev("un")
        elif i == "ꝗ":
            ev("qu")

x = ''.join(x)  # turn it all into one string
print(f"{x} \n")

two = x.split()

p2 = len(splity(x))
print(f"the length of the new one is {p2} \n")

percent2 = 100 - ((p2 / p1) * 100)
print(f"the new version is {percent2} percent shorter than the length of the original")

m = 0
for f, b in zip(one, two):
    if f != b:
        m += 1
print(f"{m} words were altered")

f = open("results.txt", "a")
f.write(f"{title_of_text} {percent2} {decipher_or_encode} {lc} \n")
f.close()
