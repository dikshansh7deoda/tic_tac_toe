# Tic Tac Toe Game - Python Essentials Project

def get_player_names():
    print("Welcome to Tic-Tac-Toe!")
    p1 = input("Enter Player 1 name (X): ")
    if p1 == "":
        p1 = "Player 1"
        
    p2 = input("Enter Player 2 name (O): ")
    if p2 == "":
        p2 = "Player 2"
        
    scores = {p1: 0, p2: 0, "Draws": 0}
    return p1, p2, scores


def check_winner(board, symbol):
    # All possible winning combinations
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]               # Diagonals
    ]
    for condition in wins:
        if board[condition[0]] == symbol and board[condition[1]] == symbol and board[condition[2]] == symbol:
            return True
    return False


def play_game(p1, p2):
    # Board spaces 1-9 to help players pick spot easily
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    current_player = p1
    current_symbol = "X"
    
    while True:
        # Print current board layout
        print()
        print(board[0] + " | " + board[1] + " | " + board[2])
        print("---------")
        print(board[3] + " | " + board[4] + " | " + board[5])
        print("---------")
        print(board[6] + " | " + board[7] + " | " + board[8])
        print()
        
        # Get move from current player
        while True:
            choice = input(current_player + " (" + current_symbol + "), enter position (1-9): ")
            
            # Make sure input is a valid number
            if choice.isdigit():
                pos = int(choice) - 1
                if 0 <= pos <= 8:
                    if board[pos] != "X" and board[pos] != "O":
                        break
                    else:
                        print("That spot is already taken! Try another one.")
                else:
                    print("Please enter a number between 1 and 9.")
            else:
                print("Invalid input! Enter a number only.")

        # Place player move on board
        board[pos] = current_symbol
        
        # Check if current player won
        if check_winner(board, current_symbol):
            print()
            print(board[0] + " | " + board[1] + " | " + board[2])
            print("---------")
            print(board[3] + " | " + board[4] + " | " + board[5])
            print("---------")
            print(board[6] + " | " + board[7] + " | " + board[8])
            print()
            print("Congratulations! " + current_player + " wins!")
            return current_player
        
        # Check if board is full (Draw)
        full = True
        for spot in board:
            if spot != "X" and spot != "O":
                full = False
                break
                
        if full:
            print()
            print(board[0] + " | " + board[1] + " | " + board[2])
            print("---------")
            print(board[3] + " | " + board[4] + " | " + board[5])
            print("---------")
            print(board[6] + " | " + board[7] + " | " + board[8])
            print()
            print("It's a draw!")
            return "Draw"
            
        # Switch player turn
        if current_player == p1:
            current_player = p2
            current_symbol = "O"
        else:
            current_player = p1
            current_symbol = "X"


# Main running loop
player1, player2, score_card = get_player_names()

while True:
    winner = play_game(player1, player2)
    
    if winner == "Draw":
        score_card["Draws"] += 1
    else:
        score_card[winner] += 1
        
    print("\n--- SCOREBOARD ---")
    print(player1 + ": " + str(score_card[player1]))
    print(player2 + ": " + str(score_card[player2]))
    print("Draws: " + str(score_card["Draws"]))
    
    again = input("\nDo you want to play again? (y/n): ")
    if again.lower() != "y":
        print("Thanks for playing!")
        break