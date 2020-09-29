inputs=input("Enter lives, energy level and shield level, seperated by a comma: ")

name = inputs.split(",")

print("Lives:" + "♥"*int(name[0]))
print("Energy:" + "♦"*int(name[1]))
print("Shield:" + "♦"*int(name[2]))