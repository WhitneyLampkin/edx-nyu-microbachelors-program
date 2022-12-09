"""
Description

Fibonacci number is a series of numbers in which each number is the sum of the two preceding numbers. The first two numbers in the series are the number 1.  Write a program to print first n Fibonacci Numbers

For example, one execution would look like this:
Please enter a positive integer greater than 1: 4
1
1
2

3

File Name 

fibonacci.py

Score

There are five tests each worth 2 points
"""

print("Please enter a positive integer greater than 1: ")
n = int(input())

first_num = 1
second_num = 1

count = 2

print(first_num)
print(second_num)

while(count < n):
    sum = first_num + second_num
    print(sum)
    first_num = second_num
    second_num = sum
    count += 1
