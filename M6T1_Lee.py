#CTI 110
#M6T1 Kilometer Converter
#Jeffrey Lee
# Oct 24 2017

#Write a program that asks the user to enter a distance in kilometers
#then converts that distance to miles
#the conversion formula:Miles = Kilometers * 0.6214
#create two functions for this program
#main() function
#show_miles()function that takes km as a parameter
#converts to miles, and prints the answer
CONVERSION_FACTOR = 0.6214

def main():
    kilometers = float(input('Enter distance in kilometers: '))
    show_miles(kilometers)

def show_miles(km):
    miles = km * CONVERSION_FACTOR

    print(km, 'kilometers equals', miles, 'miles.')

main()
    

