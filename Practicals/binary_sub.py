def binary_subtraction(a, b):
    def binary_addition(x, y):
        while y != 0:
            carry = x & y
            x = x ^ y
            y = carry << 1
        return x

    def twos_complement(n):
        return binary_addition(~n, 1)

    return binary_addition(a, twos_complement(b))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = binary_subtraction(a, b)

print(f"The result of subtracting {b} from {a} is: {result}")
