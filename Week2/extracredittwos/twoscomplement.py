#Michael Audi - Two's Complement Function

def twoscomplement(num: str):
    '''
    Docstring for twoscomplement
    
    :param num: Input a string containing a binary number of any length (EX: '010111010')
    :type num: str
    '''
    bits = int(num, 2)
    mask = (2 ** len(num)) - 1
    inverted = bits ^ mask
    complement = inverted +1
    return format(complement, f"0{len(num)}b")

def main():
    print(twoscomplement(input("Input a binary number: ")))


if __name__ == "__main__":
    main()