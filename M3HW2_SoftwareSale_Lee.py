#CTI 110
#M3HW2- SoftwareSales
#Jeffrey Lee
# 13 Sept 2017

#A software company sells a package that retails for $99.
#They offer bulk discounts for volume purchases.
#Bulk discounts are given according to the following table:

#Quantity     Discount
#10-19         10%
#20-49         20%
#50-99         30%
#100 or more   40%

#Write a program that asks the user to enter the number of packages purchased
#The program should then display the amount of the dicount (if any) and the
#total amount of the purchase after the discount

NumberOfPackages = int( input( "Enter the number of packages bought: " ) )

packagePrice = 99

if NumberOfPackages < 10:
    discount = 0
elif NumberOfPackages < 20:
    discount = 0.10
elif NumberOfPackages < 50:
    discount = 0.20
elif NumberOfPackages < 100:
    discount = 0.30
else:
    discount = 0.40

subTotal = NumberOfPackages * packagePrice
discountAmount = discount * subTotal
total = subTotal - discountAmount

print( "Amount of discount: $" + format( discountAmount, ",.2f" ) ) + \
       "\nTotal amount: $" + format( total, ",.2f" )  

