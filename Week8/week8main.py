# Michael Audi - CIS161 Week 8 Main Assignment

from math import factorial as vroom
import time

def stop_shouting():
    '''
    if the second userinput is the all uppercase version of the first,
    chastise them. if it isnt, chastise them. No mercy.
    '''
    firstin = input("Enter a phrase: ")
    secondin = input("Enter the same phrase but louder: ")
    if firstin.upper() == secondin:
        return ("Stop shouting please!")
    else:
        return ("You didn't do as you were asked... sigh.")

def vowel_check(x:str):
    '''
    calculates the total number of vowels
    in the given string
    '''
    vowels = ['a','e','i','o','u']
    count = 0
    for char in x:
        for vowel in vowels:
            if char.lower() == vowel:
                count += 1
                break
    return count

def vowel_ask():
    '''
    ask the user for a string to count the vowels of.
    uses vowel_check() to do so.
    prints the results.
    '''
    string = input("Enter a string: ")
    count = vowel_check(string)
    if count == 0:
        return f"There are no vowels in the string {string}"
    elif count == 1:
        return (f"There is {count} vowel in the string {string}.")
    else:
        return (f"There are {count} vowels in the string {string}.")

def str_compare(x:str,y:str):
    '''
    alphabetical string comparison.
    like an "a comes before b" comparison.
    '''
    return x < y

def str_ask():
    '''
    asking the user for two strings.
    compares them using str_compare().
    '''
    ask = input("Enter a string: ")
    ask2 = input("Enter another string: ")
    if str_compare(ask, ask2):
        return (f"{ask} comes before {ask2}.")
    else:
        return (f"{ask} does not come before {ask2}.")

def email_ask():
    '''
    email comparison function.
    type it the same twice lol.
    '''
    while(True):
        ask = input("------Enter your email address: ")
        ask2 = input("Enter your email address again: ")
        if ask != ask2:
            print("The two emails did not match, please try again...")
            continue
        else:
            print("Thank you!")
            break
    return

def iter_vroom(x:int):
    '''
    iterative factorial on x.
    '''
    y = 1
    for i in range(1, x + 1):
        y *= i
    return y

def recurse_vroom(x:int):
    '''
    recursive factorial on x.
    '''
    if x == 0 or x == 1:
        return 1
    else:
        return x * recurse_vroom(x-1)
    
def math_vroom(x:int):
    '''
    math.factorial on x.
    '''
    return vroom(x)

def vroom_race(x:int,func):
    '''
    times the execution of the provided function while
    passing said function the int x as its argument.
    returns [output of function, int time of exec in ns]
    '''
    start = time.perf_counter_ns()
    numout = func(x)
    stop = time.perf_counter_ns()
    return (numout), (stop - start)

def vroom_races(userin:int):
    '''
    will test and print the timed results of the iterative,
    recursive, and python module factorial functions
    using 3 predetermined and one user-provided value.
    '''
    vrooms = [iter_vroom, recurse_vroom, math_vroom]
    vroom_names = ["Iterative","Recursive","python.math"]
    inputs = [3,10,25,userin]
    
    #rangelimiter
    if userin > 100:
        raise ValueError("Input must be <= 100")

    #warmup
    for i in range(0,3):
        vrooms[i](1)

    print(f"{'Type':>12} {'':-^3} {'Input':^6} {'':-^3} {'Time (ns)':<12} {'':-^3} {'Output':^6}")
    #iterate thru inputs and functions
    for i in range(0,4):
        print(f"{'':-^50}")
        for p in range(0,3):
            result = vroom_race(inputs[i],vrooms[p])
            print(f"{vroom_names[p]:>12} {'':-^3} {inputs[i]:>6} {'':-^3} {result[1]:<12} {'':-^3} {result[0]:<6g}")
    return

def main():
    '''
    calls each step of the python assignment
    '''

    print("\n----- Step 1 -----")
    print(stop_shouting())

    print("\n----- Step 2 -----")
    print(vowel_ask())

    print("\n----- Step 3 -----")
    print(str_ask())

    print("\n----- Step 4 -----")
    email_ask()

    print("\n----- Step 5 ------")
    vroom_races(int(input("Enter an integer (<100) for factorial function racing: ")))

if __name__ == "__main__":
    main()