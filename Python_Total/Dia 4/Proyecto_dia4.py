from random import *

username = input("Write your name:")

print(f"Ok {username}, I have thought in a number between 1 & 100, and you have only 8 attempts to guess. Can you "
      f"guess it?")

number = randint(1, 101)

attempts = 0

while attempts < 8:
    guess = int(input(f"Guess the number {username}:"))
    attempts += 1

    if guess not in range(1, 101):
        print("Only numbers from 1 to 100 are allowed")
    elif guess < number:
        print("Incorrect answer and chosen number is less than the secret number.")
    elif guess > number:
        print("wrong answer and chosen number is greater than the secret number.")
    elif guess == number:
        print(f"You guessed the secret number ({number}) in {attempts} attempts!")
        break
else:
    print(f"Sorry you've run out of try!, The number was {number}")
