# Project Statement & Specification: Tic-Tac-Toe Game

## 📌 Problem Statement

Traditional paper-and-pencil games like Tic-Tac-Toe are engaging and educational for learning basic computational thinking and logic. However, playing physically requires materials and manual score tracking. Existing basic code implementations often lack robust input validation, flexible player management, or session-based win/loss tracking, leading to poor user experiences or unexpected program crashes when invalid input is entered.

There is a need for a reliable, lightweight, and user-friendly command-line interface (CLI) Tic-Tac-Toe application that handles user inputs safely, provides a smooth gameplay experience for two players, and tracks scores across multiple consecutive rounds.

---

## 🎯 Scope of the Project

The scope of this project encompasses the design and implementation of a two-player, terminal-based Tic-Tac-Toe game written in Python.

### **In-Scope:**
* **Player Initialization:** Support for custom player names with fallback defaults.
* **Interactive Gameplay:** A 3x3 grid display numbered 1 to 9 for position selection.
* **Input Validation:** Error handling for non-integer inputs, out-of-range choices (less than 1 or greater than 9), and selection of already-occupied spots.
* **Game Logic:** Automatic evaluation of winning conditions (rows, columns, diagonals) and draw state detection.
* **Scoreboard System:** Persistent score tracking across multiple rounds during a single active session.
* **Replay Capability:** Option to replay rounds without needing to restart the Python script or re-enter player names.

### **Out-of-Scope:**
* Graphical User Interface (GUI) or web interface development.
* Single-player mode with AI/Computer opponent integration.
* Persistent database storage (scores reset upon terminating the script).
* Online network or multiplayer connectivity.

---

## 👥 Target Users

1. **Python Beginners & Students:** Individuals looking to study standard Python control flows, function decomposition, dictionaries, input validation, and loop structures.
2. **Casual Gamers / Local Players:** Two players sharing a single terminal device looking for a quick, interactive pass-and-play game experience.
3. **Educators & Evaluators:** Instructors reviewing fundamental programming concepts, input sanitization, and basic CLI game architectures in Python.

---

## ⚡ High-Level Features

* **Custom Player Profiles:** Allows custom name entry for Player 1 ($X$) and Player 2 ($O$), defaulting to standard names if left empty.
* **Dynamic Grid Rendering:** Clear visual representation of the current board state after every turn, featuring numbered positions for ease of choice.
* **Robust Input Sanitization:** Continuous input loops preventing invalid inputs from breaking the execution flow.
* **Automatic Game State Engine:** Real-time evaluation of 8 possible win paths and board-full (draw) detection.
* **Multi-Round Score Tracker:** Dynamic scoreboard updating after every round with wins for each player and total draw counts.