import random
def play_rps():
    user = input("Your turn 'r' for rock,'p' for paper, 's' for scissor: ")
    computer = random.choice(['r','p','s'])
    
    if user == computer:
        print("Match Tied!")
    
    if is_triumph(user, computer):
        print("You\'ve won the match!")
    else: print("You lost!")
    
def is_triumph(player, opponent): # returns true if player wins 
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play_rps())