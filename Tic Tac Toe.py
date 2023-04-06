
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def print_board():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])

def check_win():
    # Check rows
    if board[0] == board[1] == board[2] != ' ' or \
       board[3] == board[4] == board[5] != ' ' or \
       board[6] == board[7] == board[8] != ' ':
        return True
    # Check columns
    elif board[0] == board[3] == board[6] != ' ' or \
         board[1] == board[4] == board[7] != ' ' or \
         board[2] == board[5] == board[8] != ' ':
        return True
    # Check diagonals
    elif board[0] == board[4] == board[8] != ' ' or \
         board[2] == board[4] == board[6] != ' ':
        return True
    else:
        return False

def play_game():
    PlayerOne = input("Player 1 will be X. Name: ")
    PlayerTwo = input("Player 2's will be O. Name: ")
    Turn = PlayerOne
    while True:
        print_board()
        print("It's your turn, " + Turn + ".")
        move = int(input("Enter a number from 1-9 to make a move: ")) - 1
        if board[move] == ' ':
            if Turn == PlayerOne:
             board[move] = "X"
            if Turn == PlayerTwo:
             board[move] = "O"
            if check_win():
                print_board()
                print(Turn + " wins!")
                break
            elif ' ' not in board:
                print_board()
                print("It's a tie!")
                break
            else:
                Turn = PlayerTwo if Turn == PlayerOne else PlayerOne
        else:
            print("That square is already occupied. Please choose another.")

play_game()
