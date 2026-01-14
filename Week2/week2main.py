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
except TypeError:
    print("if x = 1.825")
    print("TypeError: 'float' object cannot be interpreted as an integer")
    print("bin() and hex() can only accept integers, not floats.")

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

og_size = 240
dict_size = 25
comp_text_size = 148

#Step 1 - Compression percentage formula
def compression(og:int,dsize:int,compressed:int):
    return (1 - ((compressed + dsize)/og))

print(f"{'':-^10}")
print("Step 1 and 2")

#Step 2 - Calculate the compression percentage for the given variables
compress = compression(og_size, dict_size, comp_text_size)
print(compress)

print(f"{'':-^10}")
print("Step 3")

print(f"{'Compressed Text Size:':>21} {comp_text_size:<} characters")
print(f"{'Dictionary Size:':>21} {dict_size:<} characters")
print(f"{'Total Characters:':>21} {(comp_text_size+dict_size):<} characters")
print(f"{'Original Text Size:':>21} {og_size:<} characters")
print(f"{'Compression:':>21} {(compress*100):<.2f}%")

print(f"{'':-^10}")
print("Step 3 Again!")

og_size = 3201
dict_size = 402
comp_text_size = 1999

compress = compression(og_size, dict_size, comp_text_size)

print(f"{'Compressed Text Size:':>21} {comp_text_size:<} characters")
print(f"{'Dictionary Size:':>21} {dict_size:<} characters")
print(f"{'Total Characters:':>21} {(comp_text_size+dict_size):<} characters")
print(f"{'Original Text Size:':>21} {og_size:<} characters")
print(f"{'Compression:':>21} {(compress*100):<.2f}%")

print(f"{'':-^10}")
print("Step 3 Again!!")

og_size = 290120
dict_size = 23205
comp_text_size = 210384

compress = compression(og_size, dict_size, comp_text_size)

print(f"{'Compressed Text Size:':>21} {comp_text_size:<} characters")
print(f"{'Dictionary Size:':>21} {dict_size:<} characters")
print(f"{'Total Characters:':>21} {(comp_text_size+dict_size):<} characters")
print(f"{'Original Text Size:':>21} {og_size:<} characters")
print(f"{'Compression:':>21} {(compress*100):<.2f}%")

print(f"{'':-^10}")
print("Step 3 Again!!!")

og_size = 25
dict_size = 5
comp_text_size = 15

compress = compression(og_size, dict_size, comp_text_size)

print(f"{'Compressed Text Size:':>21} {comp_text_size:<} characters")
print(f"{'Dictionary Size:':>21} {dict_size:<} characters")
print(f"{'Total Characters:':>21} {(comp_text_size+dict_size):<} characters")
print(f"{'Original Text Size:':>21} {og_size:<} characters")
print(f"{'Compression:':>21} {(compress*100):<.2f}%")