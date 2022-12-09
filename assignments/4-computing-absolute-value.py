## Get user input
print("Please enter an integer:")
user_input = int(input())

abs_value = user_input

## Calculate Abs Value
if(user_input < 0):
    abs_value = user_input * (-1)

## Display Abs Value
## Note: sep="" overrides the default space separator for print()
print("|", user_input, "| = ", abs_value, sep="")