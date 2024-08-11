def modulo(a, b):
    while(a>b):
        a = a-b
    if a==b:
        return 0
    else:
        return a

print(modulo(92,3))
print(modulo(56,7))
print(modulo(99,11))
print(modulo(50,30))
print(modulo(8,3))
