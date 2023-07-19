from replit import clear
import art 
#HINT: You can call clear() to clear the output in the console.
Again = False
logo = art.logo
dic_of_bids = {}

print(logo)
print("Welcome to the secret auction program.")

def highest_bid(record_bids):
  mx_bid = 0
  winner = ""
  for bidder in record_bids:
      bid_value = record_bids[bidder]
      if bid_value > mx_bid:
          mx_bid = bid_value
          winner = bidder
  print(f"The winner is {winner} with a bid of {mx_bid}$.")
  
while not Again:
    name = input("What is your name?: ")
    bid =  int(input("What's your bid?: $"))
    dic_of_bids[name] = bid
    other_bidders = input("Are there any other bidders? Types \'yes\' or \'no\'.\n")
    if other_bidders == "no":
        Again = True
        clear()
        highest_bid(dic_of_bids)
        
    else:
        clear()  
     

