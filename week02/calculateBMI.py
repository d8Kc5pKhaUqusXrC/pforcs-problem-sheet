# calculateBMI.py
# This program is a BMI calculator. Note: no input sanitisation
# author: Mark Brislane


height = int(input("What is your height in cm? "))
weight = int(input("What is your weight in kg? "))

print ("Bad News: Your BMI is " + str(round(((weight / height / height) * 10000),2)))
