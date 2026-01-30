from board import Board
from rules import Rules
from ui import GameUI


def main():
    """
    Main function to start the Tic-Tac-Toe game.
    """
    board = Board(3)
    rules = Rules(3)
    game = GameUI(board, rules)
    
    game.run()

if __name__ == "__main__":
    main()