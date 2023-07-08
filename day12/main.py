from art import logo
import random

print(logo)
print("I'm Thinking Of a Number Between 1 and 100.")

difficulty = input("Choose a Difficulty. Type 'easy' or 'hard' : ").lower()

if difficulty == "easy":
  attempts = 10
elif difficulty == "hard":
  attempts = 5
print(f"You have {attempts} to guess the number.")
 
NUMBER = random.randint(1,100)

while(attempts > 0) :
  guess = int(input("Make a Guess : "))
  if (guess == NUMBER):
    print(f"You Have Won The Game! The Number Was {NUMBER}.")
    break
  elif (guess < NUMBER):
    print("Too Low.")
  elif (guess > NUMBER):
    print("Too High.")
  attempts -=1
  if(attempts == 0) :
    print(f"You Have Lost The Game! The Number Was {NUMBER}.")
  else:
    print(f"You Have {attempts} Left To Guess The Number.")
