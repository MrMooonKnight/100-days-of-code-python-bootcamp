from replit import clear
from art import logo

def findWinner(bidding_record):
  highestBid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highestBid:
      highestBid = bid_amount
      winner = bidder
  print(f"The Winner Of The Auction Is {winner} with a bid of ${highestBid}")

print(logo)

bids = {}

finished = False

while not finished :
  name = input("What is your name? ")
  price = int(input("What is your bid? $"))
  bids[name] = price
  should_continue = input("Are there any more bidders? Type 'yes' or 'no'.").lower()
  if should_continue == "no":
    clear()
    print(logo)
    finished = True
    findWinner(bids)
  elif should_continue == "yes":
    clear()
  

