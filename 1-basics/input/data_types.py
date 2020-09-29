inputs=input("Enter name, age, height and weight, seperated by a comma: ")
name = inputs.split(",")
divider = float(name[2])**2
BMI = float(name[3])/divider
print (name[0]+ "you are " + name[1] + " years old and your bmi is " + str(round(BMI,2)))