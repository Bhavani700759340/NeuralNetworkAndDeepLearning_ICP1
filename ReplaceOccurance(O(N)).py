'''Write a program that accepts a sentence and replace each occurrence of
‘python’ with ‘pythons’.
•
Sample input:
•I love playing with python
•
Sample output:
•I love playing with pythons'''
inputString = input("Enter the string: ")

# replace 'python' with 'pythons'
finalString = []
i = 0
while i < len(inputString):
    if i + 5 <= len(inputString) and inputString[i:i+6].lower() == 'python':
        finalString.append('pythons')
        i += 6
    else:
        finalString.append(inputString[i])
        i += 1

s1= ''.join(finalString)
print("String changed as per requirement:", s1)