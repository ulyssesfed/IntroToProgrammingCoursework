import random

ROCK = 0
PAPER = 1
SCISSORS = 2

# Mapping from string to choice
STR_TO_CHOICE = {
    'r': ROCK,
    'p': PAPER,
    's': SCISSORS
}

# Mapping from choice to string
CHOICE_TO_STR = {
    ROCK: 'Rock',
    PAPER: 'Paper',
    SCISSORS: 'Scissors'
}

userScore = 0
computerScore = 0

# Play the game
for roundNumber in range(1, 6):
    # Check if the game is already decided
    if max(userScore, computerScore) > 2:
        break

    print(f"Round {roundNumber}:")
    print(f"Current scores -> Computer: {computerScore}, Player: {userScore}")

    while True:
        userInput = input("Enter your choice (R for Rock, P for Paper, S for Scissors): ").lower()
        if userInput in STR_TO_CHOICE:
            break
        else:
            print("Invalid input. Please try again.")

    # Convert string to choice
    userChoice = STR_TO_CHOICE[userInput]

    computerChoice = random.randint(0, 2)

    print(f"You entered: {userInput}, which represents: {CHOICE_TO_STR[userChoice]}")
    print(f"Computer randomly picked: {CHOICE_TO_STR[computerChoice]}")

    # Determine the winner of the round
    if userChoice == computerChoice:
        print("This round is a draw!")
    elif (userChoice - computerChoice) % 3 == 1:
        print("You win this round!")
        userScore += 1
    else:
        print("Computer wins this round!")
        computerScore += 1

    print()

# Print the final outcome
print("Final Outcome")
print(f"Computer: {computerScore}")
print(f"Player: {userScore}")
if userScore > computerScore:
    print("You win!")
elif userScore < computerScore:
    print("Computer wins!")
else:
    print("It's a draw!")
