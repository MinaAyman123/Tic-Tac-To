# ❌⭕ Tic-Tac-Toe (Python CLI Game)

A simple Python command-line implementation of the classic **Tic-Tac-Toe** game (also known as **X-O**) for two players. The game randomly assigns symbols and continues until a win or a draw is reached.

---

## 🎮 Game Features

* 🧠 Randomly assigns `X` or `O` to Player 1 and Player 2
* 📦 Uses a 3×3 board with positions 1–9
* ✅ Input validation for occupied and invalid positions
* 🏆 Win detection for rows, columns, and diagonals
* 🤝 Draw condition when all spots are filled

---

## 🚀 How to Run

### 1. Clone or download the repository

```bash
git clone https://github.com/your-username/tic-tac-toe-cli.git
cd tic-tac-toe-cli
```

### 2. Run the game

```bash
python tictactoe.py
```

---

## 🖥️ Example Gameplay

```
Player1: X
Player2: O 

1	2	3
4	5	6
7	8	9

X's turn
Please Enter a number between 1-9 representing an empty position: 5
1	2	3
4	X	6
7	8	9

O's turn
Please Enter a number between 1-9 representing an empty position: 1
O	2	3
4	X	6
7	8	9

...

X wins!
```

---

## 🧱 Project Structure

* `create_empty_board()` → Initializes 3×3 board
* `show_board(board)` → Displays the board in CLI
* `set_players()` → Randomly assigns symbols
* `take_input(board, player)` → Handles player moves with input validation
* `check_full_board(board)` → Detects a tie
* `check_win(board)` → Detects winning combinations
* `play()` → Main game loop

---

## ✅ Requirements

* Python 3.x
  (No external libraries required)
