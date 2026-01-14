#Two's Complement Functions 

def twoscomplement(num: str):
    bits = int(num, 2)
    mask = (2 ** len(num)) - 1
    inverted = bits ^ mask
    complement = inverted +1
    return format(complement, f"0{len(num)}b")

