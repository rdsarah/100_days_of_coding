import art
print(art.logo)

loop = True
details = {}
while loop:
    name = input("Please type in your name: ")
    bid = int(input("Please type in your bid: $ "))
    details[name] = bid
    question = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if question=="no":
        loop = False
    elif question=="yes":
        print("\n"*20)
highest = max(details, key = details.get)
print(f"The winner is {highest} with a bid of ${details[highest]}")
