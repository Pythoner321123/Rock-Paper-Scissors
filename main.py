import random

our_message = """Rock-Paper-Scissors. \n
Choose A, B, or C. \n
A = Rock, B = Paper, C = Scissors"""

lista = ["Rock", "Paper", "Scissors"]

valid_player_choice = ["a", "b", "c", "α", "β", "ψ", "rock", "paper", "scissors"]

score = 1

# Mapping dictionary for full names
full_names = {
    'Rock': {'a': 'Rock', 'α': 'Rock', 'rock': 'Rock'},
    'Paper': {'b': 'Paper', 'β': 'Paper', 'paper': 'Paper'},
    'Scissors': {'c': 'Scissors', 'ψ': 'Scissors', 'scissors': 'Scissors'}
}

while True:
    print(our_message)
    luck = random.choice(lista)
    user_input = input().lower()

    if user_input not in valid_player_choice:
        print("Invalid input")
    else:
        for choice, options in full_names.items():
            if user_input in options:
                user_choice = choice
                break
        else:
            print("Invalid input")
            continue

        if user_choice == luck:
            print("It's a tie")
        elif (user_choice == 'Rock' and luck == 'Scissors') or \
             (user_choice == 'Paper' and luck == 'Rock') or \
             (user_choice == 'Scissors' and luck == 'Paper'):
            print("You won!")
            score += 1
            print("Your score is ", score)
        else:
            print("You lost!")
            score -= 1
            print("Your score is ", score)

        print("You picked", user_choice)
        print("I picked", luck)

    play_again = input("Do you want to try again? (yes/no): ").lower()
    if play_again != 'yes':
        if score > 0:
            print("You won! Your score is: ", score)
            print("Thanks for playing!")
        if score == 0:
            print("It's a tie.")
            print("Thanks for playing!")
        if score < 0:
            print("You lost.")
            print("Thanks for playing!")
        break
