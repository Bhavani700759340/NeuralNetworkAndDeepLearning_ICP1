'''Problem Statement : Write a python program for the following:
– Input the string “Python” as a list of characters from console, delete at least 2 characters, reverse the
resultant string and print it.
Sample input:
•python
•
Sample output:
•ntyp
'''
#reading input from console
inputString = input("Enter a string : ")

#reading no of characters to delete
n = int(input("Enter no of characters to delete but not below 2 : "))

#slicing inputString[start:stop]
if(n>=2):
    inputString = inputString[:len(inputString)-n]

#reversing the string
inputString = inputString[::-1]

print(inputString)