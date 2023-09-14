import random
from words import words
import string 
print("Let's play Hangman Game!!")
def get_valid_words(words):
    word = random.choice(words) # chooses word randomly from the imported list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_words(words)
    word_letters = set(word) #letters in the word as a set
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #user guessed letters
    lives = 5
    
    # getting user input
    while len(word_letters) > 0 and lives > 0:
        #join : displays list of letters as string
        print('You have',lives,'lives left and you have used these letters',' '.join(used_letters))
        
    # Displaying current word
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word:',' '.join(word_list))
        
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives = lives -1;
                print("\nyour letter,", user_letter,'is not in the word.')
        elif user_letter in used_letters:
            print("\nyou have already used that letter. Guess another letter.") 
        else:       
            print("\nThat's not a valid letter")
    
    # lives == 0 or length of word_letters == 0
    if lives == 0:
        print("You died, sorry. The word was", word)
    else:
        print('Yay! You guessed the word',word,'!!')
if __name__ == '__main__':
    hangman()