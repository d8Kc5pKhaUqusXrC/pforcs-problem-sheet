# calculateBMI.py
# This program is a BMI calculator. Note: no input sanitisation
# author: Mark Brislane

# Inputs height & weight, cast to ints so we can work with them as numbers
height = int(input("What is your height in cm? "))
weight = int(input("What is your weight in kg? "))

# Calculate the BMI (weight / height in m2) rounded to 2 decimal places
print ("Bad News: Your BMI is " + str(round(((weight / height / height) * 10000),2)))
