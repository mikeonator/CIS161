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

def step3(x:int,y:int):
    while (x > 0):
        if (x%2 == 0):
            print(f"{x} is Even.")
        else:
            print(f"{x} is Odd.")
        x = x - y
    print("Blastoff!!")

def step4_1():
    while True:
        wordin = input("Input a word: ")
        if len(wordin) < 5:
            print("Goodbye!")
            break
        print(f"{wordin} has {len(wordin)} letters.")


def step4_2():
    count = 0
    while True:
        wordin = input("Input a word: ")
        if len(wordin) < 5:
            print("Goodbye!")
            break
        elif count == 4:
            print("Loser!")
            break
        print(f"{wordin} has {len(wordin)} letters.")
        count += 1

def step5():
    count = 10
    while count < 101:
        print(f"{count:>5} | {bin(count):<9} | {hex(count):<5}")
        count += 1

def step6iterate(x:int):
    if x == 0:
        return
    print(x*"*")
    step6iterate(x-1)

def step6recursion(x:int):
    while x != 0:
        print(x*"*")
        x -= 1


def main():
    # Step 1
    print("\n----- Step 1 -----")
    step1(int(input("Enter an integer: ")))

    # Step 2
    print("\n----- Step 2 -----")
    step2(int(input("Enter an integer: ")))

    # Step 3
    print("\n----- Step 3 -----")
    step3(int(input("Enter an integer: ")),int(input("Enter a decrease amount: ")))

    # Step 4
    print("\n----- Step 4.1 -----")
    step4_1()

    print("\n----- Step 4.2 -----")
    step4_2()

    print("\n----- Step 5 -----")
    step5()

    print("\n----- Step 6 -----")
    print("Iteration:")
    step6iterate(5)
    print("Recursion:")
    step6recursion(5)

if __name__ == "__main__":
    main()
