import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "You lose!"

def display_options():
    print("\nOptions:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

def play_game():
    print("Welcome to Rock, Paper, Scissors Game!")
    print("--------------------------------------")

    user_score = 0
    computer_score = 0

    while True:
        display_options()

        try:
            user_choice_num = int(input("Enter the number of your choice (1-3): "))
            if user_choice_num not in [1, 2, 3]:
                print("Invalid choice. Please enter a number between 1 and 3.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        choices = ["rock", "paper", "scissors"]
        user_choice = choices[user_choice_num - 1]
        computer_choice = random.choice(choices)

        print(f"\nYour choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1

        print(f"\nScore - You: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
