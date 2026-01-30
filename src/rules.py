

class Rules:
    """
    Class that handles game rules and stop a game if someone won.
    """

    def __init__(self, nb_piece_to_win = 3):
        """
        Initialise game rules.

        Parameters:
            board size: Size of the board (to verify who won)
            nb_piece_to_win: Number of pieces needed to win
        """
        self.nb_piece_to_win = nb_piece_to_win

    def check_rows(self, board):
        """
        Check if someone won by playing rows, call the check_line.

        Parameters:
            board: State of the board
        """
        for row_index in range(board.size):
            winner = self.check_line(board, row_index, 0, 0, 1, self.nb_piece_to_win)
            if winner:
                return winner
            
        return False

    def check_columns(self, board):
        """
        Check if someone won by playing columns, call the check_line.

        Parameters:
            board: State of the board
        """
        for col_index in range(board.size):
            winner = self.check_line(board, 0, col_index, 1, 0, self.nb_piece_to_win)
            if winner:
                return winner
            
        return False

    def check_diagonals(self, board, nb_piece_to_win):
        """
        Check if someone won by playing diagonals, call the check_line.

        Parameters:
            board: State of the board
        """
        # Check all diagonals going down-right (\)
        for row in range(board.size):
            winner = self.check_line(board, row, 0, 1, 1, nb_piece_to_win)
            if winner:
                return winner
        for col in range(1, board.size):
            winner = self.check_line(board, 0, col, 1, 1, nb_piece_to_win)
            if winner:
                return winner

        # Check all diagonals going down-left (/)
        for row in range(board.size):
            winner = self.check_line(board, row, board.size - 1, 1, -1, nb_piece_to_win)
            if winner:
                return winner
        for col in range(board.size - 1):
            winner = self.check_line(board, 0, col, 1, -1, nb_piece_to_win)
            if winner:
                return winner

        return False

    def check_line(self, board, row_start, col_start, row_direction, col_direction, nb_piece_to_win):
        """
        Check a line (can be row, columns or diagonals) in a board to find a winner.

        Parameters:
            board: State of the board
            row_start: Row index of the first element to check
        """
        row_index = row_start
        col_index = col_start

        last_piece = ""
        count = 0

        while board.parameters_check(row_index, col_index):
            current_piece = board.get_cell(row_index, col_index)

            if current_piece != "" and last_piece == current_piece:
                count +=1
            else:
                last_piece = current_piece
                if current_piece == "":
                    count = 0
                else:
                    count = 1

            if count >= nb_piece_to_win:
                return last_piece
            
            row_index += row_direction
            col_index += col_direction
        
        return False

    def check_winner(self, board):
        """
        Check if someone won a game.

        Parameters:
            board: State of the board
        """
        # Check all rows
        winner = self.check_rows(board)
        if winner:
            return winner
        
        # Check all columns
        winner = self.check_columns(board)
        if winner:
            return winner
        
        # Check all diagonals
        winner = self.check_diagonals(board, self.nb_piece_to_win)
        if winner:
            return winner
        
        return False