"""
Write a program that reads from the user the number of days they traveled.

The program will then print their traveling time in the format of full weeks and additional days.
"""

print('Please enter number of days you traveled:')
days_traveled = int(input())
weeks = days_traveled//7
days = days_traveled%7
print('You traveled', weeks, 'weeks and', days, 'days!')
