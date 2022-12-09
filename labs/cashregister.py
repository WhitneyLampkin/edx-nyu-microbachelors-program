"""
Description

Write a program that computes how much a customer has to pay after purchasing two items. Make the lower-priced item half price. If the two items have identical prices, you can make one or the other half price.

The price is calculated according to the following rules:
• Buy one get one half off promotion: the lower price item is half price.
• If the customer is club card member, additional 10% off.
• Tax is added.


Inputs to the program include:
• Two items' prices
• Have club card or not (User enters 'Y' or 'y' for “yes”; 'N' or 'n' for “no”)
• Tax rate (User enters the percentage as a number; for example, they enter
8.25 if the tax rate is 8.25%)


Program displays:
• Base price - the price before the discounts and taxes
• Price after discounts - the price after the buy one get one half off promotion
and the member's discount, if applicable
• Total price - the amount of money the customer has to pay (after tax)
printed with the precision of 2 decimal digits.


Hint: In order to print a number in a specific precision, you can use the round
function passing 2 arguments to it. Use help(round) to get a brief explanation of
this function, and try playing with it, to better understand what it does.
To format to two decimal places you can use the string format function with the format of 2.2f.

For example, an execution could look like this:

Enter price of the first item: 10
Enter price of the second item: 20
Does customer have a club card? (Y/N): y
Enter tax rate, e.g. 5.5 for 5.5% tax: 8.25
Base price = 30.00
Price after discounts = 22.50
Total price = 24.36


File Name 
cashregister.py

Score

There are five tests each worth 2 points
"""

## Get user inputs
item1 = float(input("Enter price of the first item: "))
item2 = float(input("Enter price of the second item: "))
hasClubCard = input("Does customer have a club card? (Y/N): ")
taxRate = float(input("Enter tax rate, e.g. 5.5 for 5.5% tax: "))

## Other Variables
discountedPrice = float(0)
totalPrice = float(0)

## Calculate
basePrice = item1 + item2

if(item1 < item2):
    discountedPrice = (item1 / 2) + item2
else:
    discountedPrice = (item2 / 2) + item1

if(hasClubCard == "Y" or hasClubCard == "y"):
    discountedPrice = discountedPrice - (discountedPrice*.1)

totalPrice = (discountedPrice*taxRate*.01) + discountedPrice

## Display Results
print("Base price =", "{:.2f}".format(basePrice))
print("Price after discounts =", "{:.2f}".format(discountedPrice))
print("Total price =", "{:.2f}".format(totalPrice))