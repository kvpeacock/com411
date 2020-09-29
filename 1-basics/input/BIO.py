eye=input("Enter robot's eyes plz")

inputs=input("Enter Robot's name, age, height and weight, seperated by a comma: ")
name = inputs.split(",")
divider = float(name[2])**2
BMI = float(name[3])/divider
inputs=input("Enter Robot's lives, energy level and shield level, seperated by a comma: ")
settings = inputs.split(",")

print("\n##########")
print("#  {}  {}  #".format(eye,eye))
print("#  ----  #")
print("##########")
print("Lives:" + "♥"*int(settings[0]))
print("Energy:" + "♦"*int(settings[1]))
print("Shield:" + "♦"*int(settings[2]))
print ("The robot is called " + name[0] 0+ " and it is " + name[1] + " years old and their bmi is " + str(round(BMI,2)))

