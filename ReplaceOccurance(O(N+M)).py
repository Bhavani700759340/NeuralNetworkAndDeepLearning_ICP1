'''Write a program that accepts a sentence and replace each occurrence of ‘python’ with ‘pythons’.
•
Sample input:
•I love playing with python
•
Sample output:
•I love playing with pythons
'''
#HERE SPACE AND TIME COMPLEXITY - O(N+M)
inputString = input("Enter the Statement : ")

inputString = inputString.replace("python","pythons")

print(inputString)