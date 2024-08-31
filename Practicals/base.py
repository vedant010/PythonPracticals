def base(text, input_base, output_base):
    def to_decimal(num_str, base):
        num = 0
        for char in num_str:
            digit = int(char, base)
            num = num * base + digit
        return num

    def from_decimal(num, base):
        result = ""
        while num > 0:
            digit = num % base
            if digit < 10:
                result = str(digit) + result
            else:
                result = chr(ord('a') + digit - 10) + result
            num //= base
        return result

    decimal_num = to_decimal(text, input_base)
    if decimal_num is None:
        return "Error: Invalid input. Make sure the string represents a valid number."

    result = from_decimal(decimal_num, output_base)
    return result

input_text = input("Enter a number or alphabets in that base: ")
input_base = int(input("Enter the input base: "))
output_base = int(input("Enter the output base: "))
print(base(input_text, input_base, output_base))
