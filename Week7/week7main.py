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

def teepee_sort(num_list):
    evens = []
    odds = []
    listout = []
    for value in num_list:
        if value % 2 == 0:
            evens.append(value)
        else:
            odds.append(value)
    return sorted(odds) + sorted(evens, reverse=True)

def next_highest_number_iterative_only(x:int):
    if x < 10:
        return None
    initlist = list(map(int,str(x)))   
    pivot_index = -1
    swap_index = -1

    for i in range(len(initlist) - 2, -1, -1):
        if initlist[i] < initlist[i+1]:
            pivot_index = i
            break
    if pivot_index == -1:
        return None
    for j in range(len(initlist) - 1, pivot_index, -1):
        if initlist[j] > initlist[pivot_index]:
            swap_index = j
            break
    initlist[pivot_index], initlist[swap_index] = initlist[swap_index], initlist[pivot_index]
    initlist[pivot_index+1:] = initlist[pivot_index+1:][::-1]

    return int("".join(map(str,initlist)))

def find_pivot(initlist, x):
    if x < 0:
        return None
    if initlist[x] < initlist[x+1]:
        return x
    else:
        return find_pivot(initlist,x-1)

def reverse_end(initlist, left, right):
    # list, pivot+1, len(list)-1
    if left >= right:
        return
    initlist[left], initlist[right] = initlist[right], initlist[left]
    return reverse_end(initlist, left+1, right-1)

def next_highest_number_w_recurse(x:int):
    if x < 10:
        return None
    swap_index = -1
    initlist = list(map(int, str(x)))
    pivot_index = find_pivot(initlist, len(initlist)-2)

    if pivot_index == None:
        return None
    for j in range(len(initlist) - 1, pivot_index, -1):
        if initlist[j] > initlist[pivot_index]:
            swap_index = j
            break
    initlist[pivot_index], initlist[swap_index] = initlist[swap_index], initlist[pivot_index]
    reverse_end(initlist, pivot_index+1,len(initlist)-1)
    return int("".join(map(str,initlist)))

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
    print("Recursive function that will print all occurrences of the squares of all integers from 1 to input")
    in4int = int(input("Enter a positive integer: "))
    recurse_int_squares(in4int)

    print("\n----- Step 5 -----")
    print("Sorting function that will create a teepee of the numbers with the largest in the center")
    in5list = list(map(int ,input("Enter integers separated by spaces (try and make an even teepee!): ").split()))
    if len(in5list) == 0:
        in5list = [12, 43, 22, 34, 2, 21, 3, 33, 81]
    print(f"The Sorted List is as follows: {teepee_sort(in5list)}")

    print("\n----- Step 6 -----")
    print("Rearranging digits so that the new arrangement represents the next larger value that can be represented by " \
    "these digits (or reports that no such rearrangement exists if no rearrangement produces a larger value).")
    in6int = int(input("Enter an integer (big one): "))
    if len(str(in6int)) == 0:
        in6int = 5647382901
    out6listiterative = next_highest_number_iterative_only(in6int)
    out6listrecursive = next_highest_number_w_recurse(in6int)
    if out6listiterative == None or out6listrecursive == None:
        print(f"No rearrangement of {str(in6int)} is possible.")
    else:
        print(f"The iteratively rearranged list is as follows: {out6listiterative}")
        print(f"The recursively rearranged list is as follows: {out6listrecursive}")

if __name__ == "__main__":
    main()