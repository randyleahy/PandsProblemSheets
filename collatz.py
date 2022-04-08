#Asks user for a positive integer and outputs a collatz sequence
#Author Chris Foley

#Asks user for number
col = (int(input('Enter a positive integer ')))

#Definition of collatz
def collatz(n):

#specifies termination condition n = 1
    while n!=1:

        #Prints n and spaces result
        print(n, end = ' ,')

        #specifies what to do with odd number
        if n % 2 != 0: 
            n = 3*n + 1

        #specifies what to do with even number
        else:
            n = n // 2

        print(n)

#Sets user input as collatz seed number
collatz(col)