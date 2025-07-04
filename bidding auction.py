# bidding auction
bids = []


def get_highest_bid(bids):
    highest = bids[0]
    for bid in bids:
        if bid["amount"] > highest["amount"]:
            highest = bid    
    return highest
        

def place_bid():
    print("\nWelcome to the bid auction ceremony!")
    print("what is your object?")
    object_name = input("Object name: ")
    print("What is your name?")
    bidder_name = input("Bidder name: ")
    print("What is your bid amount?")
    bid_amount = int(input("Bid amount:$ "))
    bids.append({
        "object": object_name,
        "bidder": bidder_name,
        "amount": bid_amount
    })
    if bid_amount == 0:
        print("Invalid input")    
        return
    
    print(f"Bid placed successfully for {object_name} by {bidder_name} with amount ${bid_amount}.")
    while True:
        further_bid = input("there is higher amount rather than this (yes/no): ").lower()
        if further_bid == "yes":
            print("enter your name")
            bidder_name = input("Bidder name: ")
            print("enter your bid amount")
            bid_amount = int(input("Bid amount:$ "))
            bids.append({
                "bidder": bidder_name,
                "amount": bid_amount
            })
        elif further_bid == "no":
            highest_bid = get_highest_bid(bids)
            print(f"\nThe winner of the auction is {highest_bid["bidder"]} with a bid amount ${highest_bid["amount"]}")
            print(f"s/he wins the {object_name} with a ${highest_bid["amount"]}")
            print("Thank You for coming in the auction ceremony!")
            break
        else:
            continue
  




if __name__ == "__main__":
    place_bid()    
