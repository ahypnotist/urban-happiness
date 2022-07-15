#measurement converter

#grams to kilograms to milligrams

def converter(kmg, original, to):
    #kmg is the amount
    #original is the original measurement
    # to is the to be converted measurement
    if original == "kg" and to == "g" or original == "g" and to == "mg":
        new = kmg / 1000
        print(f"{kmg} {original} is {new} {to}")
    elif original == "g" and to == "kg" or original == "mg" and to == "g" :
        new = kmg * 1000
        return(new)
    elif original == "mg" and to == "kg":
        new = kmg / 1000000
        print(f"{kmg} {original} is {new} {to}")
    elif original == "kg" and to == "mg":
        new = kmg * 1000000
        print(f"{kmg} {original} is {new} {to}")
