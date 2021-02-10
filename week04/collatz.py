# collatz.py
# A program that asks the user to input any positive integer and outputs the successive values
# of the following calculation:
# If it is even, divide it by two, but if it is odd, multiply it by three and add one.
# The program ends when the current value is one.
# author: Mark Brislane
# date: 2021/02/10

# Read in a number from the command line, checks if an integer was entered and then ensures that it's positive.
while True:
    try:
        x = int(input("Please enter a positive integer: "))
    except ValueError:
        print("Sorry, I didn't understand that, please try again.")
        continue
    else:
        if x < 1:
            print("You entered 0 or a negative integer, please try again.")
            continue
        break

# Loop while x is greater than 1, if x = 1 then it will never enter this loop
while x > 1:
    print(x, end=" ")
    # x mod 2 gives a remainder of 0 if x is even
    if (x % 2) == 0:
        # x is divisible by 2 ergo even, so divide it by two and print
        x = int(x / 2)
    else:
        # x is not even so it must be odd, therefore triple it and add 1
        x = int(x * 3 + 1)

# Print the final number (1) and end
print(x)
