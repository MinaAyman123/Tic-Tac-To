def create_empty_board():
    board = [['1', '2', '3'],
             ['4', '5', '6'],
             ['7', '8', '9']]
    return board

def show_board(board):
    for row in board:
        print('\t'.join(row))
    print()

def set_players():
    from random import choice
    player1 = choice(['X', 'O'])
    player2 = 'O' if player1 == 'X' else 'X'
    return player1, player2

def take_input(board, player):
    while True:
        player_input = input('Please Enter a number between 1-9 representing an empty position: ')
        if player_input == '1' and board[0][0].isdigit():
            board[0][0] = player
            break
        elif player_input == '2' and board[0][1].isdigit():
            board[0][1] = player
            break
        elif player_input == '3' and board[0][2].isdigit():
            board[0][2] = player
            break
        elif player_input == '4' and board[1][0].isdigit():
            board[1][0] = player
            break
        elif player_input == '5' and board[1][1].isdigit():
            board[1][1] = player
            break
        elif player_input == '6' and board[1][2].isdigit():
            board[1][2] = player
            break
        elif player_input == '7' and board[2][0].isdigit():
            board[2][0] = player
            break
        elif player_input == '8' and board[2][1].isdigit():
            board[2][1] = player
            break
        elif player_input == '9' and board[2][2].isdigit():
            board[2][2] = player
            break
        else:
            print('Invalid Choice. Try again.')
    show_board(board)

def check_full_board(board):
    for row in board:
        for col in row:
            if col.isdigit():
                return False
    return True

def check_win(board):
    lines = [
        board[0], board[1], board[2],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    for line in lines:
        if line[0] == line[1] == line[2] and not line[0].isdigit():
            return True
    return False

def play():
    player1, player2 = set_players()
    print("Player1:", player1)
    print("Player2:", player2, '\n')
    board = create_empty_board()
    show_board(board)

    while True:
        for player in [player1, player2]:
            print(f"{player}'s turn")
            take_input(board, player)
            if check_win(board):
                print(f"{player} wins!")
                show_board(board)
                return
            if check_full_board(board):
                print("Game Finished. It's a tie!")
                show_board(board)
                return

if __name__ == '__main__':
    play()
