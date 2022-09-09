# Rock, Paper, Scissors game

Play_again = True
while Play_again:

    P1 = input('Player 1: ')
    P2 = input('Player 2: ')

    outcomes = {
        "Rock": 1,
        "Paper": 2,
        "Scissors": 3
    }

    P1 = outcomes[P1]
    P2 = outcomes[P2]

    if P2 - P1 == 1 or P2 - P1 == -2:
        print("Player 2 wins!")

    if P2 - P1 == -1 or P2 - P1 == 2:
        print("Player 1 wins!")

    if P2 == P1:
        print("It's a tie!")

    answer = input("Want to play again?:")

    if answer == "No":
        Play_again = False
