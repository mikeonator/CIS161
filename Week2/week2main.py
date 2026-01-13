#Michael Audi - CIS161 Week 2 Main Assignment

##Part 1

print("--Part 1--")

###Step 1

x = 31

print("Step 1")
print(f"x = {x} | bin(x) = {bin(x)} | hex(x) = {hex(x)}")

###Step 2

x = 1.825

print(f"{'':-^10}")
print("Step 2")
try:
    print(f"x = {x} | bin(x) = {bin(x)} | hex(x) = {hex(x)}")
except:
    print("if x = 1.825")
    print("TypeError: 'float' object cannot be interpreted as an integer")

x = 18

print(f"x = {x} | bin(x) = {bin(x)} | hex(x) = {hex(x)}")

###Step 3

y = 0b1011

z = 0xA3

print(f"{'':-^10}")
print("Step 3")
print(f"int(y) = {int(y)} | bin(y) = {bin(y)} | hex(y) = {hex(y)}")
print(f"int(z) = {int(z)} | bin(z) = {bin(z)} | hex(z) = {hex(z)}")

###Step 4

w = x + y + z

print(f"{'':-^10}")
print("Step 4")
print(f"The Sum of x ({x}), y ({y}), and z ({z}) is: {w}")

##Compression

print(f"{'':-^10}")
print("--Compression--")


#Step 1 - Compression percentage formula
def compression(og_size:int,dict_size:int,comp_text_size:int):
    return (1 - ((comp_text_size + dict_size)/og_size))

print(f"{'':-^10}")
print("Step 1")

print(compression(240, 25, 148))
