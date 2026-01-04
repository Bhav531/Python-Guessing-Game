import random

print("This is a guessing game. I will be thinking of a random number and you will have 6 attempts to guess it.")

number = random.randint(1, 20)
attempts = 6
guessed_numbers = set()

while attempts > 0:
    guess = int(input("Guess the number between 1 and 20: "))
    
    if guess in guessed_numbers:
        print(f"You already guessed {guess}. Try a different number.")
        continue
    
    guessed_numbers.add(guess)
    attempts -= 1
    
    if guess == number:
        print(f"Congratulations! You guessed the number {number} correctly.")
        break
    elif guess < number:
        print(f"Too low. You have {attempts} guesses remaining.")
    else:
        print(f"Too high. You have {attempts} guesses remaining.")
else:
    print(f"Sorry, you ran out of attempts. The number was {number}.")
