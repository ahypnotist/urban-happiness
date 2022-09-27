print("Welcome to the PyNotes Scale visualizer!")
print("This is a slightly different way of visualizing scales")
print("based on the number of tones and semitones added.")
print("It doesnt really focus on the first and last note being repeated, or the octave")
print("")

SoF = input("Do you want to use sharp notes or flat notes? ")
if SoF == "SHARP" or SoF == "Sharp" or SoF == "sharp" or SoF == "#" :
    SoF = "#"
    noteline = ["C ", "C#", "D ", "D#", "E ", "F ", "F#", "G ", "G#", "A ", "A#", "B "]
elif SoF == "FLAT" or SoF == "flat" or SoF == "Flat" or SoF == "b" :
    SoF = "b"
    noteline = ["C ", "Db", "D ", "Eb", "E ", "F ", "Gb", "G ", "Ab", "A ", "Bb", "B "]

cmajor = input("What note and what mode do you want? Write b not flat, and # not sharp.\n Current modes are major/ionian, chromatic, pentatonic, (natural) minor, and phrygian. ")
aminor = cmajor
cmajor = cmajor.split()
print(f"{aminor} has these notes:")

#pretty useful function
#puts first item of list at the end
#lst is the list itself
#number is the number of times the function will do this

def puf(lst, number):
    for i in range(number):
        added = lst[0]
        lst.pop(0)
        lst.append(added)

#this thing turns any other way of saying a notes name into the capitalized way and the Symbol
#it helps  the "this utilizes puf based on the note you chose" thing

if SoF == "#":
    if cmajor[0] == "c":
        cmajor[0] = "C"
    elif cmajor[0] == "c#" or cmajor[0] == "Db" or cmajor[0] == "db":
        cmajor[0] = "C#"
    elif cmajor[0] == "d":
        cmajor[0] == "D"
    elif cmajor[0] == "d#" or cmajor[0] == "Eb" or cmajor == "eb":
        cmajor[0] == "D#"
    elif cmajor[0] == "e":
        cmajor[0] == "E"
    elif cmajor[0] == "f":
        cmajor[0] == "F"
    elif cmajor[0] == "f#" or cmajor[0] == "gb" or cmajor == "Gb":
        cmajor[0] == "F#"
    elif cmajor[0] == "g":
        cmajor[0] == "G"
    elif cmajor[0] == "g#" or cmajor[0] == "Ab" or cmajor == "ab":
        cmajor[0] == "G#"
    elif cmajor[0] == "a":
        cmajor[0] == "A"
    elif cmajor[0] == "a#" or cmajor[0] == "Bb" or cmajor == "bb":
        cmajor[0] == "A#"
    elif cmajor[0] == "b":
        cmajor[0] == "B"  
elif SoF == "b":
    if cmajor[0] == "c":
        cmajor[0] = "C"
    elif cmajor[0] == "c#" or cmajor[0] == "C#" or cmajor[0] == "db":
        cmajor[0] = "Db"
    elif cmajor[0] == "d":
        cmajor[0] == "D"
    elif cmajor[0] == "d#" or cmajor[0] == "D#" or cmajor == "eb":
        cmajor[0] == "Eb"
    elif cmajor[0] == "e":
        cmajor[0] == "E"
    elif cmajor[0] == "f":
        cmajor[0] == "F"
    elif cmajor[0] == "f#" or cmajor[0] == "gb" or cmajor == "F#":
        cmajor[0] == "Gb"
    elif cmajor[0] == "g":
        cmajor[0] == "G"
    elif cmajor[0] == "g#" or cmajor[0] == "G#" or cmajor == "ab":
        cmajor[0] == "Ab"
    elif cmajor[0] == "a":
        cmajor[0] == "A"
    elif cmajor[0] == "a#" or cmajor[0] == "A#" or cmajor == "bb":
        cmajor[0] == "Bb"
    elif cmajor[0] == "b":
        cmajor[0] == "B"

