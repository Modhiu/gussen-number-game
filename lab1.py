import random

def main():
  """Runs a number guessing game."""
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 9.99.")
  print("You have 5 attempts to guess it.")

  # Generate the random number
  target_number = random.randint(1, 100)

  # Keep track of the number of guesses
  guesses_left = 5

  # Start the game loop
  while guesses_left > 0:
    # Get the user's guess
    guess = int(input("Guess the number: "))

    # Check the guess
    if guess == target_number:
      print("Congratulations! You guessed the number in", 5 - guesses_left, "attempts!")
      break
    elif guess < target_number:
      print("Too low! Try again. Attempts left:", guesses_left - 1)
    else:
      print("Too high! Try again. Attempts left:", guesses_left - 1)

    # Decrement the number of guesses left
    guesses_left -= 1

  # Game over message
  if guesses_left == 0:
    print("Sorry, you ran out of guesses. The number was", target_number)

  # Ask the user if they want to play again
  play_again = input("Do you want to play again? ")
  if play_again.lower() == "y":
    main()

if __name__ == "__main__":
  main()
