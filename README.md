Rock, Paper, Scissors in Python

This is a simple command-line Rock, Paper, Scissors game implemented in Python. It allows you to play against the computer by choosing rock, paper, or scissors.
Features

    Play against the computer
    Simple command-line interface
    Keeps track of the game result

Requirements

    Python 3.x

How to Run

Clone the Repository:

    git clone git@github.com:OkuhleMwelase/rock_paper_scissors.git
    cd rock_paper_scissors


Run the Script:

    python rock_paper_scissors.py

How to Play

    When prompted, enter your choice: rock, paper, or scissors.
    The computer will randomly select one of the three options.
    The script will compare your choice with the computer's choice and display the result.
    Type quit to exit the game.

Example Gameplay

Welcome to Rock, Paper, Scissors!
Enter rock, paper, or scissors (or 'quit' to exit): rock
Computer chose: paper
You lose!

Enter rock, paper, or scissors (or 'quit' to exit): paper
Computer chose: rock
You win!

Enter rock, paper, or scissors (or 'quit' to exit): scissors
Computer chose: scissors
It's a tie!

Enter rock, paper, or scissors (or 'quit' to exit): quit
Thanks for playing!

Code Structure

    get_computer_choice(): Function to randomly select the computer's choice.
    get_winner(player_choice, computer_choice): Function to determine the result of the game based on the player's and computer's choices.
    main(): Main function to manage the game loop and handle user input.

License

This project is licensed under the MIT License. See the LICENSE file for details.
Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.
