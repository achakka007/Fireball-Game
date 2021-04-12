import random


# import time
# Fireball Game


def main():
    moves = ["Charge", "Block", "Fireball", "Iceball", "Windslash", "Terranova", "Lightningbolt"]
    max_moves = len(moves) - 1
    game_over = False
    player1move = 0
    player2move = 0
    player1input = ""
    player1charge = 0
    player2charge = 0

    print("""Hello, Player 1. Choose from""", list_to_string(moves))
    print("Type the name of the move you would like to choose")
    print("If you need help type Help")
    print()

    while not game_over:
        # INPUT
        player1input = input("What's your move?")  # PLAYER MOVE

        if player1input == "Shadow Monarch":  # Special Case
            print("You cannot be beaten. Player 2 has given up ;)")
            break
        if player1input == "Help":
            print("Choose from", list_to_string(moves))
            print("Player 1 Charge:", player1charge)
            print()
            continue

        pos = 0
        for i in moves:
            if player1input == i:
                player1move = pos
            else:
                pos += 1

        if player2charge < max_moves:  # BOT MOVE
            if player1charge == 0:  # Player 1 cannot block
                if player2charge >= 2:  # Player 2 attacks if possible
                    player2move = random.randint(2, player2charge)
                else:  # Player 2 cannot attack so charges instead
                    player2move = 0
            elif player1charge == 1:  # Player 1 can block or charge so player 2 charges or attacks
                if player2charge < 2:
                    player2move = 0
                else:
                    player2move = 0 if random.randint(0, 9) < 5 else (random.randint(2, player2charge))
            else:  # Player can do anything so player 2 does anything possible
                player2move = random.randint(0, player2charge)
        else:  # Player 2 can do anything
            if player1charge == 0:  # Player 1 cannot block so Player 2 attacks
                player2move = random.randint(2, max_moves)
            elif player2charge == 1:  # Player 1 can block or charge so player 2 charges or attacks
                player2move = 0 if random.randint(0, 9) < 5 else (random.randint(2, max_moves))
            else:  # Player 2 does anything
                player2move = random.randint(0, max_moves)

        # INPUT CHECK
        if player1move > player1charge:
            print("Invalid move")
            print()
            continue
        assert (player1move <= player1charge) and (player2move <= player2charge)

        # GAME  # Missing Block Mechanism
        if player1move > player2move:  # Player 1 can win
            if player2move == 1:  # Player 2 blocks
                print("---Blocked---")
                player1charge -= player1move
                player2charge -= 1
            elif player1move == 1 and player2move == 0:  # Special Case - P1 Blocks P2 Charges
                player1charge -= 1
                player2charge += 1
            else:  # Player 1 does win
                game_over = True
                # time.sleep(1)
                print("Player 1 Wins!!!")

        if player2move > player1move:  # Player 2 can win
            if player1move == 1:  # Player 1 blocks
                print("---Blocked---")
                player1charge -= 1
                player2charge -= player2move
            elif player2move == 1 and player1move == 0:  # Special Case - P2 Blocks P1 Charges
                player2charge -= 1
                player1charge += 1
            else:  # Player 2 does win
                game_over = True
                # time.sleep(1)
                print("Player 2 Wins!!!")

        if player1move == player2move:  # Tie
            if player1move == 0:  # Both charge
                player1charge += 1
                player2charge += 1
            else:  # Both use equal attacks
                player1charge -= player1move
                player2charge -= player2move

        # Print Moves
        print("Player 1 played", moves[player1move])
        print("Player 2 played", moves[player2move])
        # print(player1charge)
        print()


def list_to_string(l):
    rv = "0-" + l[0]
    count = 1
    for i in l:
        if i == "Charge":
            continue
        rv = rv + ", " + str(count) + "-" + i
        count += 1
    return rv


if __name__ == "__main__":
    main()