if cmajor[0] != "A#" or cmajor[0] != "C#" or cmajor[0] != "D#" or cmajor[0] != "F#" or cmajor[0] != "G#":
    cmajor[0] = cmajor[0] + " "
elif cmajor[0] != "Bb" or cmajor[0] != "Db" or cmajor[0] != "Eb" or cmajor[0] != "Gb" or cmajor[0] != "Ab":
    cmajor[0] = cmajor[0] + " "   
#this thing utilizes puf based on the note you chose
found = cmajor[0]
if found != 0 :
    try:
        x = noteline.index(found)
        puf(noteline, x)
    except ValueError:
        if SoF == "#":
            print("You entered a flat when you chose to use sharp notes.\n Now the C Major scale will be displayed. \n")
        if SoF == "b":
            print("You entered a sharp when you chose to use flat notes.\n Now the C Major scale will be displayed. \n")
#pointing
if cmajor[1] == "Major" or cmajor[1] == "major" or cmajor[1] == "MAJOR" or cmajor[1] == "ionian" or cmajor[1] == "Ionian" or cmajor[1] == "IONIAN":
    pointing = ["⬇ ", "  ", "⬇ ", "  ", "⬇ ", "⬇ ", "  ", "⬇ ", "  ", "⬇ ", "  ", "⬇ "]
    print(' '.join(pointing))
elif cmajor[1] == "Minor" or cmajor[1] == "minor" or cmajor[1] == "MINOR" or cmajor[1] == "Natural minor" or cmajor[1] == "Natural Minor" or cmajor[1] == "NATURAL MINOR":
    pointing = ["⬇ ", "  ", "⬇ ", "⬇ ", "  ", "⬇ ", "  ", "⬇ ", "⬇ ", "  ", "⬇ ", "  "]
    print(' '.join(pointing))
elif cmajor[1] == "Phrygian" or cmajor[1] == "phrygian" or cmajor[1] == "PHRYGIAN":
    pointing = ["⬇ ", "⬇ ", "  ", "⬇ ", "  ", "⬇ ", "  ", "⬇ ", "⬇ ", "  ", "⬇ ", "  "]
    print(' '.join(pointing))
elif cmajor[1] == "Pentatonic" or cmajor[1] == "pentatonic" or cmajor[1] == "PENTATONIC":
    pointing = ["⬇ ", "  ", "⬇ ", "  ", "⬇ ", "  ", "  ", "⬇ ", "  ", "  ", "⬇ ", "  "]
    print(' '.join(pointing))
elif cmajor[1] == "Chromatic" or cmajor[1] == "chromatic" or cmajor[1] == "CHROMATIC":
    pointing = ["⬇ ", "⬇ ", "⬇ ", "⬇ ", "⬇ ", "⬇ ", "⬇ ", "⬇ ", "⬇ ", "⬇ ", "⬇ ", "⬇ "]
    print(' '.join(pointing))
elif cmajor[1] == "Dorian" or cmajor[1] == "dorian" or cmajor[1] == "DORIAN":
    pointing = ["⬇ ", "  ", "⬇ ", "⬇ ", "  ", "⬇ ", "  ", "⬇ ", "  ", "⬇ ", "⬇ ", "  "]
    print(' '.join(pointing))
    
print(' '.join(noteline))

#sharp/flat counter
notesinscale = []

for f, b in zip(noteline, pointing):
    if b == "⬇ " :
        notesinscale.append(f)


chord = []

#i am sure there is a better way to do this

c = 1

for n in notesinscale:
    if c == 1:
        chord.append(n)
    elif c == 3:
        chord.append(n)
    elif c == 5:
        chord.append(n)
    c += 1
        

notescale = (' '.join(notesinscale))
tchord = (' '.join(chord))

nos = 0

for j in notesinscale:
    if j == "C#" or j == "D#" or j == "F#" or j == "G#" or j == "A#" or j == "Db" or j == "Eb" or j == "Gb" or j == "Ab" or j == "Bb":
       nos += 1 

print(f"The notes in these scale are {notescale}. There are {nos} sharps or flats in this scale.")
print(f"The basic triad made from this scale would be {tchord}")
