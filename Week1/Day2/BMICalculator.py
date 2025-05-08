print("Welcome to Body Mass Index Calculator. Enter some details to calculate your Body Mass Index.")

user_name = input("Please enter the name of the user: ")
height = float(input("Please enter the height in metres: "))
weight = float(input("Please enter the weight in kg: "))

# Calculate the bmi using weight and height.
bmi = round(weight/(height ** 2), 2)

print(f"The BMI for {user_name} is: {bmi}")
# The above concept is f-strings where we can add character f before the string and add variables without any type conversion/ casting
