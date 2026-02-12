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

def step6recursion(x:int):
    if x == 0:
        return
    print(x*"*")
    step6recursion(x-1)

def step6iteration(x:int):
    while x != 0:
        print(x*"*")
        x -= 1

def ec_sumofdigits(x:int):
    if x < 10:
        return x
    else:
        return ((x % 10) + ec_sumofdigits(x // 10))

def ec_palindrome(x:str):
    x = x.strip().replace(" ","").lower()
    if len(x) <= 1:
        return True
    elif x[0] == x[-1]:
        return ec_palindrome(x[1:-1])
    else:
        return False


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
    step6iteration(5)
    print("Recursion:")
    step6recursion(5)

    print("\n----- Extra Credit 1 -----")
    ec1in = int(input("Input a number: "))
    print(f"The sum of {ec1in}'s digits is {ec_sumofdigits(ec1in)}.")

    print("\n----- Extra Credit 2 -----")
    ec2in = input("Input a potential palindrome: ")
    if ec_palindrome(ec2in):
        print(f"{ec2in.lower()} is a palindrome.")
    else:
        print(f"{ec2in.lower()} is not a palindrome.")

if __name__ == "__main__":
    main()
