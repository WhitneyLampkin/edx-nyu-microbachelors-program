"""
Write a program that reads a positive integer, n, and prints the numbers from 1 up to n.
"""

print("Please enter a positive integer:")
input_num = int(input())
counter = 1

print("Printing counter...")

while(counter <= input_num):
    print(counter)
    counter=counter+1

for number in range(1, input_num+1):
    print("The number is: ", number)

names = ["Susie", "Larry", "Mark"]

for name in names:
    print("The name is:", name)