from info import MENU, resources

profit = 0

def resource_status(order_ingredients):
    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            print(f"Sorry, not enough {item}.")
            return False
    return True

def process_coins():
    """Returns the total from the coins received"""
    print("Please insert coins.")
    quarter = int(input("How many quarters?: "))*0.25
    dime = int(input("How many dimes?: "))*0.10
    nickle = int(input("How many nickles?: "))*0.05
    penny = int(input("How many pennies?: "))*0.01
    return quarter + dime + nickle + penny

def transaction_status(total_received, cost):
    """Returns whether transaction is possible or not"""
    change = 0
    if total_received >= cost:
        global profit 
        profit += cost
        change = round((total_received - cost), 2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    
def make_coffee(choice, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here's your {choice}. Enjoy!")

machine = True
while machine:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice=="off":
        machine = False
    elif choice=="report":
        print(f"Water {resources["water"]}ml")
        print(f"Milk {resources["milk"]}ml")
        print(f"Coffee {resources["coffee"]}ml")
    else:
        if resource_status(MENU[choice]["ingredients"]):
            total_received = process_coins()
            cost = MENU[choice]["cost"]
            if transaction_status(total_received, cost):
                order_ingredients = MENU[choice]["ingredients"]
                make_coffee(choice, order_ingredients)
