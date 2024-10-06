import time

# First Approach
def count_odd_even_approach1(l):
    even_count = 0
    odd_count = 0
    for n in l:
        even_count += n % 2 == 0  
        odd_count += n % 2 == 1   
    return even_count, odd_count

# Second Approach
def count_odd_even_approach2(l):
    even_count = 0
    odd_count = 0
    for n in l:
        if n % 2:
            odd_count += 1  
        else:
            even_count += 1  
    return even_count, odd_count

# Third Approach
def count_odd_even_approach3(l):
    even_count = 0
    odd_count = 0
    for n in l:
        if n % 2 == 0:
            even_count += 1
        else:
            odd_count += 1 
    return even_count, odd_count

# Test data
l = [45,85,62,9,54,85,31,22,20,6,5,5,6,6,5,65]


even_count1, odd_count1 = count_odd_even_approach1(l)
print(f"Approach 1 - Even numbers: {even_count1}, Odd numbers: {odd_count1}")


even_count2, odd_count2 = count_odd_even_approach2(l)
print(f"Approach 2 - Even numbers: {even_count2}, Odd numbers: {odd_count2}")


even_count3, odd_count3 = count_odd_even_approach3(l)
print(f"Approach 3 - Even numbers: {even_count3}, Odd numbers: {odd_count3}")





def compare_execution_time(func1, func2, func3, arg):
    
    repetitions = 200000
    total_time_func1 = 0
    for _ in range(repetitions):
        start = time.time()
        func1(arg)
        end = time.time()
        total_time_func1 += (end - start)
    avg_time_func1 = total_time_func1 / repetitions
    print(f"Time taken for approach 1 = {avg_time_func1:.6f} s (average of {repetitions} runs)")

    total_time_func2 = 0
    for _ in range(repetitions):
        start = time.time()
        func2(arg)
        end = time.time()
        total_time_func2 += (end - start)
    avg_time_func2 = total_time_func2 / repetitions

    total_time_func3 = 0
    for _ in range(repetitions):
        start = time.time()
        func3(arg)
        end = time.time()
        total_time_func3 += (end - start)
    avg_time_func3 = total_time_func3 / repetitions

    percent_diff_func2 = ((avg_time_func2 - avg_time_func1) / avg_time_func1) * 100
    percent_diff_func3 = ((avg_time_func3 - avg_time_func1) / avg_time_func1) * 100

  
    if percent_diff_func2 < 0:
        print(f"Approach two is {abs(percent_diff_func2):.2f}% faster than approach one")
    else:
        print(f"Approach two is {percent_diff_func2:.2f}% slower than approach one")


    if percent_diff_func3 < 0:
        print(f"Approach three is {abs(percent_diff_func3):.2f}% faster than approach one")
    else:
        print(f"Approach three is {percent_diff_func3:.2f}% slower than approach one")



compare_execution_time(count_odd_even_approach1, count_odd_even_approach2, count_odd_even_approach3, l)
