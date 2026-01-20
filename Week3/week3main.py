#Michael Audi - CIS161 Week 3 Main Assignment

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
        print('     TypeError: can only concatenate str (not "int") to str')
        print('     Because age is an str, the + is being treated as string concatenation, not as addition.\n')
        print(f"Your age in 5 years would be {(int(age) + 5)}")
    
    ##Step 3
    print("\n--- Step 3 ---")
    addto = input("How many years do you wish to add to your age?\n")
    print(f"Your age in {addto} years would be {int(addto) + int(age)}")
    

if __name__ == "__main__":
    main()