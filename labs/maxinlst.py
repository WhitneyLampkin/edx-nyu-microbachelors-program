"""
Description

Implement function max_val(lst), which returns the maximum value of the elements in list.
For example, given a list lst: [-19, -3, 20, -1, 5, -25], the function
should return 20.


The name of the method should be max_val and the method should take one parameter which is the list of values to test.  Here is an example call to the function

print(max_val([-19, -3, 20, -1, 5, -25]))

File Name 

maxinlst.py

Score

There are three tests each worth 2 points

Note: You do not need any other code including the main method or any print statements. ONLY the max_val method is required. Otherwise, the autograder will fail and be unable to grade your code. (I.e., do not include the above example in your code.) The above example should be used be test your code but deleted or comment out upon submission.
"""

def max_val(list):
    maxValue = list[0]
    for item in list:
        if item > maxValue:
            maxValue = item
    return maxValue

##print(max_val([-19, -3, 20, -1, 5, -25]))