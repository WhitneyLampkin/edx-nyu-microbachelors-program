"""
Description

Write a function that is given a phrase and returns the first word in that phrase.
For example, given ‘the quick brown fox’, your function should return ‘the’.

Here is an example call to the function

print(firstword(“the quick brown fox”)):

File Name 

firstword.py

Score

There are three tests each worth 2 points

Note: You do not need any other code including the main method or any print statements. ONLY the firstword method is required. Otherwise, the autograder will fail and be unable to grade your code. (I.e., do not include the above example in your code.) The above example should be used be test your code but deleted or comment out upon submission.
"""

def firstword(phrase):
    phrase.strip()
    str_array = phrase.split(" ")
    new_string = ''.join(str_array[0])
    return new_string

print(firstword("the quick brown fox"))