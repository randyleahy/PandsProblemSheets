#Reads a textfile from the commandline and counts occurences of letters
#Author Chris Foley

from itertools import count
from posixpath import split
import string
import sys


def letterFrequency(fileName, letter):
    # open file in read mode
    file = open(fileName, 'r')
 
    # store content of the file in a variable
    text = file.read()
 
    # using count()
    return text.count(letter)
 
 
# call the function and display the letter count
print(letterFrequency('test.txt', 'e'))