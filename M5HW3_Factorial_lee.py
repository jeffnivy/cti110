#CTI 110
#M5HW3 Factorial
#Jeffrey Lee
#17 Oct 2017

#Write a program that asks the user for a nonnegative integer
#then uses a loop to calculate the factorial of that number
#Display the factorial

userInteger = int( input( "Please enter a number: " ) )

while userInteger < 1:
    userInteger = int( input( "Please enter a positive number please: " ) )

factorial = 1

for currentNumber in range( 1, userInteger + 1 ):
    factorial = factorial * currentNumber

print( "The factorial of", userInteger, "is" , factorial )
