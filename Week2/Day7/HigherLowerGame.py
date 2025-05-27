import random
import art
import data

def identify_competitor():
    return random.choice(data.celebs)

def clear_screen():
    print("\n" * 20)
    print(art.game_name)

def print_competitors(comp_a, comp_b, current_score):
    clear_screen()
    if current_score > 0:
        print(f"You're right! Current score: {current_score}")
    print(f"Compare A: {comp_a["name"]}, {comp_a["profession"]}, from {comp_a["country"]}.")
    print(art.versus)
    print(f"Compare B: {comp_b["name"]}, {comp_b["profession"]}, from {comp_b["country"]}.")

def identify_winner(follow_a, follow_b):
    return "A" if follow_a >= follow_b else "B"

# Print the game name graphics

score = 0
continue_play = True

competitor_a = identify_competitor()

while continue_play:
    competitor_b = identify_competitor()
    if competitor_b == competitor_a:
        competitor_b = identify_competitor()

    print_competitors(competitor_a, competitor_b, score)

    winner = identify_winner(float(competitor_a["followers"]), float(competitor_b["followers"]))

    guess = input("Who has more followers? Type 'A' or 'B': ")

    if guess.lower() == winner.lower():
        score += 1
        competitor_a = competitor_b
    else:
        continue_play = False
        clear_screen()
        print(f"Sorry, that's wrong. Final score: {score}")
