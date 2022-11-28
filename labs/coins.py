"""
Description
Write a program that asks the user to enter an amount of money in the format of dollars and remaining cents.  The program should calculate and print the minimum number of coins (quarters, dimes, nickels and pennies) that are equivalent to the given amount.
Hint: In order to find the minimum number of coins, first find the maximum number of quarters that fit in the given amount of money, then find the maximum number of dimes that fit in the remaining amount, and so on.

File Name 
coins.py

Score
There are five tests each worth 2 points.
For example,  an  execution should look  like  this:
Please enter the amount of money to convert:

# of dollars: 2
# of cents: 37
The coins are 9 quarters, 1 dimes, 0 nickels and 2 pennies
"""

print("Please enter the amount of money to convert:")

dollars = int(input("# of dollars: "))
cents = int(input("# of cents: "))

total = ((dollars if dollars > 0 else 0) * 100) + (cents if cents > 0 else 0)

quarters = total // 25
total = total - (quarters*25)

dimes = total // 10
total = total - (dimes*10)

nickels = total // 5
total = total - (nickels*5)

pennies = total // 1

print('The coins are', quarters, 'quarters,', dimes, 'dimes,', nickels, 'nickels and', pennies, 'pennies')