#Write a program using a value-returning function for this assignment
#Note how this differs from M6T1, which uses a void function
#25 Oct 2017
#CTI 110 M6T2_feetToInches
#Jeffrey Lee
#

#Write a program that asks the user to enter a distance in feet
#and prints that same distance in inches
#Inches = Feet * 12
#You should create two functions for this program
#main() function that calls the next function and prints the answer
#feet_to_inches()function that asks the user to enter a distance in feet
#calculates the distance in inches
#returns that value

INCHES_PER_FOOT = 12

def main():
    feet = int(input('Enter number of feet: '))

    print(feet, 'equals', feet_to_inches(feet), 'inches.')

def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

main()
