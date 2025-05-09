print("Welcome to the Rollercoaster ride!")

height = int(input("Please enter your height: "))

if height >= 120:
    print("You are eligible to buy the ticket.")
    age = int(input("Please enter your age: "))
    amount = 0
    if age < 12:
        print("Child ticket price: INR 5")
        amount = 5
    elif age >= 12 and age <= 18:
        print("Youth ticket price: INR 7")
        amount = 7
    else:
        print("Adult price ticket: INR 12")
        amount = 12

    photo_required = input("Do you require a photo to be clicked during the ride and shared with you? (Yes or No)")
    if photo_required.lower() == "yes":
        amount += 3

    print(f"The total amount for your ride ticket is: INR {amount}")

else:
    print("Sorry! you are not eligible to have this ride.")

