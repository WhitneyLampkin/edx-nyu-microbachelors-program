"""
Description

Modify your earlier BMI Metric program to round to two decimal positions and also display the CDC standard weight status categories:

The CDC standard weight status categories are:

BMI/Weight Status
Below 18.5/Underweight
18.5-24.9/Normal
25.0-29.9/Overweight
30.0 and above/Obese

For example,  an  execution could look  like  this:
Please enter weight in kilograms: 50
Please enter height in meters: 1.58
BMI is: 20.03, Status is Normal

File Name 

bmimetric2.py

Score

There are five tests each worth 2 points
"""

## Get user inputs 
weight = int(input("Please enter weight in kilograms: "))
height = float(input("Please enter height in meters: "))
heightSquared = height*height

status = "Unknown"

## Calculate
bmi = (weight if weight > 0 else 0)/(heightSquared if heightSquared > 0 else 1)
bmi = float(round(bmi, 2))

## Determine Status

if(bmi < 18.5):
    status = "Underweight"
if(18.5 < bmi < 24.9):
    status = "Normal"
if(25.0 < bmi < 29.9):
    status = "Overweight"
if(bmi > 30.0):
    status = "Obese"

## Result
print('BMI is: ', bmi, ", Status is ", status, sep="")