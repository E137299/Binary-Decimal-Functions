def binary_to_decimal(binary_str: str) -> int:
    decimal_value = 0
    power = 0

    # Iterate over the binary string from right to left
    for digit in reversed(binary_str):
        # Convert the current digit to an integer and add to the decimal value
        if digit == '1':
            decimal_value += 2 ** power
        power += 1

    return decimal_value


def decimal_to_binary(decimal_num: int) -> str:
    binary_str = ""
    
    # Continue dividing the number by 2 and store the remainder
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_str = str(remainder) + binary_str
        decimal_num = decimal_num // 2
    
    # Ensure the binary string is exactly 8 bits long
    binary_str = binary_str.zfill(8)
    
    return binary_str
