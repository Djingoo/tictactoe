
import random


class ComputerPlayer:
    """
    Computer player that will play randomly.
    """

    def __init__(self, piece, name="Computer"):
        """
        Initialise a computer player.

        Parameters:
            name: computer name
            piece: piece the computer will play
        """
        self.name = name
        self.piece = piece

    def get_move(self, board):
        """
        Get a random move based on the empty cells.

        Parameters:
            board: the state of the board
        """
        empty_cells = board.get_empty_cells()
        if len(empty_cells) > 0:
            return random.choice(empty_cells)
        return None
