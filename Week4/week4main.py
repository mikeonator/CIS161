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

## Step 5

def car_value(purchase_price, years, car_type):
    if car_type == "German":
        return purchase_price * (.95 ** years)
    elif car_type == "Japanese":
        return purchase_price * (.93 ** years)
    elif car_type == "Italian":
        return purchase_price * (1.05 ** years)
    else:
        print("Invalid car type")
        return 0.0

car_type = input("What type of car is it (German/Japanese/Italian)? ")
purchase_price = float(input("What is the purchase price? "))
years = int(input("How many years? "))
value = car_value(purchase_price, years, car_type)
print(f"The value of {car_type} car will be ${value:.2f} after {years} years.")

## Step 6

def dog_years_to_human_years(dog_years: float) -> float:
    # Matches sample output: 3 dog years -> 22.3 human years
    return (dog_years * 7.4) + 0.1

print("Dog’s Age calculator:")
dog_name = input("What is your dog’s name? ")
dog_years = float(input(f"How old is {dog_name}? "))
human_years = dog_years_to_human_years(dog_years)
print(f"Your {dog_name} is {human_years:.1f} human years old")

## Step 7

def ice_cream_cone_price(num_scoops: int) -> float:
    return (num_scoops * 1.15) + 2.25

print("Ice cream cone price calculator:")
scoops = int(input("How many scoops would you like? "))
print(f"A {scoops}-scoop cone will cost ${ice_cream_cone_price(scoops):.2f}")
