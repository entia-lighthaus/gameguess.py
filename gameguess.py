import random

def play_game():
    secret_number = random.randint(1, 10)
    guess_count = 0

    print("I'm thinking of a number between 1 and 10. Can you guess it?")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            guess_count += 1

            match guess:
                case _ if guess == secret_number:
                    print(f"🎉 Congratulations, you guessed it in {guess_count} tries!")
                    break
                case _ if guess > secret_number:
                    print("📈 Oops, your guess is a bit high. Try again!")
                case _ if guess < secret_number:
                    print("📉 Nope, your guess is a bit low. Give it another shot!")
        except ValueError:
            print("❌ Please enter a valid number!")

# Game loop with replay option
while True:
    play_game()
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! 👋")
        break
