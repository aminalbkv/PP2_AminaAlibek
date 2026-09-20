import random


# Here is the player's name
player_name = input("Hello! What is your name?\n")


# Here is a random number between 1 and 20
secret_number = random.randint(1, 20)


# Here is the number of guesses
guess_count = 0


print(
    "Well,",
    player_name + ",",
    "I am thinking of a number between 1 and 20."
)


# Here is the guessing loop
while True:

    guess = int(input("Take a guess.\n"))
    guess_count += 1

    if guess < secret_number:
        print("Your guess is too low.")

    elif guess > secret_number:
        print("Your guess is too high.")

    else:
        print(
            "Good job,",
            player_name + "!",
            "You guessed my number in",
            guess_count,
            "guesses!"
        )
        break