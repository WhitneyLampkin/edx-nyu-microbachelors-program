"""
Description

Write a function that is given a phrase and returns the phrase we get if we take  
out the first word from the input phrase.
For example, given ‘the quick brown fox’, your function should return ‘quick brown fox’


Here is an example call to the function

print(remainingwords(“the quick brown fox”)):

File Name 

remaining.py

Score

There are three tests each worth 2 points

Note: You do not need any other code including the main method or any print statements. ONLY the remainingwords method is required. Otherwise, the autograder will fail and be unable to grade your code. (I.e., do not include the above example in your code.) The above example should be used be test your code but deleted or comment out upon submission.
"""

def remainingwords(phrase):
    phrase.strip()
    str_array = phrase.split(" ")
    str_array.pop(0)
    new_string = ' '.join(str_array)
    return new_string

##print(remainingwords("the quick brown fox"))