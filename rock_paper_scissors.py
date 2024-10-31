import random

# Function to get the computer's choice randomly
def get_computer_choice():
    # Define possible choices
    choices = ["rock", "paper", "scissors"]
    # Randomly select one choice
    return random.choice(choices)

# Function to determine the winner
def get_winner(player_choice, computer_choice):
    # Check for a tie
    if player_choice == computer_choice:
        return "It's a tie!"
    # Winning conditions for the player
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "scissors" and computer_choice == "paper") or
        (player_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    # If none of the above, the player loses
    else:
        return "You lose!"

# Main function to manage the game loop and handle user input
def main():
    print("Welcome to Rock, Paper, Scissors!")
    
    # Infinite loop to continue the game until the player decides to quit
    while True:
        # Prompt the player to enter their choice
        player_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
        
        # If player wants to quit, break the loop
        if player_choice == "quit":
            print("Thanks for playing!")
            break
        # Validate the player's choice
        elif player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue  # Skip to the next iteration if input is invalid

        # Get a random choice for the computer
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        # Determine the game result
        result = get_winner(player_choice, computer_choice)
        # Print the result (win, lose, or tie)
        print(result)


if __name__ == "__main__":
    main()
