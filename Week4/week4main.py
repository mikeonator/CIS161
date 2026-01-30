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


## Step 4

def dog_age(dog_years):
    return (24 + (dog_years - 2) * 4)

input1 = 5
input2 = 11
print(f"{input1} dog years is equivalent to {dog_age(input1)} human years.")
print(f"{input2} dog years is equivalent to {dog_age(input2)} human years.")

