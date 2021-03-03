# extract-url.py
#
# A program that extracts the URLs from an access.log file.
#
# i.e. The part of the URL that is stored in the access.log file, complete with the query parameters
# (I am aware that the host name is not stored in this file, the referring host is)
#
# The program stores the URLs as strings in a list
# [
#  '/cart.do?action=view&itemId=EST-6&productId=SC-MG-G10&JSESSIONID=SD5SL9FF2ADFF4958',
#  '/category.screen?categoryId=SHOOTER&JSESSIONID=SD7SL9FF5ADFF5066'
# ]
#
# author: Mark Brislane
# date: 2021/03/03

import re

# File to open
filename = "www1/access.log"

# Open the file for reading, error if it can't be found
try:
    file = open(filename, 'r', encoding='utf8')
except FileNotFoundError:
    print("The file " + filename + " was not found.")
    sys.exit(1)

# Read the file, line by line, into a list variable called lines.
lines = file.readlines()
# Close the file
file.close()

# Create an empty list
list_of_resources = []
# Create an empty dictionary, used solely for the extra marks section
extra_marks_dict = {}
# Init counter
count = 0

# regex = '(?<=(GET|POST)\s)\S+' <- for some reason, this won't work: "look-behind requires fixed-width pattern"
# RegEx is "GET " / "POST " until the following space. "GET " / "POST " - the resource can then be accessed by
# Group 1 in the result. I wouldn't have to do this if the previous regex worked.
regex = '(?:(GET|POST) )(\S+)'

for line in lines:
    # Extract the resource part of the line
    resource = re.findall(regex, line)[0][1]
    # Add it to a list
    list_of_resources.append(resource)

    # Extra marks section - to create a dict within a list for each resource
    # Split the resource on the ? (path & parameters)
    path = re.split('\?', resource)[0]
    parameters = re.split('\?', resource)[1]
    # Split each parameter into it's key / value pair
    parameter = re.split('&', parameters)
    extra_marks_param_dict = {}
    # Loop through each key / value pair and add them to a dictionary
    for i in parameter:
        key = re.split('=', i)[0]
        value = re.split('=', i)[1]
        extra_marks_param_dict[key] = value
    # Add the dictionary entry for this resource
    extra_marks_dict[count] = {'resource': path, 'parameters': extra_marks_param_dict}
    # Counter is required so each entry in the dict is unique
    count = count + 1

# Print the list of resources from the access log file, remove the # if you really want to do this!
# print(list_of_resources)
# Print the dict required for the extra marks section - again remove the #, the result is quite large!
# print(extra_marks_dict)
