#hollowknight hit calculator
#this code is wrong
print("welcome to the hollow knight boss hit calculator!")
print("only thk for now sorry")
nailSpell = input("nail or spells? sorry spore shroom mains")
#NAILS
if nailSpell == "nail" :
    rank = int(input("which upgrade? tell me from 0 to 4, 0 being old nail, and 4 being perfect nail"))
    if rank == 0.0 :
        damage = 5.0
    else :
        damage = 5.0 + (4.0 * (rank))
    art = input("arts or swings?")
    #ARTS
    if art == "art" :
        nailArt = input("cyclone or great?")
        if nailArt == "great" :
            damage = damage * 2.5
        elif nailArt == "cyclone" :
            triggerFinger = input("will u press a bunch more times during the attack for 6 hits or not and only do 3 hits?")
            if triggerFinger == "yes" :
                damage = 6.0 * (damage * 1.25)
            if triggerFinger == "no" :
                print("i have no idea why not but ok")
                damage = 3.0 * (damage * 1.25)
    elif art == "swing" :
        breakStrong = input("do you have fragile/unbreakable strength equipped?") #strength doesnt affect nail arts so its a good indicator that your using swings
    #CHARMS
    fallenFury = input("do you have fury of the fallen equipped?")
    if breakStrong == "yes" :
        if fallenFury == "yes" :
            damage = 2.625 * damage
        else :
            damage = 1.5 * damage
    elif fallenFury == "yes" :
        print("this assumes youre gonna be on 1 mask the entire fight btw")
        damage = 1.75 * damage
#SPEELLS
elif nailSpell == "spells" :
    pass
#lets do thk first bcuz theyre great
boss = "3"
if boss == "3" :
    printboss = "THK"
    helth = 1000.0
prehits = helth / damage
hits = math.ceil(prehits)
print(f"your damage per attack is {damage}")
if art == "art" :
    print(f"it will take {hits} {nailArt} slashes to beat {printboss}")
elif art == "swing" :
    print(f"it will take {hits} {art}s to beat {printboss}")
