# Michael Audi - CIS161 Week 4 Main Assignment

import cream_history as creamy

# Step 1


def avg_three(num1, num2, num3):
    '''
    This function takes three numbers as arguments and returns their average.
    '''
    return ((num1 + num2 + num3)/3)


# Step 2
print("---- Step 1 & 2 ----")
# cannot move the print(avg_three()) statements before
# function definition because the python interpreter
# goes line by line and wouldn't know what avg_three() is yet
print(avg_three(7, 5, 9))
print(avg_three(6, 6, 7))

# Step 3
# print(num1) would not work because
# the variable num1 is defined within
# the scope of avg_three not global
print("\n---- Step 3 ----")
try:
    print(num1)
except NameError:
    print("NameError: name 'num1' is not defined")


# Step 4
print("\n---- Step 4 ----")


def dog_age(dog_years: int):
    '''
    This function takes an integer as an argument and returns the equivalent human years.
    '''
    return (24 + (dog_years - 2) * 4)


input1 = 5
input2 = 11
print(f"{input1} dog years is equivalent to {dog_age(input1)} human years.")
print(f"{input2} dog years is equivalent to {dog_age(input2)} human years.")

# Step 5
print("\n---- Step 5 ----")


def car_query(purchase_price=None, years=None, car_type=None):
    '''
    This function takes three arguments (with input prompts as default) and returns the purchase price, years, and car type.
    '''
    if purchase_price is None:
        purchase_price = float(input("What is the purchase price? "))
    if years is None:
        years = int(input("How many years since release? "))
    if car_type is None:
        car_type = input("What type of car is it (German/Japanese/Italian)? ")
    return purchase_price, years, car_type


def car_value(purchase_price, years, car_type):
    '''
    This function takes three arguments and returns the value of the car based on the purchase price, years, and car type.
    '''
    if car_type == "German":
        return purchase_price * (.95 ** years)
    elif car_type == "Japanese":
        return purchase_price * (.93 ** years)
    elif car_type == "Italian":
        return purchase_price * (1.05 ** years)
    else:
        print("Invalid car type")
        return 0.0


ferrari = car_query(88000, 38, "Italian")
print(
    f"The value of an {ferrari[2]} 1988 Ferrari 328 GTS should be ${car_value(*ferrari):.2f} after {ferrari[1]} years.")
toyota = car_query(25280, 34, "Japanese")
print(
    f"The value of an {toyota[2]} 1992 Toyota Supra should be ${car_value(*toyota):.2f} after {toyota[1]} years.")
mercedes = car_query(48595, 26, "German")
print(
    f"The value of an {mercedes[2]} 2000 Mercedes-Benz E320 Wagon should be ${car_value(*mercedes):.2f} after {mercedes[1]} years.")
tesla = car_query(53000, 8, "American")
print(
    f"The value of an {tesla[2]} 2018 Tesla Model 3 Long Range AWD should be ${car_value(*tesla):.2f} after {tesla[1]} years.")
usercar = car_query()
print(
    f"The value of an {usercar[2]} car will be ${car_value(*usercar):.2f} after {usercar[1]} years.")

# Step 6
print("\n---- Step 6 ----")

print("Dog’s Age calculator:")
dog_name = input("What is your dog’s name? ")
dog_years = int(input(f"How old is {dog_name}? "))
print(f"Your {dog_name} is {dog_age(dog_years)} human years old")

# Step 7
print("\n---- Step 7 ----")


def ice_cream_cone_price(num_scoops: int) -> float:
    '''
    This function takes an integer as an argument and returns the price of the ice cream cone.
    '''
    return (num_scoops * 1.15) + 2.25


print("Ice cream cone price calculator:")
scoops = int(input("How many scoops would you like? "))
print(f"A {scoops}-scoop cone will cost ${ice_cream_cone_price(scoops):.2f}")

# Step 7 - Extra Credit
print("\n---- Step 7 - Extra Credit ----")

print("Calculate Price of 1/2 Gallon of Ice Cream based on month and year (1984 to 2025)")

yearin = int(input("What Year? "))
monthin = int(input("What Month (as a number)? "))

priceout = creamy.get_prices(monthin, yearin)

print(f"The price of ice cream on {yearin}-{monthin}-01 was ${priceout}")
