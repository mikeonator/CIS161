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

if __name__ == "__main__":
    main()