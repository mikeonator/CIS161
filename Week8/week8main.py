# Michael Audi - CIS161 Week 8 Main Assignment


def stop_shouting():
    firstin = input("Enter a phrase: ")
    secondin = input("Enter a phrase: ")
    if firstin.upper() == secondin:
        return ("Stop shouting please!")
    else:
        return ("You didn't do as you were asked... sigh.")

def vowel_check(x:str):
    vowels = ['a','e','i','o','u']
    count = 0
    for char in x:
        for vowel in vowels:
            if char == vowel:
                count += 1
                break
    return count

def vowel_ask():
    string = input("Enter a string: ")
    count = vowel_check(string)
    if count == 0:
        return f"There are no vowels in the string {string}"
    elif count == 1:
        return (f"There is {count} vowel in the string {string}.")
    else:
        return (f"There are {count} vowels in the string {string}.")

def str_compare(x:str,y:str):
    if x < y:
        return True
    else:
        return False

def str_ask():
    ask = input("Enter a string: ")
    ask2 = input("Enter another string: ")
    if str_compare(ask, ask2):
        return (f"{ask} comes before {ask2}.")
    else:
        return (f"{ask} does not come before {ask2}.")


def main():
    print("\n----- Step 1 -----")
    print(stop_shouting())

    print("\n----- Step 2 -----")
    print(vowel_ask())

    print("\n----- Step 3 -----")
    print(str_ask())

if __name__ == "__main__":
    main()