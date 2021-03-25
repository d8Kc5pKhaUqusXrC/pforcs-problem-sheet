# Task:
# Write a (bullet proof) function called averageTo(aList, toIndex)
#
# The function should take in a list and an index.
#
# The function will return the average of the numbers up to and including the toIndex in the aList.
#
# When I say "bullet proof", I would like the function to always return an integer, even if a error occurs
# (say return -1), but it will use logging to make a meaningful log warning, for any error that occurs (eg the
# aList contains an entry that is not a number/ toIndex is not valid, there are many things that could go wrong)
#
# Write the code to test all the things that could go wrong with this function, and a test to
# check the function does work.
#
# The test code can be in the same file or different file.
#
# author: Mark Brislane
# date: 2021/03/23

import logging
logging.basicConfig(level=logging.DEBUG)

def averageTo(aList, toIndex):
    sum = 0
    average = -1
    try:
        # Check if toIndex is longer then the length of aList and also zero or greater
        # Will result in a TypeError if toIndex is not a number at all (except TypeError below)
        if (toIndex <= len(aList)) and (toIndex >= 0):
            try:
                for i in range(toIndex):
                    sum = sum + aList[i]
                average = sum / toIndex
            # An entry in the list is not a number.
            except TypeError:
                logging.debug("At least one of the entries in the list was not a number.")
            # Fired when toIndex is 0
            except ZeroDivisionError:
                logging.debug("The index was 0")
        # Else, if toIndex is negative
        elif toIndex < 0:
            logging.debug("The index, %d, was negative", toIndex)
        # Else, i.e. toIndex was longer than the list
        else:
            logging.debug("The index, %d, was out of range - not enough entries in the list", toIndex)
    except TypeError:
        logging.debug("The index was not a number.")
    return average


if __name__ == '__main__':
    assert averageTo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6)
    assert averageTo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)
    assert averageTo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -10)
    assert averageTo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11)
    assert averageTo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'a')
    assert averageTo([1, 2, 3, 'hello', 5, 6, 7, 8, 9, 10], 6)

