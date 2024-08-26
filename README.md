# Binary and Decimal Conversions
## Objective:
In this assignment, you will write two Python functions:
- A function to convert a binary number (given as a string) to a decimal value.
- A function to convert a decimal value to a binary number (returned as a string).
## Instructions:
1. **Binary to Decimal Conversion (binary_to_decimal())**
    - Write a function named binary_to_decimal(binary_str) that takes in a binary number as a string (e.g., "1011") and returns the decimal equivalent as an integer.
    - Constraints: You should not use Python's built-in functions like int() with base arguments, or bin().
2. Decimal to Binary Conversion (decimal_to_binary)
    - Write a function named decimal_to_binary(decimal_num) that takes in a decimal number (e.g., 11) and returns the binary equivalent as a string (e.g., "1011").
    - Constraints: You should not use Python's built-in functions like bin().

## Example:
**Binary to Decimal:**
```python
python
binary_str = "1101"
decimal_value = binary_to_decimal(binary_str)
print(decimal_value)  # Output should be 13
```
**Decimal to Binary:**
```python
decimal_num = 13
binary_value = decimal_to_binary(decimal_num)
print(binary_value)  # Output should be "1101"
```

**Hints:**
    - For binary_to_decimal, consider how you would manually convert a binary number to decimal by summing powers of 2.
    - For decimal_to_binary, think about how you repeatedly divide the number by 2 and track the remainders.

## Evaluation Criteria:
- Correctness: Both functions should correctly convert binary to decimal and decimal to binary.
- Code readability: The code should be clean, well-organized, and easy to understand.
- Edge cases: The functions should handle edge cases gracefully (e.g., converting 0 in both directions).