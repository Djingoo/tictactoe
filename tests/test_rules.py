import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from board import Board
from rules import Rules

class TestRules(unittest.TestCase):
    """
    Class made to test winner verification.
    """
    def setUp(self):
        """
        Setup the test environnement.
        """
        self.board = Board()
        self.rules = Rules()

    def test_horizontal_win(self):
        """
        Testing an horizontal win.
        """
        self.board.place_piece(0, 0, "X")
        self.board.place_piece(0, 1, "X")
        self.board.place_piece(0, 2, "X")

        self.assertTrue(self.rules.check_winner(self.board))

    def test_vertical_win(self):
        """
        Testing a vertical win.
        """
        self.board.place_piece(0, 0, "X")
        self.board.place_piece(1, 0, "X")
        self.board.place_piece(2, 0, "X")

        self.assertTrue(self.rules.check_winner(self.board))

    def test_diagonal_win(self):
        """
        Testing a diagonal win.
        """
        self.board.place_piece(0, 0, "X")
        self.board.place_piece(1, 1, "X")
        self.board.place_piece(2, 2, "X")

        self.assertTrue(self.rules.check_winner(self.board))

    def test_no_winner_yet(self):
        """
        Testing if no one is winning.
        """
        self.assertFalse(self.rules.check_winner(self.board))
    