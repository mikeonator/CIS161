#Two's Complement Functions 

def invertbits(num: str):
    bits = int(num, 2)
    mask = (2 ** len(num)) - 1
    inverted = bits ^ mask
    return format(inverted, f"0{len(num)}b")

