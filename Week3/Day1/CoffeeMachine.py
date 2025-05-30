import CoffeeData

def print_report(current_report):
    print(f'''
    Water: {current_report["water"]}ml
    Milk: {current_report["milk"]}ml
    Coffee: {current_report["coffee"]}gm
    Money: ${current_report["money"]}       
    ''')

def check_resources(current_report, choice):
    if current_report["water"] < CoffeeData.data[choice]["ingredients"]["water"]:
        return "Sorry there is not enough water."
    elif current_report["coffee"] < CoffeeData.data[choice]["ingredients"]["coffee"]:
        return "Sorry there is not enough coffee."
    elif current_report["milk"] < CoffeeData.data[choice]["ingredients"]["milk"]:
        return "Sorry there is not enough milk."
    else:
        return "Preparing your drink"

def input_coins_and_calculate_amount():
    amount = 0
    print("Please insert coins.")
    quarter_count = int(input("How many quarters? "))
    dime_count = int(input("How many dimes? "))
    nickel_count = int(input("How many nickels? "))
    penny_count = int(input("How many pennies? "))

    amount = quarter_count * 0.25 + dime_count * 0.10 + nickel_count * 0.05 + penny_count * 0.01
    return amount

def check_sufficient_coins_entered(amount, choice):
    prep_coffee = False
    if amount < CoffeeData.data[choice]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    elif amount > CoffeeData.data[choice]["cost"]:
        change = round((amount - CoffeeData.data[choice]["cost"]), 2)
        print(f"Here is ${change} dollars in change.")
        prep_coffee = True
    else:
        prep_coffee = True
    return prep_coffee


def deduct_resources(report, choice):
    for key in CoffeeData.data[choice]["ingredients"]:
        report[key] -= CoffeeData.data[choice]["ingredients"][key]
    report["money"] = CoffeeData.data[choice]["cost"]
    return report


def prepare_drink(report, choice):
    final_report = deduct_resources(report, choice)
    print(f"Here is your {choice}. Enjoy!")
    return final_report

ingredients_report = {
    "water": 500,
    "coffee": 100,
    "milk": 300,
    "money": 0
}
run_coffee_machine = True

while run_coffee_machine:
    user_choice = input("What would you like? (espresso/ latte/ cappuccino)")
    if user_choice == "report":
        print_report(ingredients_report)
    elif user_choice == "off":
        run_coffee_machine = False
    else:
        resource_check = check_resources(ingredients_report, user_choice)
        if resource_check == "Preparing your drink":
            amount_entered = input_coins_and_calculate_amount()
            is_drink_prepared = check_sufficient_coins_entered(amount_entered, user_choice)
            if is_drink_prepared:
                ingredients_report = prepare_drink(ingredients_report, user_choice)
        else:
            print(resource_check)

