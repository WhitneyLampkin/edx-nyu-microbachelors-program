"""
Description

Write a program that  reads a character (string of  length  1)  from  the 
user, and classifies it to  one of the following: lower case letter, upper case letter, 
digit,  or non-alphanumeric character 

Sample  output (4 different executions):  
Enter a character: j
j is  a lower case  letter.
Enter a character: 7
7 is  a digit.
Enter a character: ^
^ is  a non-alphanumeric  character.
Enter a character: C
C is  an  upper case  letter.

File Name 

chartype.py

Score

There are five tests each worth 2 points
"""

user_input = input("Enter a character: ")

if(user_input.islower()):
    print(user_input, "is a lower case letter.")
elif(user_input.isdigit()):
    print(user_input, "is a digit.")
elif(user_input.isalnum() == False):
    print(user_input, "is a non-alphanumeric character.")
elif(user_input.isupper()):
    print(user_input, "is an upper case letter.")
