# Michael Audi - CIS161 Week 7 Main Assignment

import math

def print_even_range(x:int,y:int):
    listout = []
    while x < y:
        if x % 2 == 0:
            listout.append(x)
        x += 1
    return listout

def factor_pos_int(x:int):
    setout = set()
    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            setout.add(i)
            setout.add(x // i)
    return sorted(setout)

def numeric_name_value(name:str):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    sum = 0
    for char in name.lower():
        for index, value in enumerate(alphabet):
            if char == value:
                sum += index
    return sum

def recurse_int_squares(x:int):
    if x == 0:
        return
    else:
        recurse_int_squares(x-1)
        print(x**2)    

def main():

    print("----- Step 1 -----")
    print("Printing even numbers within input range")
    in1Low = int(input("Enter the Lower Bound: "))
    in1Up = int(input("Enter the Upper Bound: "))
    print(f"The even numbers between {in1Low} and {in1Up} are: {print_even_range(in1Low,in1Up)}")
    
    print("\n----- Step 2 -----")
    print("Printing all factors of a given positive integer")
    in2 = int(input("Enter an integer: "))
    print(f"The integers that are factors of {in2} are: {factor_pos_int(in2)}")

    print("\n----- Step 3 -----")
    print("Printing the numerical sum of a given name based on a 0-25 value assignment to the alphabet")
    in3name = input("Enter your last name: ")
    print(f"The numerical sum corresponding to the name {in3name} is: {numeric_name_value(in3name)}")

    print("\n----- Step 4 -----")
    print("Write recursive function that will print all occurrences of the squares of all integers from 1 to input")
    in4int = int(input("Enter a positive integer: "))
    recurse_int_squares(in4int)

if __name__ == "__main__":
    main()