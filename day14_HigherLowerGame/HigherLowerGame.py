from game_data import data
import random, art

print(art.logo)

# game = True
# score = 0
# while game:
#     print(f"You're right! Current score: {score}")
#     sample =  random.sample(data, 2)
#     A, B = sample[0], sample[1]

#     print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
    
#     print(art.vs)

#     print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}.")
#     choice = input("Who has more follower? Type 'A' of 'B': ").upper()
#     if choice=="A" and A['follower_count'] > B['follower_count']:
#         score +=1 
#     elif choice=="B" and A['follower_count'] < B['follower_count']:
#         score +=1 
#     else:
#         game = False
# print(f"Sorry, that's wrong. Final score: {score}")

def format(account):
    """Takes the account data and returns a printable format"""
    account_name = account['name']
    account_desc = account['description']
    account_country = account['country']
    return (f"Compare A: {account_name}, a {account_desc}, from {account_country}.")

def compare(choice, a,b):
    """Compares the choices to check if the user is correct"""
    if a > b:
        return choice=="A"
    else:
        return choice=="B"

score = 0
game = True
B = random.choice(data)

while game:
    A = B
    B = random.choice(data)
    print(f"Compare A: {format(A)}")
    print(art.vs)
    print(f"Against B: {format(B)}")
    choice = input("Who has more follower? Type 'A' of 'B': ").upper()
    is_correct = compare(choice, A['follower_count'], B['follower_count'])

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, you're wrong. Final score {score}")
        game = False
