import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from board import Board

class TestBoard(unittest.TestCase):
    """
    Class made to test board functions.
    """
    def setUp(self):
        """
        Setup the test environnement.
        """
        self.board = Board()

    def test_place_piece(self):
        """
        Test various function when placing a piece.
        """
        self.board.place_piece(0, 0, "X")
        self.assertEqual(self.board.get_cell(0, 0), "X")
        self.assertFalse(self.board.is_cell_empty(0, 0))
        empty_cells = self.board.get_empty_cells()
        self.assertNotIn((0, 0), empty_cells)

    def test_reset_board(self):
        """
        Test reset function.
        """
        self.board.place_piece(0, 0, "X")
        self.board.reset()
        self.assertTrue(self.board.is_cell_empty(0, 0))

    def test_valid_index(self):
        """
        Test parameters_check function.
        """
        self.assertFalse(self.board.parameters_check(-1, 0))
        self.assertFalse(self.board.parameters_check(0, 10))