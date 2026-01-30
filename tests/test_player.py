import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from player import ComputerPlayer
from board import Board

class TestPlayer(unittest.TestCase):
    def setUp(self):
        """
        Setup the test environnement.
        """
        self.board = Board(2)
        self.computer = ComputerPlayer("O")

    def test_get_move(self):
        self.board.place_piece(0, 0, "X")
        self.board.place_piece(1, 0, "X")
        self.board.place_piece(0, 1, "X")
        self.board.place_piece(1, 1, "X")
        self.assertIsNone(self.computer.get_move(self.board))