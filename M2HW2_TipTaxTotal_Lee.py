#CTI-110
#M2HW2- Tip Tax Total
#Jeffrey Lee
#9Sept2017

#Write a program that calculates the total amount of a meal purchased at a restaurant
#The program should ask the user to enter the charge for the food
#Then calculate the amount of a 18% tip and &% sales tax
#Display each of these amounts and the total

foodCost = float( input( "Enter the charge of the food: " ) )

tipAmount = 0.18 * foodCost

salesTax = 0.07 * foodCost

total = foodCost + tipAmount + salesTax

print( "Food Cost: $" + format( foodCost, ",.2f"), "tipAmount: $" +\
       format( tipAmount, ",.2f") ),  "Sale Tax: $" + format( salesTax, ",.2f"),\
        "total: $" + format( total, ",.2f")
