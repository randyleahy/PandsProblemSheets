#Outputs if day is a weekday or not
#Author Chris Foley 



# Import Module
import datetime

# To Get the Week Number
weekNumber = datetime.datetime.today().weekday()

#Checks if less than 5 days have passed in the week
if weekNumber < 5:
    #if no
    print("Yes, unfortunately today is a weekday.")
else:
    #if yes
    print ("It is the weekend, yay!")





  

       