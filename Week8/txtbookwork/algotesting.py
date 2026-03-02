# Michael Audi - CIS161 Week 8 Algorithm Textbook Work

import math

def algo53(n:int):
    if n < 1:
        raise ValueError(f"Input must be a positive integer. Received: {n}")
    elif((n == 1) or (n == 2)):
        return [n]

    quotient, remainder = divmod(n, 3)

    if remainder == 0:
        return [3] * quotient
    elif remainder == 1:
        return [3]*(quotient - 1) + [2,2]
    else:
        return [3] * quotient + [2]

        


def main():
    algo53out = algo53(2001)
    print(f"List of pos integers: {algo53out}")
    print(f"length of list: {len(algo53out)}")
    print(f"Product of list: {math.prod(algo53out)}")

if __name__ == "__main__":
    main()