"""
PS No.: 52
Project Title: Rock Paper Scissors
Bachelor of Technology - Computer Science and Engineering
Language: Python 3
Concepts: Conditions, Functions, Random

Problem Statement:
Create a console game where the player plays three rounds of Rock, Paper, Scissors
against the computer, the winner of each round is shown, and the final result of
the match is declared.
"""

import random

# ==============================================================================
# CONFIGURATION / TEST MODE
# ==============================================================================
# As specified in PS No. 52:
# "For testing, the computer's choices in the 3 rounds are fixed as Scissors, Rock, Paper."
# When TEST_MODE is True, the fixed sequence is used to pass college test cases.
# When TEST_MODE is False, random.choice() from the random module is used.
TEST_MODE = True


def get_computer_choice(round_number):
    """
    Determines computer choice.
    Uses fixed sequence ['scissors', 'rock', 'paper'] in TEST_MODE,
    or random module in normal mode.
    """
    if TEST_MODE:
        fixed_choices = ["scissors", "rock", "paper"]
        return fixed_choices[(round_number - 1) % len(fixed_choices)]
    else:
        return random.choice(["rock", "paper", "scissors"])


def get_player_choice():
    """
    Prompts player for their choice and validates input.
    Repeats until player enters 'rock', 'paper', or 'scissors'.
    """
    valid_choices = ["rock", "paper", "scissors"]
    while True:
        choice = input("Enter rock, paper, or scissors: ").strip().lower()
        if choice in valid_choices:
            return choice
        print("Invalid choice. Enter rock, paper or scissors.")


def determine_winner(player, computer):
    """
    Compares player and computer choices using conditions and returns the winner.
    Rock beats Scissors, Scissors beats Paper, Paper beats Rock.
    """
    if player == computer:
        return "Draw"
    elif (
        (player == "rock" and computer == "scissors")
        or (player == "scissors" and computer == "paper")
        or (player == "paper" and computer == "rock")
    ):
        return "You win"
    else:
        return "Computer wins"


def play_match():
    """
    Plays a 3-round match of Rock, Paper, Scissors.
    Tracks round results, updates scores, and prints final match result.
    """
    round_summaries = []
    player_score = 0
    computer_score = 0
    draws = 0

    # 3-round loop
    for round_num in range(1, 4):
        player_choice = get_player_choice()
        computer_choice = get_computer_choice(round_num)
        winner = determine_winner(player_choice, computer_choice)

        round_summaries.append(f"Round {round_num}: {winner}")

        if winner == "You win":
            player_score += 1
        elif winner == "Computer wins":
            computer_score += 1
        else:
            draws += 1

    # Display round-by-round summary
    print(" | ".join(round_summaries))

    # Display score summary
    print(f"You {player_score} | Computer {computer_score} | Draws {draws}")

    # Declare final match result
    if player_score > computer_score:
        print("Result: You win the match!")
    elif computer_score > player_score:
        print("Result: Computer wins the match.")
    else:
        print("Result: Match drawn.")


def main():
    """
    Main game loop. Runs matches and handles 'Play again?' prompt.
    """
    while True:
        play_match()

        # Input validation for Play again
        play_again = input("Play again? (y/n): ").strip().lower()
        if play_again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
