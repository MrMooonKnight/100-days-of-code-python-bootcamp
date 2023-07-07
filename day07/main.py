import random
import time
from words import word_list
from art import stages, logo
from replit import clear

lives = 6

print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for i in range(word_length):
    display += "_"

end_of_game = False

time.sleep(2)

while not end_of_game:
    clear()
    print(f"{' '.join(display)}")  
    print(stages[lives])

    guess = input("Guess a letter : ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter

    if guess not in chosen_word:
        print(f"Oops, wrong guess </3")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose :(")

   

    if "_" not in display:
        end_of_game = True
        print('You Win :D')

    

