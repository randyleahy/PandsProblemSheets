#Calculates BMI
#Author Chris Foley

from sympy import RealNumber

#takes input of weight in kilos and height in meters
a = RealNumber(input('Enter your weight (KG)'))
b = RealNumber(input('Enter your height(M)'))

#Height squared
b1 = b*2

#Caluclates BMI as W/H(squared)
Newnumber = (a / b1)

#Defines BMI as result of above calculation
BMI = Newnumber 

#Prints the result
print('Your BMI is {}'.format(BMI))