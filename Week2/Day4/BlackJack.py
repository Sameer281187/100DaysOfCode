import random
import BlackJackArt

def initial_draw(all_cards):
    """ Draws the initial two card numbers for player and one card number for computer"""
    for i in range(2):
        if i < 1:
            cards_drawn["player"].append(random.choice(all_cards))
            cards_drawn["computer"].append(random.choice(all_cards))
        else:
            cards_drawn["player"].append(random.choice(all_cards))

def check_win_by_blackjack(score):
    """ Checks if the player wins by blackjack after initial draw"""
    if score == 21:
        print("Won by Blackjack. You won")
        exit(1)

def display_initial_scores(player, cards):
    """Displays the scores of player and computer after each card draw made by player"""
    print(f"Your Cards: {cards["player"]}, current score: {player}")
    print(f"Computer's first card: {cards["computer"][0]}")

def want_to_play():
    """Checks with player if they want to continue playing"""
    is_play = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")
    continue_play = True if is_play == "y" else False
    return continue_play

def display_graphics():
    """Displays the BLACKJACK graphics at start of each round"""
    print(BlackJackArt.blackjack_art)

def display_final_result(player, computer):
    """ Checks the final result and declares the winner"""
    if player > 21:
        print("You went over, You Lose")
    elif computer > 21:
        print("Opponent went over, You win")
    elif player == computer_score:
        print("Draw")
    elif player > computer_score:
        print("You Won")
    else:
        print("You Lose")

all_card_numbers = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
display_graphics()
is_continue = want_to_play()

while is_continue:
    cards_drawn = {
        "player": [],
        "computer": []
    }
    initial_draw(all_card_numbers)

    player_score = sum(cards_drawn["player"])
    computer_score = sum(cards_drawn["computer"])

    check_win_by_blackjack(player_score)
    display_initial_scores(player_score, cards_drawn)

    while player_score <= 21:
        is_continue = input("Type 'y' to get another card, type 'n' to pass: ")
        if is_continue == "y":
            cards_drawn["player"].append(random.choice(all_card_numbers))
            player_score = sum(cards_drawn["player"])
            display_initial_scores(player_score, cards_drawn)
        else:
            break

    if player_score <= 21:
        while computer_score < 17:
            cards_drawn["computer"].append(random.choice(all_card_numbers))
            computer_score = sum(cards_drawn["computer"])

    print(f"Your final hand: {cards_drawn["player"]}, final score: {player_score}")
    print(f"Computer final hand: {cards_drawn["computer"]}, final score: {computer_score}")

    display_final_result(player_score, computer_score)

    is_continue = want_to_play()
    print("\n" * 20)
    if is_continue:
        display_graphics()



