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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_sufficient(resource, user_choice):
    if resource["water"] >= MENU[user_choice]["ingredients"]["water"]:
        if resource["coffee"] >= MENU[user_choice]["ingredients"]["coffee"]:
            if user_choice == "espresso":
                return True
            else:
                if resource["milk"] >= MENU[user_choice]["ingredients"]["milk"]:
                    return True
                else:
                    feedback = "Sorry there is not enough milk."
                    return False, feedback
        else:
            feedback = "Sorry there is not enough coffee."
            return False, feedback
    else:
        feedback = "Sorry there is not enough water."
        return False, feedback


def insert_coins():
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    coin_sum = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return coin_sum


def update_resources(resource, user_choice):
    resources["water"] = resources["water"] - MENU[user_choice]["ingredients"]["water"]
    resources["coffee"] = resources["coffee"] - MENU[user_choice]["ingredients"]["coffee"]
    if user_choice != "espresso":
        resources["milk"] = resources["milk"] - MENU[user_choice]["ingredients"]["milk"]


continue_order = True
order_cost_sum = 0

while continue_order:

    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "espresso" or choice == "latte" or choice == "cappuccino":
        if is_sufficient(resources, choice) == True:
            #print(is_sufficient(resources, choice))
            inserted_coin = insert_coins()
            choice_cost = MENU[choice]["cost"]
            if inserted_coin > choice_cost:
                update_resources(resources, choice)
                change = round(inserted_coin - choice_cost, 2)
                print(f"“Here is ${change} dollars in change.")
                print(f"Here is your {choice} ☕️. Enjoy!")
                order_cost_sum = choice_cost + order_cost_sum
            elif inserted_coin == choice_cost:
                update_resources(resources, choice)
                print(f"Here is your {choice} ☕️. Enjoy!”")
                order_cost_sum = choice_cost + order_cost_sum
            else:
                print(f"Sorry that's not enough money. Money refunded.")
        else:
            print(is_sufficient(resources, choice)[1])
    elif choice == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${order_cost_sum}")
    elif choice == "off":
        print("Off.")
        continue_order = False
