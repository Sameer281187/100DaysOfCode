import random
import BlackJackArt

def initial_draw(all_cards, cards):
    """ Draws the initial two card numbers for player and one card number for computer"""
    for i in range(2):
        if i < 1:
            cards["player"].append(random.choice(all_cards))
            cards["computer"].append(random.choice(all_cards))
        else:
            cards["player"].append(random.choice(all_cards))

def check_win_by_blackjack(score, cards):
    """ Checks if the player wins by blackjack after initial draw"""
    if score == 21:
        display_initial_scores(score, cards)
        print("Won by Blackjack. You won")
        exit(1)

def display_initial_scores(player, cards):
    """Displays the scores of player and computer after each card draw made by player"""
    print(f"Your Cards: {cards["player"]}, current score: {player}")
    print(f"Computer's first card: {cards["computer"][0]}")

def want_to_play():
    """Checks with player if they want to continue playing"""
    is_play = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")
    print("\n" * 20)
    display_graphics()
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
    elif player == computer:
        print("Draw")
    elif player > computer:
        print("You Won")
    else:
        print("You Lose")

def play_game():
    cards_drawn = {
        "player": [],
        "computer": []
    }
    initial_draw(all_card_numbers, cards_drawn)

    player_score = sum(cards_drawn["player"])
    computer_score = sum(cards_drawn["computer"])

    check_win_by_blackjack(player_score, cards_drawn)
    display_initial_scores(player_score, cards_drawn)

    while player_score <= 21:
        continue_playing = input("Type 'y' to get another card, type 'n' to pass: ")
        if continue_playing == "y":
            latest_card = random.choice(all_card_numbers)
            cards_drawn["player"].append(latest_card)
            player_score = sum(cards_drawn["player"])
            if player_score > 21 and latest_card == 11:
                cards_drawn["player"].remove(latest_card)
                cards_drawn["player"].append(1)
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

all_card_numbers = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

is_continue = want_to_play()
while is_continue:
    play_game()
    is_continue = want_to_play()



