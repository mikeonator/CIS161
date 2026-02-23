# Michael Audi - CIS161 Week 8 Main Assignment


def stop_shouting():
    firstin = input("Enter a phrase: ")
    secondin = input("Enter a phrase: ")
    if firstin.upper() == secondin:
        print("Stop shouting please!")
    else:
        print("You didn't do as you were asked... sigh.")
    return

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
        print(f"There are no vowels in the string {string}")
    elif count == 1:
        print(f"There is {count} vowel in the string {string}.")
    else:
        print(f"There are {count} vowels in the string {string}.")

def main():
    print("\n----- Step 1 -----")
    stop_shouting()

    print("\n----- Step 2 -----")
    vowel_ask()

    return

if __name__ == "__main__":
    main()