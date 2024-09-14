def decimal_subtraction(str1, str2):
    
    return str_to_int(str1) - str_to_int(str2)
def decimal_addition(str1, str2):
    
    return str_to_int(str1) + str_to_int(str2)

def str_to_int(text):
    
    temp = 0
    mul = 1
    string = 0
    for i in range(len(text) - 1,-1,-1):
        string = ord(text[i]) - ord('0')
        temp = temp + string*mul
        mul = mul * 10
    
    return temp
        
print(decimal_subtraction('5698', '3465'))
print(decimal_addition('5698', '3465'))
