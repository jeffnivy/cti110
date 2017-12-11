#CTI 110
#M3HW1- AgeClassifier
#Jeffrey Lee
#13 Sept 2017

#Write a program that asks the user to enter a person’s age.
#The person should display a message whether the person is an infant,child,teenager or adult.
#If the person is 1 year old or less, he or she is an infant.
#If the person is older than one year, but younger than 13 years, he or she is a child.
#If the person is at least 13 years old, but less than 20 years old, he or she is a teenager.
#If the person is at least 20 years old, he or she is an adult.

Age = int( input( "Please enter your age: " ))

if Age <= 1:
    print( "You are an infant" )
elif Age < 13:
    print( "You are a child" )
elif Age < 20:
    print( "You are a teenager" )
elif Age >= 20:
    print( "You are an adult" )
