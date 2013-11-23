import random
import time
letters = ["a", "e", "i", "o", "u", "y", "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
vowels = ["a", "e", "i", "o", "u", "y"]
consanents = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
name=[]
global_smtp = name
def isIn(List, String):
    itIs=False
    for s in List:
        if s == String:
            itIs=True
    return itIs

def first():
    chosen = random.choice(letters).upper()
    name.append(chosen)
    return chosen
def second():
    if isIn(consanents, name[0])==True:
        tORf=[True, False]
        if random.choice(tORf)==True:
            chosen=random.choice(consanents)
            name.append(chosen)
            return chosen
        else:
            chosen=random.choice(vowels)
            name.append(chosen)
            return chosen
    else:
        chosen=random.choice(consanents)
        name.append(chosen)
        return chosen
def third():
    if isIn(vowels, name[0]) and isIn(vowels, name[1]):
        chosen=random.choice(consanents)
        name.append(chosen)
        return chosen
    elif isIn(consanents, name[0]) and isIn(consanents, name[1]):
        chosen=random.choice(vowels)
        name.append(chosen)
        return chosen
    else:
        chosen=random.choice(letters)
        name.append(chosen)
        return chosen
def fourth():
    if isIn(vowels, name[1]) and isIn(vowels, name[2]):
        chosen=random.choice(consanents)
        name.append(chosen)
        return chosen
    elif isIn(consanents, name[1]) and isIn(consanents, name[2]):
        chosen=random.choice(vowels)
        name.append(chosen)
        return chosen
    else:
        chosen=random.choice(letters)
        name.append(chosen)
        return chosen
def fifth():
    if isIn(vowels, name[2]) and isIn(vowels, name[3]):
        chosen=random.choice(consanents)
        name.append(chosen)
        return chosen
    elif isIn(consanents, name[2]) and isIn(consanents, name[3]):
        chosen=random.choice(vowels)
        name.append(chosen)
        return chosen
    else:
        chosen=random.choice(letters)
        name.append(chosen)
        return chosen    
    
"""def main():
    print("Random Name Generator")
    num2do=int(raw_input("How many names do you want?  "))
    count=0
    while count <= num2do:
        first()
        second()
        third()
        fourth()
        fifth()
        print name
        name=[]
        count+=1
    raw_input("Press enter to exit")
    print "closing..."
    time.sleep(1)
main()"""
first()
second()
third()
fourth()
fifth()
print name


        
