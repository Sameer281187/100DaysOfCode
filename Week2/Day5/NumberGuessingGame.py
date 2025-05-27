import random
import art

def guess_a_number():
    return int(input("Make a guess: "))

def reduce_attempt_count(attempt, message):
    attempt -= 1
    if attempt > 0:
        print(message)
        print("Guess again")
        print(f"You have {attempt} attempts remaining to guess the number.")
    else:
        print("You have run out of guesses. Refresh the page to run again.")
    return attempt

print(art.logo)
print("Welcome to the Number Guessing Game !")
print("I am thinking of a number between 1 and 100. ")

thought_number = random.randrange(1, 100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

no_of_attempts = 10 if difficulty.lower() == "easy" else 5
print(f"You have {no_of_attempts} attempts to guess the number.")

while no_of_attempts > 0:
    guessed_number = guess_a_number()
    message_value = ""
    if guessed_number == thought_number:
        print(f"You got it! The answer was {guessed_number}")
        break
    elif guessed_number < thought_number:
        message_value = "Too Low"
        no_of_attempts = reduce_attempt_count(no_of_attempts, message_value)
    else:
        message_value = "Too High"
        no_of_attempts = reduce_attempt_count(no_of_attempts, message_value)
