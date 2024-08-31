def slice(obj, slicing_parameters):

    if not slicing_parameters:
        return obj

    start, stop, step = slicing_parameters + [None] * (3 - len(slicing_parameters))

    length = len(obj)

    if step is None:
        step = 1

    if step < 0:
        if start is None:
            start = length - 1
        if stop is None:
            stop = -1
        else:
            stop = stop - 1
    else:
        if start is None:
            start = 0
        if stop is None:
            stop = length

    sliced_obj = []
    i = start

    if step > 0:
        while i < stop and i < length:
            sliced_obj.append(obj[i])
            i += step
    else:
        while i > stop and i >= 0:
            sliced_obj.append(obj[i])
            i += step

    if isinstance(obj, str):
        return "".join(sliced_obj)
    else:
        return sliced_obj


my_string = "Hello, World!"
my_list = [1, 2, 3, 4, 5]
my_tuple = (10, 20, 30, 40, 50)

print(slice(my_string, [2, 3, 1]))  
print(slice(my_list, [2, 4]))     
print(slice(my_tuple, []))        
print(slice(my_string, [None, None, -1])) 
