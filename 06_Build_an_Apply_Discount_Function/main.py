def apply_discount(price, discount):
    # Input check
    if not (isinstance(price, int) or isinstance(price, float)):
        return 'The price should be a number'
    if not (isinstance(discount, int) or isinstance(discount, float)):
        return 'The discount should be a number'
    if price <= 0:
        return 'The price should be greater than 0'
    if discount < 0 or discount > 100:
        return 'The discount should be between 0 and 100'

    # Function logic    
    return price - price * discount / 100
