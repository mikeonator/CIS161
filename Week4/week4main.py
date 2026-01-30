# Michael Audi - CIS161 Week 4 Main Assignment

## Step 1
def avg_three(num1,num2,num3):
    return ((num1 + num2 + num3)/3)

## Step 2
### CANNOT MOVE THE PRINT STATEMENTS BEFORE
### FUNCTION DEFINITION BECAUSE THE PYTHON
### INTERPRETER GOES LINE BY LINE AND
### WOULDN'T KNOW WHAT avg_three() IS YET
print (avg_three(7, 5, 9))
print (avg_three(6, 6, 7))

## Step 3
### print(num1) would not work because
### the variable num1 is defined within
### the scope of avg_three not global
try:
    print(num1)
except NameError:
    print("NameError: name 'num1' is not defined")