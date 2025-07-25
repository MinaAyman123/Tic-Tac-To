from random import choice

def create_empty_board():
  return [
      [1,2,3],
      [4,5,6],
      [7,8,9]
        ]

def show_board(board):
  for i in range(3):
    for j in range(3):
      print(board[i][j],end="      ")
    print()

def set_players():
  return choice(['X', 'O'])

def take_input(board, player):
  while True:
      n=int(input("Please Enter a number between 1,9 represents an empty position:"))
      for i in range(3):
        for j in range(3):
            if n==board[i][j]:
              board[i][j]=player
              return
      print("Invaliied input")

def check_full_board(board):
  for i in range(3):
    for j in range(3):
      if isinstance(board[i][j],int):
        return False
  return True

def check_win(board):
    for row in board:
        if row[0] == row[1] == row[2] and isinstance(row[0], str):
            return f"{row[0]} wins"

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and isinstance(board[0][col], str):
            return f"{board[0][col]} wins"

    if board[0][0] == board[1][1] == board[2][2] and isinstance(board[0][0], str):
        return f"{board[0][0]} wins"

    if board[0][2] == board[1][1] == board[2][0] and isinstance(board[0][2], str):
        return f"{board[0][2]} wins"

def play():
  board=create_empty_board()
  player=set_players()
  show_board(board)
  while True:
    take_input(board,player)
    show_board(board)
    if check_win(board):
      print(check_win(board))
      break
    if check_full_board(board):
      print("ITs Tie")
      break
    player= "O" if player=="X" else "X"

if __name__=='__main__':
    play()