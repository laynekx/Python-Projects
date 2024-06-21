MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f'Sorry. The {item} is insufficient.')
            return False
        return True

def is_transaction_successful(payment, cost):
    if cost > payment:
        print("Sorry. That's not enough money. Money refunded.")
        return False
    else:
        change = round(payment - cost, 2)
        print(f'Here is your change: ${change:.2f}')
        global profit
        profit += cost
        return True

def process_coins():
    print('Please insert coins.')
    total = int(input('How many quarters?')) * 0.25
    total += int(input('How many dimes?')) * 0.10
    total += int(input('How many nickels?')) * 0.5
    total += int(input ('How many pennies?')) * 0.01
    return total

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]  
    print(f'Here is your {drink_name}.')    


machine_on = True

while machine_on:
    selection = input('What would you like? (espresso/latte/cappuccino)').lower()
    if selection == 'report':
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Profit: ${profit:.2f}')
    elif selection == 'off':
        machine_on = False
    else:
        drink = MENU[selection]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(selection, drink["ingredients"])
