def selection_sort(input_list):
    # No need to sort for empty or single element lists
    if len(input_list) <= 1:
        return input_list

    # Outer loop to choose the current position to replace the minimum onto (leave last)
    for i in range(len(input_list) - 1):
        # Inner loop to find the next minimum element
        for j in range(i+1, len(input_list)):
            if input_list[j] < input_list[i]:
                # Python way of swapping without temp
                input_list[i], input_list[j] = input_list[j], input_list[i]
                
    # Return the sorted list            
    return input_list
