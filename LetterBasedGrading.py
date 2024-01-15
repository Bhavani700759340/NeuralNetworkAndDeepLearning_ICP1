'''Use the if statement conditions to write a program to
print the letter grade based on an input class score.
Use the grading scheme we are using in this class.'''

'''Grading Scale
Percent (%) Grade
90 100 A
80 89 B
70 79 C
60 69 D
0 60 F'''

inputNum = int(input("Enter the number : "))
if(inputNum>=90 and inputNum<=100):
    print("Grade is A")
elif(inputNum>=80 and inputNum<=89):
    print("Grade is B")
elif(inputNum>=70 and inputNum<=79):
    print("Grade is C")
elif(inputNum>=60 and inputNum<=69):
    print("Grade is D")
else:
    print("Grade is F")