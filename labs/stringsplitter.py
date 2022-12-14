"""
Description

Read from the user a string containing 
odd number of characters. Your program should: 
a) Print the middle character. 
b) Print the string up to but not including the middle character (i.e., the first half 
of the string). 
c) Print the string from the middle character to the end (not including the 
middle character). 

Sample output: 
Enter an odd length string: Fortune favors the bold
Middle character: o
First half: Fortune fav
Second half: rs the bold

File Name 

stringsplitter.py

Score

There are five tests each worth 2 points
"""

user_input = input("Enter an odd length string: ")
str_length = len(user_input)
middleIndex = str_length//2

## Find middle character
middleCharacter = user_input[middleIndex:(middleIndex+1)]

## Find first half
firstHalf = user_input[:middleIndex]

## Find second half
secondHalf = user_input[(middleIndex+1):]

## Display Results
print("Middle character:", middleCharacter)
print("First half:", firstHalf)
print("Second half:", secondHalf)