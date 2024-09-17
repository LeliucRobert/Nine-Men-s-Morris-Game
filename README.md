# **Nine Men's Morris Game**

## **Project Overview**

This is an implementation of the **Nine Men's Morris** board game in Python. The game is played **User vs Computer**, where the computer has a competitive AI that provides a challenging experience. The game is built using **Object-Oriented Programming (OOP)** and follows a **Layered Architecture** design.

The game consists of three phases:
1. Placing pieces on vacant points.
2. Moving pieces to adjacent points.
3. (Optional) Flying pieces to any vacant point when reduced to three men.

## **Game Rules**

The game is played on a grid with twenty-four intersections, called points. Each player has **nine pieces** or **men**, usually colored black and white. The goal is to form "mills" — three of your pieces in a straight line, either horizontally or vertically — and remove your opponent's pieces.

### **How to Win**
A player wins by:
- Reducing the opponent to two men, at which point they can no longer form mills.
- Blocking the opponent's moves, leaving them with no legal moves.

## **Phases of the Game**

### **Phase 1: Placing Pieces**
- The game starts on an empty board.
- Players alternate turns, placing their pieces on empty points.
- When a player forms a mill (three pieces in a row), they can remove one of the opponent's pieces. However, pieces in a mill can only be removed if no other pieces are available.
- Once all men have been placed on the board, the game moves to Phase 2.

### **Phase 2: Moving Pieces**
- Players take turns moving one of their pieces to an adjacent empty point.
- Pieces cannot jump over other pieces.
- Forming mills allows players to remove one of the opponent's pieces.
- If all of a player's pieces are blocked, and they cannot move, they lose.
- Players can break a mill by moving a piece out and back into the same mill to remove an opponent's piece again. This is called "pounding."

### **Phase 3: Flying (Optional)**
- When a player is reduced to three pieces, they enter the "flying" phase.
- During this phase, the player can move their pieces to any vacant point on the board, not just adjacent ones.
- This phase is meant to give the weaker player a chance to fight back when they are close to losing.

## **Features**
- **Competitive AI**: The game provides a fun and competitive experience by implementing a challenging AI opponent.
- **User vs Computer**: The game is designed to be played between the user and the AI-controlled computer.
- **Three Phases**: The game progresses through three different phases, each introducing new rules and strategies.


## **How to Play**
1. **Phase 1 (Placing Pieces)**: Place your pieces on empty points, aiming to form mills. When a mill is formed, you can remove one of the opponent's pieces.
2. **Phase 2 (Moving Pieces)**: Move your pieces to adjacent empty points. Continue forming mills and removing the opponent’s pieces.
3. **Phase 3 (Flying)**: If reduced to three pieces, move them to any empty point on the board, not just adjacent points.

## **Setup Instructions**
1. Clone or download the repository.
2. Ensure you have Python installed on your machine.
3. Run the game by executing the Python script:
   ```bash
   python nine_mens_morris.py
