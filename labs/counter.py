"""
Write a program that asks the user to enter a number of quarters, dimes, nickels and pennies
and then outputs the monetary value of the coins in the format of dollars and remaining cents.
Your program should interact with the user exactly as it shows in the following example:


Please enter the number of coins:
# of quarters: 20
# of dimes: 4
# of nickels: 13
# of pennies: 17
The total is 6 dollars and 22 cents
"""

print('Please enter the number of coins:')
quarters = int(input('# of quarters: '))
dimes = int(input('# of dimes: '))
nickels = int(input('# of nickels: '))
pennies = int(input('# of pennies '))

total = 0

dollars = 0
cents = 0

print('The total is ', dollars, 'dollars and ', cents, 'cents.')
