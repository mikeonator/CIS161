#Michael Audi - CIS161 Week 3 Main Assignment

import lifeexpectancy as le

def main():

    ##Step 1
    print("--- Step 1 ---")
    name = input("What's your name?\n")
    print(f"Hello {name}!")

    ##Step 2
    print("\n--- Step 2 ---")
    age = input("What's your age?\n")
    
    try:
        print(f"Your age in 5 years would be {age + 5}")
    except TypeError:
        print('TypeError: can only concatenate str (not "int") to str')
        print('Because age is an str, the + is being treated as string concatenation, not as addition.\n')
        print(f"Your age in 5 years would be {(int(age) + 5)}")
    
    ##Step 3
    print("\n--- Step 3 ---")
    addto = input("How many years do you wish to add to your age?\n")
    print(f"Your age in {addto} years would be {int(addto) + int(age)}\n")

    ##Step 3 Extra Credit
    print(f"{'':-^13}")
    print(f"You are currently age {age}.")
    print(f"Based on the Actuarial Life Table as used in the 2025 Trustees Report by the Social Security Administration...")
    print(f"...")
    print(f"...")
    print(f"...")
    print(f"You are expected to die in the year {le.life_expectancy(int(age))}!")



if __name__ == "__main__":
    main()