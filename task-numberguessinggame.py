import random

def play_guessing_game():
    print("Welcome to the Number Guesser Game!")
    print("I've selected a number between 1 and 100.")
    max_attempts = 10
    attempts = 0
    secret_number = random.randint(1, 100)

    while attempts < max_attempts:
        try:
            guess = int(input(f"\nEnter your guess (Attempt {attempts + 1}): "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Attempts left:", max_attempts - attempts)
        elif guess > secret_number:
            print("Too high! Attempts left:", max_attempts - attempts)
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
    else:
        print(f"\nSorry, you've run out of attempts. The secret number was {secret_number}.")

if __name__ == "__main__":
    play_guessing_game()
