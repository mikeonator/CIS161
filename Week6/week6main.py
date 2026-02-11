# Michael Audi - CIS161 Week 6 Main Assignment

def step1(x:int):
    while (x > 0):
        print(x)
        x -= 1
    print("Blastoff!!")

def step2(x:int):
    while (x > 0):
        if (x%2 == 0):
            print(f"{x} is Even.")
        else:
            print(f"{x} is Odd.")
        x -= 1
    print("Blastoff!!")


def main():
    # Step 1
    print("\n----- Step 1-----")
    step1(int(input("Enter an integer: ")))

    # Step 2
    print("\n----- Step 2-----")
    step2(int(input("Enter an integer: ")))



if __name__ == "__main__":
    main()
