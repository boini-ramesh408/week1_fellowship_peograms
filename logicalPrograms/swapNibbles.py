def swap_nibbles(integer_number):
    return (integer_number & 0x0F) << 4 | (integer_number & 0xF0) >> 4
    print(swap_nibbles(integer_number))


integer_number = int(input("enter a integer number to find the nibbles:"))
swap_nibbles(integer_number)
