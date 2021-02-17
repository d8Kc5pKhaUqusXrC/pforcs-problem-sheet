# squareroot.py
#
# Program that estimates the square root of a number using the Newton method
#
# Let N be any number then the square root of N can be given by the formula:
# root = 0.5 * (X + (N / X)) where X is any guess which can be assumed to be N or 1.
#
# Approach
# 1. Assign X to the N itself.
# 2. Now, start a loop and keep calculating the root which will surely move towards the correct square root of N.
# 3. Check for the difference between the assumed X and calculated root, if not yet inside tolerance then update root
#    and continue.
# 4. If the calculated root comes inside the tolerance allowed then break out of the loop.
# 5. Print the root.
#
# Uses code from https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
#
# author: Mark Brislane
# date: 2021/02/17

def sqrt(n):
    # Calculate the square root of number using the Newton method
    # Assign X to the N itself.
    x = n

    # Now, start a loop and keep calculating the root which will surely move towards the correct square root of N.
    while 1:
        # Calculate an initial / closer root
        calc_root = 0.5 * (x + n / x)

        # Check for the difference between the assumed X and calculated root,
        # if not yet inside tolerance (0.1) then update root and continue.
        if abs(calc_root - x) < 0.1:
            # If the calculated root comes inside the tolerance allowed then break out of the loop.
            break

        x = calc_root

    return calc_root


# Read in a number from the command line, checks if indeed it was a number and then ensures that it's positive.
while True:
    try:
        number = float(input("Please enter a positive number: "))
    except ValueError:
        print("Sorry, I didn't understand that, please try again.")
        continue
    else:
        if number <= 0:
            print("You entered 0 or a negative integer, please try again.")
            continue
        break

root = sqrt(number)

# Print the root
print("The square root of " + str(number) + " is approx. " + "{:.1f}".format(root))