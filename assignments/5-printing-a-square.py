"""
Write a program that reads a positive integer, n, and prints a n*n square, filled with '*' symbols.
"""

print("Please enter a positive integer: ")
user_input = int(input())
counter = 1

while counter <= user_input:
    for i in range(user_input):
        print(user_input*"*")
    break


