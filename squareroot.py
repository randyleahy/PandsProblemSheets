#Uses the Newton Method to derive an estimated square root of a number
#Author Chris Foley

#Defines Newton method for number and sets numebr of iterations of method to be used
def sqrt(number, number_iters = 500):
    
    #Number we're trying to get the root of and our guess at the root
    a = float(number) 
    
    for i in range(number_iters): 
        #Specifys the method to be repeated
        number = 0.5 * (number + a / number)
    #returns the refined esitmate
    return number

#Applys the method to number placed in the brackets
print(sqrt())


