def find_auction_winner():
    highest_bid = 0
    winner = ""
    for name in final_bids:
        if final_bids[name] > highest_bid:
            highest_bid = final_bids[name]
            winner = name

    print(f"The winner is {winner} with a bid of {highest_bid}")

print("Welcome to the Secret Auction Program")
final_bids = {}

bidders_exists = True

while bidders_exists:
    name = input("What is your name: ")
    bid = float(input("What is your bid: INR "))
    final_bids[name] = bid

    more_bidders = input("Are there any other bids/bidders? (yes/no): ")
    print("\n" * 35)
    bidders_exists = True if more_bidders.lower() == "yes" else False

find_auction_winner()
