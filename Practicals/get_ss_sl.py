def get_SS_SL_(L):

    L_sorted = sorted(set(L))

    if len(L_sorted) == 1:
        return [L_sorted[0], L_sorted[0]]  
    elif len(L_sorted) == 2:
        return [L_sorted[1], L_sorted[0]] 

    second_smallest = L_sorted[1]
    second_largest = L_sorted[-2]

    return [second_largest, second_smallest]

print(get_SS_SL_([10, 10, 20]))  
