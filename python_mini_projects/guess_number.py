import random
def guess(a):
    random_number = random.randint(1,a);
    guess = 0;
    while guess != random_number:
       guess = int(input(f"Guess a number between 1 and {a}: "))
       if guess < random_number:
           print("Its Too Low. Guess again!")
       elif guess > random_number:
           print("It's Too High. Guess again!")
    print(f"Woah! You guessed the {random_number} correctly")

def computer_guess(y):
    low = 1
    high = y
    comment = ''
    while comment != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        comment = input(f'Is {guess} number is too high(H) or too low(L) or correct(C)')
        if comment == 'h':
            high = guess - 1;
        elif comment == 'l':
            low = guess + 1;
    print(f"Woaho you guessed {guess} correctly")        
            
         
         
computer_guess(89)  