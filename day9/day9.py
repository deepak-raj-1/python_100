from art import logo
print(logo)
bid_data = {}
bidding_finished = False
while not bidding_finished:
    name = input("What is your name? :")
    bid = int(input("What is your bid? : $"))
    bidders = input("Are there any other bidders? Type 'yes or 'no'.").lower()
    if bidders == "no":
        bidding_finished = True
        print("\n" * 50)
    else:
        print("\n" * 50)
    bid_data[name] = bid
max_bid = max(bid_data.values())
max_bidder_names = []
for name, bid in bid_data.items():
    if bid == max_bid:
        max_bidder_names.append(name)
if len(max_bidder_names) > 1:
    print("It's a tie!")
    print("The winners are:", ", ".join(max_bidder_names))
    print(f"Winning bid: ${max_bid}")
else:
    print(f"The winner is {max_bidder_names[0]} with a bid of ${max_bid}")