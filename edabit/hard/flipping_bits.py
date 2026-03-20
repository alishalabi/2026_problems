"""
You will be given a list of 32-bit unsigned integers. Flip all the bits 1 -> 0 and 0 -> 1 and return the result as an unsigned integer.

Worked Example
n = 4
4 is 0100 in binary. We are working in 32 bits so:
00000000000000000000000000000100 = 4
11111111111111111111111111111011 = 4294967291
return 4294967291
Examples
flipping_bits(2147483647) ➞ 2147483648

flipping_bits(1) ➞ 4294967294

flipping_bits(4) ➞ 4294967291
"""

def flipping_bits(input):
    converted_input = f"{input:032b}"
    switched_converted = ""
    for number in converted_input:
        if number == "1":
            switched_converted += "0"
        else:
            switched_converted += "1"
    return int(switched_converted, 2)


print(flipping_bits(4))
print(flipping_bits(2147483647))
print(flipping_bits(1))
