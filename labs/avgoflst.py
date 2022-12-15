"""
Description

Implement function avg_val(lst), which returns the average
value of the elements in list.
For example, given a list lst: [19, 2, 20, 1, 0, 18], the function
should return 10.


The name of the method should be avg_val and the method should take one parameter which is the list of values to test.  Here is an example call to the function

print(avg_val([19, 2, 20, 1, 0, 18]))

File Name 

avgoflst.py

Score

There are three tests each worth 2 points

Note: You do not need any other code including the main method or any print statements. ONLY the max_val method is required. Otherwise, the autograder will fail and be unable to grade your code. (I.e., do not include the above example in your code.) The above example should be used be test your code but deleted or comment out upon submission.
"""

def avg_val(list):
    total = 0
    length = len(list)
    for item in list:
        total = total + item
    avgValue = total/length
    return avgValue

##print(avg_val([19, 2, 20, 1, 0, 18]))