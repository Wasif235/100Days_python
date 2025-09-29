def find_highest_bidder(bidding_dict):
      winner=""
      highest_bid=0
      for key in bidding_dict:
         bid_amount=bidding_dict[key]
         if bid_amount>highest_bid:
            highest_bid = bid_amount
            winner= key
         
      print(f" The winner is {winner} with a bid of ${highest_bid}") 
print("welcome to Auction")
again=True
bids={}
while again is not False:
   name=input("Enter your name:\n")
   price=int(input("Aution price:\n"))
   bids[name]=price
   print("Are there any other bidder?")
   con=input("type 'yes' or 'no'\n")
   if con == 'no':
      again=False
      find_highest_bidder(bids)   
      
   elif con== 'yes':
      print("\n"*20)
 
               
   
   