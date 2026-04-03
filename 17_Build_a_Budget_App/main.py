class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        # Check if withdrawal is possible and only then add to ledger
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0.00
        # Add positive and negative amounts from all ledger elements
        for dictionary in self.ledger:
            balance += dictionary['amount']
        return balance

    def transfer(self, amount, category):
        status = self.withdraw(amount, f'Transfer to {category.name}')
        category.deposit(amount, f'Transfer from {self.name}')
        return status

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True    

    # Method for returning the string representation of the Category object
    def __str__(self):
        # Center the name of the category with 30 characters and * filled
        result_str = f'{self.name:*^30}'
        for element in self.ledger:
            # Limit description to 23 characters
            result_str += f"\n{element['description'][:23]:<23}{element['amount']:>7.2f}"
        # Add the total balance to the result
        result_str += f'\nTotal: {self.get_balance():.2f}'    
        return result_str    


def create_spend_chart(categories):
    result_str = 'Percentage spent by category'
    spent_dictionary = {} # Mapping b/w category:spent%
    spent_total = 0.00 # Total withdrawals in all categories
    for category in categories:
        withdrawals = 0.00
        # Extract the deposits
        for dictionary in category.ledger:
            if dictionary['amount'] < 0:
                withdrawals += -dictionary['amount']
        spent_dictionary[category.name] = withdrawals
        spent_total += withdrawals
    # Divide the spent percentages by total spent amount and round to nearest 10 for each category (round (perc, -1))
    for category in categories:
        spent_dictionary[category.name] = int(round((spent_dictionary[category.name] / spent_total) * 100, -1))
    # Create the Y-Axis till 100
    for y in range(100, -1,-10):
        result_str += f'\n{y:>3}| '
        # create bars for each category
        for category in categories:
            if spent_dictionary[category.name] >= y:
                result_str += 'o'
            else:
                result_str += ' '
            result_str += '  '             
    # Create the horizontal lines
    horizontal_lines = 1 + 3 * len(categories)
    result_str += '\n' + 4 * ' ' + horizontal_lines * '-'
    # TODO: Print category names vertically

    return result_str + '\n' + str(spent_dictionary)

# Test Code
food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
auto = Category('Auto')
#print(food)
print(create_spend_chart([food, clothing, auto]))   
