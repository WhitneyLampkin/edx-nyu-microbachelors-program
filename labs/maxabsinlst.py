"""
Description

Implement function max_abs_val(lst), which returns the maximum absolute
value of the elements in list.
For example, given a list lst: [-19, -3, 20, -1, 0, -25], the function
should return 25.


The name of the method should be max_abs_val and the method should take one parameter which is the list of values to test.  Here is an example call to the function

print(max_abs_val([-19, -3, 20, -1, 0, -25]))

File Name 

maxabsinlst.py

Score

There are three tests each worth 2 points


Note: You do not need any other code including the main method or any print statements. ONLY the max_abs_val method is required. Otherwise, the autograder will fail and be unable to grade your code. (I.e., do not include the above example in your code.) The above example should be used be test your code but deleted or comment out upon submission.
"""

def max_abs_val(list):
    maxAbsValue = list[0]
    for item in list:
        itemAbsValue = item
        if item < 0:
            itemAbsValue = item * -1
        if itemAbsValue > maxAbsValue:
            maxAbsValue = itemAbsValue
    return maxAbsValue

##print(max_abs_val([-19, -3, 20, -1, 5, -25]))