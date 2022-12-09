"""
Write a program that reads a positive integer, n, and prints a n line right triangle, aligned to the left, filled with "*" symbols.
"""

print("Please enter a positive integer: ")
n = int(input())

for i in range(1, n+1):
    line = i*"*"
    print(line)