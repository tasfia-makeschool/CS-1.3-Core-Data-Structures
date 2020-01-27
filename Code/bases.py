#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    # Decode digits from binary (base 2)
    '''
    if base == 2:
        exp = 0
        decimal = 0
        for digit in digits[::-1]:
            decimal += int(digit) * 2**exp
            exp += 1
        return decimal
    '''

    # Decode digits from hexadecimal (base 16)
    '''
    elif base == 16:
        exp = 0
        decimal = 0
        for digit in digits[::-1]:
            decimal += string.hexdigits.index(digit) * 16**exp
            exp += 1
        return decimal
    '''

    # Decode digits from any base (2 up to 36)
    exp = 0
    decimal = 0
    for digit in digits[::-1]:
        decimal += (string.digits + string.ascii_lowercase).index(digit) * base**exp
        exp += 1
    return decimal


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    # assert number >= 0, 'number is negative: {}'.format(number)

    # Encode number in binary (base 2)
    '''
    if base == 2:
        if number > 1:
            return encode(number // 2, base) + str(number % 2)
        else:
            return '1'
    '''

    # Encode number in hexadecimal (base 16)
    '''
    elif base == 16:
        hex_digits = string.hexdigits[:16]
        if number <= 16:
            return hex_digits[number]
        else:
            return encode(number // 16, base) + hex_digits[number % 16]
    '''

    if number < 0 and base == 2:
        return negative_binary(encode, (0 - number)) # callback function
    else:
        # recursive -- Encode number in any base (2 up to 36)
        base_digits = (string.digits + string.ascii_lowercase)[:base]
        if number < base:
            return base_digits[number]
        else:
            return encode(number // base, base) + base_digits[number % base]

    # try iterative 

def negative_binary(encode, number):
    def invert(binary):
        return ''.join(['1' if bit == '0' else '0' for bit in binary])

    num_encode = encode(number, 2)[::-1]
    if len(num_encode) > 3:
        num_encode += (8 - len(num_encode)) * '0'
    else:
        num_encode += (4 - len(num_encode)) * '0'
    num_encode = invert(num_encode)
    neg_bin = ''
    carry = True
    for bit in num_encode:
        if carry:
            bit_sum = int(bit) + 1
            if bit_sum > 1:
                if bit_sum == 2:
                    neg_bin += '0'
                if bit_sum == 3:
                    neg_bin += '1'
                carry = True
            else:
                carry = False
                neg_bin += str(bit_sum)
        else:
            neg_bin += bit
    
    return neg_bin[::-1]

def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # Convert digits from base 2 to base 16 (and vice versa)
    # Convert digits from base 2 to base 10 (and vice versa)
    # Convert digits from base 10 to base 16 (and vice versa)
    # Convert digits from any base to any base (2 up to 36)
    return encode(decode(digits, base1), base2)

def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(
            digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    # main()
    # print(negative_binary(encode(60, 2)))
    # print(negative_binary(60))
    print(encode(-72, 2))
