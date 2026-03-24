def number_pattern(n):
    # Input validation
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    if n <= 0:
        return 'Argument must be an integer greater than 0.'    
    # Function logic
    return ' '.join([str(i + 1) for i in range(n)])
