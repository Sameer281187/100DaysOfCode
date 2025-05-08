print("Welcome to the Restaurant Billing Contribution calculator !")

total_bill = float(input("What is your total bill amount ? INR "))
tip_percentage = float(input("What %age of total bill do you want to give as a tip ? 5, 7 or 10 ? "))
no_of_people = int(input("How many people to split the bill ? "))

contribution_amount = round((total_bill * (1 + (tip_percentage / 100))) / no_of_people, 2)

print(f"Each person should pay: {contribution_amount}")