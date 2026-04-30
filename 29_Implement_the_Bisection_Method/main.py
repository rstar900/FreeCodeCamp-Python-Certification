def f(x, number):
    result = x*x - number
    return result

def abs(x):
    if x < 0:
        return -1*x
    return x    

def square_root_bisection(number, tolerance=0.1, max_iterations=10):
    if number < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if number == 0 or number == 1:
        print(f'The square root of {number} is {number}')
        return number
    # Iterate for the function f(x) = x^2-number, until iterations are max, or solution within tolerance
    x_min = 0
    x_max = max(number, 1)
    x_mid = (x_min + x_max) / 2
    iterations = max_iterations
    while iterations > 0:  
        x_mid = (x_min + x_max) / 2
        fx = f(x_mid, number)
        print(f'{iterations},{x_min},{x_max}')
        if fx >= 0:
            if abs(x_min - x_max) <= tolerance:
                print(f'The square root of {number} is approximately {x_mid}')
                return x_mid
            x_max =  x_mid
        else:
            if abs(x_min - x_max) <= tolerance:
                print(f'The square root of {number} is approximately {x_mid}')
                return x_mid
            x_min = x_mid
        iterations -= 1
    print(f'Failed to converge within {max_iterations} iterations')
