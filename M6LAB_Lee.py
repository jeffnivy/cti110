#CTI 110
#M6Lab Age and name
#Jeffrey Lee
#1 Nov 2017

#Write a program that will ask the user their name and then ask their age.
#The program should then greet them by name, and tell them their age
#infant, child, teenager, or adult
#main() which is a void function
#greet(name) which is a void function
#ageCategory(age) which returns a string


    
name = input("what is your name? ")
Age = int( input( "Please enter your age: " ))

def hello():
    print('Hello!')
hello()
def print_welcome(name):
    print('Welcome', name)
    
print_welcome(name)
print("Nice to meet you")

if Age <= 1:
    print( "You are an infant" )
elif Age < 13:
    print( "You are a child" )
elif Age < 20:
    print( "You are a teenager" )
elif Age >= 20:
    print( "You are an adult" )

