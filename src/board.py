
class Board:
    """
    Representation of the game board.
    """

    def __init__(self, size=3):
        """
        Initialise the board with a chosen size.
        
        Parameters:
            size : Dimension of the board
        """
        self.size = size
        self.grid = []
        self.reset()

    def reset(self):
        """
        Reset the board in order to launch another game.
        """
        self.grid = []
        for row in range(self.size):
            new_row = []
            for col in range(self.size):
                new_row.append("")
            self.grid.append(new_row)

    def is_cell_empty(self, row, col):
        """
        Verify if a cell is empty.
        
        Parameters:
            row: row index of the cell
            col: column index of the cell
        """
        if self.parameters_check(row, col):
            return self.grid[row][col] == ""
        return False

    def place_piece(self, row, col, piece):
        """
        Place a piece on the board.

        Parameters:
            row = row index in the board
            col = col index in the board
            piece = piece of the player (X or O)
        """
        if not self.is_cell_empty(row, col):
            return False
        
        self.grid[row][col] = piece
        return True
    
    def get_empty_cells(self):
        """
        Return a list of tuples with all empty cells of the board.
        """
        empty_cells = []
        for row in range(self.size):
            for col in range(self.size):
                if self.grid[row][col] == "":
                    empty_cells.append((row,col))
        return empty_cells
    
    def get_cell(self, row, col):
        """
        Get the content of a cell.

        Parameters:
            row : row index of the cell
            col : column index of the cell
        """
        if self.parameters_check(row, col):
            return self.grid[row][col]
        return None

    def parameters_check(self, row, col):
        """
        Check if the row and columns are valid.

        Parameters:
            row : row index to verify
            col : col index to verify
        """
        if row < 0 or row >= self.size:
            return False
        if col < 0 or col >= self.size:
            return False
        return True
    