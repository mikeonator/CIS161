#Michael Audi - Two's Complement Function

def twoscomplement(InNum: str):
    '''
    Input a string containing a decimal number between -128 and 127 and recieve a string containing the Two's complement of that decimal.
    
    :param num: Input a string containing a decimal number between -128 and 127.
    :type num: str
    :return str: String containing the Two's Complement of the input decimal number.
    '''

    num = int(InNum)
    if (num > 127) or (num < -128):
        return "ERROR | Please input a decimal number (max 127 | min -128)."
    elif (0 <= num <= 127):
        #if number is positive, return formatted string containing the binary representation of the positive number.
        return (f"{bin(num)[2:]:0>8}")
    elif (-128 <= num < 0):
        #if number is negative, perform twos complement action on the binary representation of the negative number as a positive (ykwim)
        bits = abs(num)
        mask = ((2 ** 8) - 1)
        inverted = bits ^ mask
        complement = inverted + 1
        return (f"{bin(complement)[2:]:0>8}")

def main():
    print(twoscomplement(input("Please input a decimal number (max 127 | min -128): ")))


if __name__ == "__main__":
    main()