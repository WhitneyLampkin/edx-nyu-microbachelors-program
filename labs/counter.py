"""
Lab 2 - Coin Counter Lab

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

"""Get user inputs"""
print("Please enter the number of coins:")
quarters = int(input("# of quarters: "))
dimes = int(input("# of dimes: "))
nickels = int(input("# of nickels: "))
pennies = int(input("# of pennies: "))


"""Calculate dollars & cents"""
total = ((quarters if quarters > 0 else 0) * 25) + ((dimes if dimes > 0 else 0) * 10) + ((nickels if nickels > 0 else 0) * 5) + ((pennies if pennies > 0 else 0) * 1)
dollars = total // 100
cents = total % 100

"""Print results"""
print('The total is', dollars, 'dollars and', cents, 'cents')
