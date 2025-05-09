print("*****************Welcome to pizza ordering service*****************")

size = input("Enter the size of pizza that you want to order (S for small, M for Medium, L for Large): ")
add_pepperoni = input("Do you want to add pepperoni to your pizza (Y for yes, N for no): ")
extra_cheeze = input("Do you want to add extra cheeze for your pizza (Y for yes, N for no): ")
amount = 0

if size.lower() == "s":
    print("The amount for small pizza is INR 15")
    amount += 15
elif size.lower() == "m":
    print("The amount for medium pizza is INR 20")
    amount += 20
elif size.lower() == "l":
    print("The amount for large pizza is INR 25")
    amount += 25
else:
    print("Please enter a valid value for size of the pizza. Refer the menu.")
    exit("Invalid pizza type selected")

if add_pepperoni.lower() == "y":
    if size.lower() == "s":
        print("INR 2 will be added to your amount for adding pepperoni to small pizza")
        amount += 2
    else:
        print("INR 3 will be added to your amount for adding pepperoni to medium or large pizza")
        amount += 3

if extra_cheeze.lower() == "y":
    print("INR 1 will be added to your amount for adding extra cheese to your pizza")
    amount += 1

print(f"Thank you for ordering the pizza with us. Your total amount for the pizza is INR {amount}")

