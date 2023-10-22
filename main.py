# modules import
from menu import MENU, resources

# variables
total_collected = 0
is_on = True

# functions
def get_user_choice():
    '''This function is used to get the user choice of what they would like. The options are either espresso, latte, cappuccino, report, or off.'''
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    return user_choice

def report():
    '''Function is used to display the remaining resources left in the machine'''
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${total_collected:.2f}")

def deduct_materials(item):
    '''This function will be used to deduct the materials when an order is placed.'''
    required_ingredients = MENU[item]['ingredients']
    for ingredient, amount in required_ingredients.items():
        resources[ingredient] -= amount

def enough_material(item):
    '''This function is used to find out whether there are enough materials to produce the selected product.'''
    for ingredient, amount in MENU[item]['ingredients'].items():
        if resources[ingredient] < amount:
            print(f"Sorry, not enough {ingredient}!")
            return False
    return True

def money_total():
    total = 0
    print("Time to pay!")
    denominations = {
        'quarters': 0.25,
        'dimes': 0.1,
        'nickels': 0.05,
        'pennies': 0.01
    }
    for denomination, value in denominations.items():
        num = int(input(f"How many {denomination}? "))
        total += num * value
    return total

def process_order(item):
    if enough_material(item):
        deduct_materials(item)
        total_paid = money_total()
        cost = MENU[item]['cost']
        if total_paid < cost:
            print(f"Sorry, this is not enough money! You need ${cost:.2f}.")
        else:
            change = round(total_paid - cost, 2)
            if change > 0:
                print(f"Here is your {item}. Your change is ${change:.2f}.")
            else:
                print(f"Here is your {item}. No change needed.")
            return cost
    else:
        return 0

# main program
while is_on:
    user_selection = get_user_choice()

    if user_selection in ['espresso', 'latte', 'cappuccino']:
        cost = process_order(user_selection)
        total_collected += cost
    elif user_selection == 'report':
        report()
    elif user_selection == 'off':
        is_on = False
    else:
        print("Invalid choice. Please choose from espresso, latte, cappuccino, report, or off.")

# Display the total money collected after all transactions
print(f"Total money collected: ${total_collected:.2f}")




        
    





