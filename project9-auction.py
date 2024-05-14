# Rule :- here one bidder dont know other bidder price, until the end of auction

def find_winner(bidder_details):
    highest_bid = 0
    winner = ""
    for bidder in bidder_details:
        if bidder_details[bidder]>highest_bid:
            highest_bid = bidder_details[bidder]
            winner = bidder
    print(f"the winner is {winner} with a bid price of {highest_bid}")
    
next_bid = True

bidders_data = {}
while next_bid != False:
    name = input("please enter your name \t ")
    price = int(input("please enter your bid value \t "))
    bidders_data[name]=price     # storing the vales in a dictionary 
    next_bid = input("Is their next bidder available yes or no ").lower()
    if next_bid == "no":
        find_winner(bidders_data)
        break
        
    


