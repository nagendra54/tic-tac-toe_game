import random
import time

def default():
    print("\nWelcome! Let's play TIC TAC TOE!\n")

def rules():
    print("The board will look like this!")
    print("The positions of this 3 x 3 board is same as the right side of your keyboard.\n")
    print(" 7 | 8 | 9 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 1 | 2 | 3 ")
    print("\nYou just have to input the position (1-9).")

def play():
    return input("\nAre you ready to play the game? Enter [Y]es or [N]o.\t").upper().startswith('Y')

def names():
    p1_name = input("\nEnter NAME of PLAYER 1:\t").capitalize()
    p2_name = input("Enter NAME of PLAYER 2:\t").capitalize()
    return p1_name, p2_name

def choice(p1_name):
    while True:
        p1_choice = input(f"\n{p1_name}, do you want to be X or O?\t")[0].upper()
        if p1_choice in ['X', 'O']:
            break
        print("INVALID INPUT! Please Try Again!")
    p2_choice = 'O' if p1_choice == 'X' else 'X'
    return p1_choice, p2_choice

def first_player():
    return random.choice((0, 1))

def display_board(board, avail):
    print("    " + " {} | {} | {} ".format(board[7],board[8],board[9]) + "            " + " {} | {} | {} ".format(avail[7],avail[8],avail[9]))
    print("    " + "-----------" + "            " + "-----------")
    print("    " + " {} | {} | {} ".format(board[4],board[5],board[6]) + "            " + " {} | {} | {} ".format(avail[4],avail[5],avail[6]))
    print("    " + "-----------" + "            " + "-----------")
    print("    " + " {} | {} | {} ".format(board[1],board[2],board[3]) + "            " + " {} | {} | {} ".format(avail[1],avail[2],avail[3]))

def player_choice(board, name, choice):
    while True:
        try:
            position = int(input(f'\n{name} ({choice}), Choose your next position (1-9): '))
            if position in range(1, 10) and space_check(board, position):
                print("\n")
                return position
            else:
                print("INVALID INPUT. Position is taken or out of range. Try again!")
        except:
            print("INVALID INPUT. Please enter a number between 1-9.")

def CompAI(board, name, choice):
    position = 0
    possibilities = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    for let in ['O', 'X']:
        for i in possibilities:
            boardCopy = board[:]
            boardCopy[i] = let
            if win_check(boardCopy, let):
                return i
    openCorners = [x for x in possibilities if x in [1, 3, 7, 9]]
    if openCorners:
        return random.choice(openCorners)
    if 5 in possibilities:
        return 5
    openEdges = [x for x in possibilities if x in [2, 4, 6, 8]]
    if openEdges:
        return random.choice(openEdges)
    return random.choice(possibilities)

def place_marker(board, avail, choice, position):
    board[position] = choice
    avail[position] = ' '

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    return all(board[i] != ' ' for i in range(1, 10))

def win_check(board, choice):
    return (
        (board[1] == board[2] == board[3] == choice) or
        (board[4] == board[5] == board[6] == choice) or
        (board[7] == board[8] == board[9] == choice) or
        (board[1] == board[4] == board[7] == choice) or
        (board[2] == board[5] == board[8] == choice) or
        (board[3] == board[6] == board[9] == choice) or
        (board[1] == board[5] == board[9] == choice) or
        (board[3] == board[5] == board[7] == choice)
    )

def replay():
    return input('\nDo you want to play again? Enter [Y]es or [N]o: ').lower().startswith('y')
print("Hii this is tic-tac-toe...")
input("Press ENTER to start the game!")
default()
rules()
while True:
    theBoard = [' '] * 10
    available = [str(num) for num in range(10)]

    print("\n[0]. Player vs. Computer")
    print("[1]. Player vs. Player")
    print("[2]. Computer vs. Computer")

    while True:
        try:
            mode = int(input("\nSelect an option [0]-[2]: "))
            if mode in [0, 1, 2]:
                break
            else:
                print("Please enter 0, 1, or 2.")
        except:
            print("Invalid input. Please enter a number.")

    if mode == 1:
        p1_name, p2_name = names()
        p1_choice, p2_choice = choice(p1_name)
    elif mode == 0:
        p1_name = input("\nEnter NAME of PLAYER who will go against the Computer:\t").capitalize()
        p2_name = "Computer"
        p1_choice, p2_choice = choice(p1_name)
    else:
        p1_name = "Computer1"
        p2_name = "Computer2"
        p1_choice, p2_choice = "X", "O"

    print(f"\n{p1_name}: {p1_choice}")
    print(f"{p2_name}: {p2_choice}")

    turn = p1_name if first_player() == 0 else p2_name
    print(f"\n{turn} will go first!")

    play_game = True if mode == 2 else play()
    if mode == 2:
        input("\nThis is going to be fast! Press Enter for the battle to begin!\n")

    while play_game:
        current_player, current_choice = (p1_name, p1_choice) if turn == p1_name else (p2_name, p2_choice)

        display_board(theBoard, available)

        if "Computer" in current_player:
            position = CompAI(theBoard, current_player, current_choice)
            print(f'{current_player} ({current_choice}) has placed on {position}\n')
            time.sleep(1)
        else:
            position = player_choice(theBoard, current_player, current_choice)

        place_marker(theBoard, available, current_choice, position)

        if win_check(theBoard, current_choice):
            display_board(theBoard, available)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(f'\n\nCONGRATULATIONS {current_player}! YOU HAVE WON THE GAME!\n\n')
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            play_game = False
        elif full_board_check(theBoard):
            display_board(theBoard, available)
            print("~~~~~~~~~~~~~~~~~~")
            print('\nThe game is a DRAW!\n')
            print("~~~~~~~~~~~~~~~~~~")
            break
        else:
            turn = p1_name if current_player == p2_name else p2_name

    if not replay():
        break

print("\n\n\t\t\tTHE END!")

