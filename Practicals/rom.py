def is_valid_number(string, base):
    valid_chars = "0123456789ABCDEF"[:base]
    for char in string.upper():
        if char not in valid_chars:
            return False
    return True

def rom(string, base):
    if string.startswith("0x"):
        string = string[2:]
    elif string.startswith("0o"):
        string = string[2:]
    
    if is_valid_number(string, base):
        num = int(string, base)
        roman_symbols = [
            ("M", 1000),
            ("CM", 900),
            ("D", 500),
            ("CD", 400),
            ("C", 100),
            ("XC", 90),
            ("L", 50),
            ("XL", 40),
            ("X", 10),
            ("IX", 9),
            ("V", 5),
            ("IV", 4),
            ("I", 1),
        ]
        result = ""
        for symbol, value in roman_symbols:
            while num >= value:
                result += symbol
                num -= value
        return result
    else:
        return "Error: Invalid input. Make sure the string represents a valid number."

print(rom("0o12", 8))
print(rom("123", 10))  
print(rom("0x12", 16))
