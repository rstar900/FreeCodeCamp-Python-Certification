def quick_sort(input_list):
    # Base case
    if len(input_list) <= 1:
        return input_list

    # Take the first element as pivot element
    pivot = input_list[0]

    # Divide into three lists
    # One with elements less than the pivot,
    less_list = []
    # one with elements equal to the pivot,
    equal_list = []
    # and one with elements greater than the pivot
    greater_list = []

    # Fill the lists
    for i in input_list:
        if i < pivot:
            less_list.append(i)
        elif i == pivot:
            equal_list.append(i)
        else:
            greater_list.append(i)

    # Sort them recursively (no need for equal list as it only has the same elements)
    less_list =  quick_sort(less_list) 
    greater_list =  quick_sort(greater_list)                

    # Combine all the sorted lists in a new list and return it
    return less_list + equal_list + greater_list 
