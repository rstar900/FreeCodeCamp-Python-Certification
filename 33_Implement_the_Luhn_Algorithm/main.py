def verify_card_number(number):
    # We assume the input is a valid type of input from the examples, so no invalid character check
    numbers_list = [int(i) for i in number if i.isnumeric()]
    
    # Double every other number (leaving last)
    for i in range(len(numbers_list)-2, -1, -2):
        numbers_list[i] *= 2
        # If the doubled number is a 2 digit number, add the digits
        if numbers_list[i] >= 10:
            numbers_list[i] = numbers_list[i] // 10 + numbers_list[i] % 10

    # If the sum of numbers is divisible by 10 then valid, else invalid
    if sum(numbers_list) % 10 == 0:
        return 'VALID!'            

    return 'INVALID!'   
