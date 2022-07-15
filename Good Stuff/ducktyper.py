import random as r
#dnd dice helper

proficiency_modifier = int(input("What is your proficiency modifier?"))

stats = input("Enter your character's stat modifiers. The first stat is strength, second is dexterity, "
              "\n third is constitution, fourth is intelligence, fifth is wisdom, and sixth is charisma. "
              "\n Enter them without spaces and divided by commas.")
stats = stats.split(",")

check = input("What ability are you trying to check? Enter it with the first letter capitalized.")
proficient = input("Is your character proficient in this ability? Enter yes or no.")

if check == "Deception" or "Persuasion" or "Performance" or "Intimidation" :
    if proficient == "yes":
        add = int(stats[5]) + proficiency_modifier
elif check == "Athletics":
    if proficient == "yes":
        add = int(stats[0]) + proficiency_modifier
elif check == "Acrobatics" or "Sleight of Hand" or "Stealth":
    if proficient == "yes":
        add = int(stats[1]) + proficiency_modifier
elif check == "Arcana" or "History" or "Investigation" or "Nature" or "Religion":
    if proficient == "yes":
        add = int(stats[4]) + proficiency_modifier
elif check == "Animal Handling" or "Insight" or "Medicine" or "Perception" or "Survival":
    if proficient == "yes":
        add = int(stats[3]) + proficiency_modifier

check = input("Are you trying to check an ability or attack?")
                        
if check == "ability":
    x = r.randint(1,20)
    x += add