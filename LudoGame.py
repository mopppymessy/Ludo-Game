import random

#initialize a 4x4 board
board = []
for i in range(4):
    row = [0, 0, 0, 0]
    board.append(row)

#tokens per player
player1_tokens = [1, 2, 3]  #In hand
player2_tokens = [4, 5, 6]

#Tokens on board
tokens_on_board = {}  #token: (row, col)

#tokens that completed the board
completed_tokens = []

#print the current board state
def print_board():
    for row in board:
        row_display = []
        for cell in row:
            if cell != 0:
                row_display.append(str(cell))  #show token number
            else:
                row_display.append('.')        #show empty space as '.'

        print('  '.join(row_display))

    print(f"🏁Completed tokens: {completed_tokens}")
    print()

#move a token forward by dice roll
def move_existing_token(token, roll, player_name, player_tokens):
    if token not in tokens_on_board:
        print("Token not on board. Try again.")
        return False

    row, col = tokens_on_board[token]
    flat_index = row * 4 + col
    new_index = flat_index + roll

    #must roll exactly remaining_spaces + 1 to finish
    if new_index == 16:
        print(f"{player_name}, token {token} has completed its journey! 🎉")
        board[row][col] = 0
        del tokens_on_board[token]
        completed_tokens.append(token)
        return True
    elif new_index > 15:
        print(f"{player_name}, token {token} needs a {16 - flat_index} to finish.")
        return False

    new_row, new_col = divmod(new_index, 4)

    target_cell = board[new_row][new_col]

    #handle opponent killing only
    if target_cell != 0:
        #Player 1 can only kill Player 2 tokens
        if player_name == "Player 1" and target_cell in [4, 5, 6]:
            print(f"{player_name} landed on an opponent! Token {target_cell} is killed.")
            player2_tokens.append(target_cell)
            del tokens_on_board[target_cell]
        #Player 2 can only kill Player 1 tokens
        elif player_name == "Player 2" and target_cell in [1, 2, 3]:
            print(f"{player_name} landed on an opponent! Token {target_cell} is killed.")
            player1_tokens.append(target_cell)
            del tokens_on_board[target_cell]
        else:
            print(f"{player_name}, you cannot move onto your own token!")
            return False

    #Move the token
    board[row][col] = 0
    board[new_row][new_col] = token
    tokens_on_board[token] = (new_row, new_col)
    return True

#bring new token onto the board
def place_new_token(token, player_name, player_tokens):
    for col in range(4):
        if board[0][col] == 0:
            board[0][col] = token
            tokens_on_board[token] = (0, col)
            player_tokens.remove(token)
            return True
    print(f"{player_name}, no space to bring a new token onto the board.")
    return False

#handle player turn
def move_token(player_tokens, player_name):
    input(f"\n{player_name}, press ENTER to roll the dice...")
    roll = random.randint(1, 6)
    print(f"{player_name} rolled a {roll}.")

    #tokens on board
    movable_tokens = [t for t in tokens_on_board if
                      (player_name == "Player 1" and t in [1, 2, 3]) or
                      (player_name == "Player 2" and t in [4, 5, 6])]

    can_place_new = roll == 6 and player_tokens

    print_board()

    while True:
        if can_place_new:
            print(f"Tokens in hand: {player_tokens}")
            print(f"Tokens on board: {movable_tokens}")
            choice = input("Choose a token to PLACE from hand or MOVE from board, type token number: ").strip()
        else:
            print(f"Tokens on board: {movable_tokens}")
            if not movable_tokens:
                print("No tokens to move. Turn skipped.")
                return
            choice = input("Choose a token to MOVE from board, type token number: ").strip()

        if not choice.isdigit():
            print("Please enter a valid number.")
            continue

        token = int(choice)

        if can_place_new and token in player_tokens:
            if place_new_token(token, player_name, player_tokens):
                print_board()
            break

        elif token in movable_tokens:
            if move_existing_token(token, roll, player_name, player_tokens):
                print_board()
            break
        else:
            print("Invalid token. Try again.")

#Start the game
def start_game():
    print_board()
    while True:
        move_token(player1_tokens, "Player 1")
        if all(t in completed_tokens for t in [1, 2, 3]):
            print("🏆 Player 1 has completed all tokens! Game over.")
            break

        move_token(player2_tokens, "Player 2")
        if all(t in completed_tokens for t in [4, 5, 6]):
            print("🏆 Player 2 has completed all tokens! Game over.")
            break

#run game
start_game()
