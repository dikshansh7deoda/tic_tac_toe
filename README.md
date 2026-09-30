# **Tic-Tac-Toe (Python Essentials Project)**

A classic two-player Tic-Tac-Toe game implemented in Python for the command line interface (CLI). This project features custom player names, position validation, multi-round play with win/draw tracking, and a real-time scoreboard.

## **🚀 Features**

* **Custom Player Names:** Players can enter personalized names or use defaults (Player 1 and Player 2).  
* **Interactive Grid Board:** Spaces are labeled 1–9 for intuitive move selection.  
* **Input Validation:** Prevents invalid inputs (non-numbers, out-of-range numbers) and stops players from overwriting taken spots.  
* **Scoreboard & Multi-round Support:** Tracks overall wins for both players as well as total draws across multiple rounds.  
* **Pure Python:** Uses core standard Python libraries without external dependencies.

## **🎮 How to Play**

1. The game displays a 3x3 grid with positions labeled 1 through 9:  
   1 | 2 | 3  
   \---------  
   4 | 5 | 6  
   \---------  
   7 | 8 | 9

2. **Player 1** plays as **X** and **Player 2** plays as **O**.  
3. On your turn, type the number corresponding to the grid position where you wish to place your symbol and press Enter.  
4. The first player to align 3 symbols horizontally, vertically, or diagonally wins\!  
5. If all spaces are filled without 3 in a row, the game results in a draw.  
6. At the end of a round, view the updated scoreboard and choose whether to play another round.

## **🛠️ Requirements & Installation**

### **Requirements**

* **Python 3.x** installed on your system.

### **Running the Game**

1. **Clone or Download** this repository.  
2. Open your terminal or command prompt and navigate to the project folder:  
   cd path/to/project

3. Run the Python script:  
   python main.py

   *(Replace main.py with the actual file name if different)*

## **📁 Code Structure**

| **Function / Block** | **Description** |

| get\_player\_names() | Prompts players for custom names and initializes the scoreboard dictionary. |

| check\_winner(board, symbol) | Evaluates grid state against all 8 winning combinations (rows, columns, diagonals). |

| play\_game(p1, p2) | Manages the main round loop, renders the board, handles player moves, and detects wins or draws. |

| Main Program Loop | Manages overall match sessions, score updates, and replay prompts. |

## **📜 License**

This project is open-source and free to use for learning and development purposes.
