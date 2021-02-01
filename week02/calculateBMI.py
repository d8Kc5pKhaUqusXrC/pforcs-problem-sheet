# calculateBMI.py
# This program is a BMI calculator.
# author: Mark Brislane

# Inputs height & weight, cast to ints so we can work with them as numbers
while True:
    try:
        height = int(input("What is your height in cm? "))
    except ValueError:
        print("Sorry, I didn't understand that, please try again.")
        continue
    else:
        break
while True:
    try:
        weight = int(input("What is your weight in kg? "))
    except ValueError:
        print("Sorry, I didn't understand that, please try again.")
        continue
    else:
        break

# Calculate the BMI (weight / height in m2) rounded to 2 decimal places
print("Bad News: Your BMI is " + str(round(((weight / height / height) * 10000),2)))
