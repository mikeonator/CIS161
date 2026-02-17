# Michael Audi - CIS161 Week 7 Main Assignment


def print_even_range(x:int,y:int):
    while x < y:
        if x % 2 == 0:
            print(x)
        x += 1

def main():

    print("----- Step 1 -----")
    print("Printing even numbers within input range")
    in1Low = int(input("Enter the Lower Bound: "))
    in1Up = int(input("Enter the Upper Bound: "))
    print(f"The even numbers between {in1Low} and {in1Up} are:")
    print_even_range(in1Low,in1Up)

if __name__ == "__main__":
    main()