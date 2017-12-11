# CTI 110
# M5HW2 Running Total
# Jeffrey Lee
# 17 Oct 2017

#Write a program that asks the user to enter a series of numbers.
#It should loop, adding these numbers to a running total
#until the user enters a negative number
#When a negative number is entered, the program should exit the loop

total = 0
userNumber = float( input( "Please enter the first number or a negative " + \
                           "negative number to quit: " ) )
                    
while userNumber > -1:
    total = total + userNumber
    userNumber = float( input( "Please enter the next number or a " + \
                               "negative number to quit: " ) )
print()
print( "The sum of all numbers you entered is",total )
