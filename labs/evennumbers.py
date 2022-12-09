"""
Description

Write a program that reads a positive integer n, and prints the first
n even numbers.

For example, one execution would look like this:
Please enter a positive integer: 3
2
4
6

File Name 

evennumbers.py

Score

There are three tests each worth 2 points
"""

print("Please enter a positive integer: ")
n = int(input())

for i in range(1, n+1):
    print(i*2)