# CTI 110
# M3LAB
# Lee
# 13 Sept 2017



# This program takes a number grade and outputs a letter grade.

 # system uses 10-point grading scale  
A_score = 90-100
B_score = 80
C_score = 70
D_score = 60
F_score = 0-50
# TO DO: define the rest of the scores
# TO DO: finish this
# Program start

grade = float(input("Enter the grade "))
if grade > 0 and grade < 50:
    print("F")
elif grade > 50 and grade <=60:
    print("D")
elif grade > 60 and grade <=70:
    print("C")
elif grade > 70 and grade <=80:
    print("B")
elif grade > 80 and grade <=90:
    print("A")
elif grade > 90 and grade <=100:
    print("A")
else:
    print("Grades are between 0 and 100")
    









