
import random

def main():
    player1 = 0
    player1Wins = 0
    player2 = 0
    player2Wins = 0
    rounds = 1

    while rounds != 6:
        print("round" + str(rounds))
        player1 = roll_dice()
        player2 = roll_dice()
        print(f"player 1 Roll: " + str(player1))
        print("player 2 Roll: " + str(player2))

        if player1 == player2:
            print("Draw\n")
        elif player1 > player2:
            player1Wins=player1Wins+1
            print("Player 1 won game\n")
        else:
            player2Wins=player2Wins+1
            print("Player 2 won game\n")
        rounds = rounds+1
    if player1Wins == player2Wins:
        print("Draw")
    elif player1Wins > player2Wins:
        print("Player 1 wins! with Rounds Won of " + str(player1Wins))
    else:
        print("Player 2 wins! with Rounds won of "+str(player2Wins))


def roll_dice():
    number = random.randint(1, 6)
    if number == 1:
        print("----------")
        print("|         |")
        print("|    O    |")
        print("|         |")
        print("----------")
    if number == 2:
        print("----------")
        print("|         |")
        print("| O     O |")
        print("|         |")
        print("----------")
    if number == 3:
        print("----------")
        print("|    O    |")
        print("|    O    |")
        print("|    O    |")
        print("----------")

    if number == 4:
        print("----------")
        print("| O     O |")
        print("|         |")
        print("| O     O |")
        print("----------")

    if number == 5:
        print("----------")
        print("| O     O |")
        print("|    O    |")
        print("| O     O |")
        print("----------")
    if number == 6:
        print("----------")
        print("| O      O |")
        print("| O      O |")
        print("| O      O |")
        print("----------")
    return number


main()

