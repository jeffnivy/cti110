#CTI 110
#M5HW1 distance traveled
#Jeffrey Lee
#11 oct 2017

#Write a program that asks the user two questions
#The speed of a vehicle, and the number of hours it has traveled
#The program should then display the distance that the vehicle has traveled for each hour of that time period
#Hour		Distance Traveled
#1                   40
#2                   80
#3                   120

#program uses a counting loop

vehicleSpeed = float( input("What is the speed of the vehicle:"))
timeTraveled = int( input("How many hours has it traveled?:"))

print


print ( "Hour" '\t' "Distance Traveled" )
for currentHour in range( 1,timeTraveled + 1):
    distanceTraveled = vehicleSpeed * currentHour
    print currentHour,'\t',  distanceTraveled 
    
