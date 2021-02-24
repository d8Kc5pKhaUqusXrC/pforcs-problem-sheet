# es.py
#
# Program that is called like "python es.py filename.txt" and outputs the number of times the latter
# e appears in the file.
#
# Sample file included: moby10b.txt (The Project Gutenberg Etext of Moby Dick, by Herman Melville)
# Obviously the same file as Andrew used as the result is the same.
# https://www.gutenberg.org/files/2701/old/moby10b.txt
#
# author: Mark Brislane
# date: 2021/02/24

import sys

# Read the filename into a variable (passed from arguments)
filename = sys.argv[1]

# Open the file for reading
try:
    file = open(filename, 'r', encoding='utf8')
except FileNotFoundError:
    print("The file " + filename + " was not found.")
    sys.exit(1)

# Read in the file into a variable
data = file.read()

# Count the occurrences of the letter e in the file
e = data.count("e")

# Print the number
print(e)
