def count(string, substring, boolean):
    count = 0
    start = 0

    while True:
        # Find the next occurrence of the substring
        start = string.find(substring, start)
        
        # If no more occurrences are found, break the loop
        if start == -1:
            break
        
        # Increment the count
        count += 1
        
        # Move the start index
        if boolean:
            start += 1  # Move one character forward for overlapping
        else:
            start += len(substring)  # Move past the substring for non-overlapping

    return count

string = "abababa"
substring = "aba"
boolean = True

result = count(string, substring, boolean)
print(result) 

boolean = False
result = count(string, substring, boolean)
print(result) 
