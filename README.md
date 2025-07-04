


# 4x4 Ludo-Token Board Game Python 

This is a terminal-based two-player board game written in Python. The game is played on a 4x4 grid, where each player strategically moves 3 tokens across the board based on dice rolls. The first player to complete all tokens wins.


## 📌 Game Concept

- The board is a 4x4 grid represented in a linear fashion 0 to 15
- Each player has 3 tokens:
  - Player 1: Tokens 1, 2, 3
  - Player 2: Tokens 4, 5, 6
- Tokens can only be introduced onto the board after rolling a 6.
- Once a token is on the board, it moves forward based on dice rolls.
- The objective is to move all your tokens to the end of the board and exit them using an exact roll.


## 🎮 How to Play

### Turn Mechanics
1. Each player takes turns.
2. Press ENTER key to roll a dice from 1–6
3. If you roll a 6:
   - You may bring a new token from your hand onto the board placed on row 0
   - Or, you may choose to move an existing token already on the board
4. If you roll 1–5:
   - You can only move existing tokens
   - If you have no movable tokens, your turn is skipped

### Token Movement
- Tokens move linearly across the 4x4 board row by row, left to right
- Position index is calculated as: row * 4 + col

### 💥 Killing Opponent Tokens
- If you land on a space already occupied by an opponent’s token, that token is killed and sent back to their hand.
- You cannot land on your own token since it is a 2D board the players turn will be skipped.

### 🏁 Winning Condition
- A token can only be removed from the board completed by rolling exactly the remaining steps to reach position 16.
  - For example:
    - Position 14 needs 2
    - Position 15 needs 1
- The first player to **complete all three tokens** wins the game.

## Sample Output

Player 1, press ENTER to roll the dice...
Player 1 rolled a 6.
Tokens in hand: \[1, 2, 3]
Tokens on board: \[]
Choose a token to PLACE from hand or MOVE from board, type token number: 1

1  .  .  .
.  .  .  .
.  .  .  .
.  .  .  .

🏁Completed tokens: \[]


## Features

- ✔ 4x4 interactive board display in CLI
- Random dice rolling with user input
- Exact-roll exit logic
- 🛡 Cannot kill own tokens
- Opponent tokens are killed and returned to hand
- Game ends when all 3 tokens of a player are completed


## ⚙ How to Run
Run the Python game script:
   python game.py

Follow the prompts in the terminal.

## Notes

->Token state is tracked in 3 categories:

- Tokens in hand (playerX_tokens)
- Tokens on the board (tokens_on_board)
- Tokens completed (completed_tokens)
- The board is a 2D list for display but internally uses flat indices for logic.
- All logic is handled through functions like:

    -move_existing_token()
    -place_new_token()
    -move_token()
    -start_game()

## 🛠 Technologies Used

* Python 3
* Terminal based interaction
* Random module for dice simulation

## Future Improvements

- Add turn history or move log
-🖼GUI version using Tkinter or Pygame
- Color-coded tokens
- Online multiplayer support





