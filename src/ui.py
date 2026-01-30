
import customtkinter as ctk
from player import ComputerPlayer


class GameUI:
    """
    Tic-Tac-Toe UI using customtkinter.
    """
    def __init__(self, board, rules):
        """
        Set up the game window.
        
        Parameters:
            board: The game board object
            rules: The game rules object
        """
        self.board = board
        self.rules = rules
        
        self.game_over = False
        self.player_piece = None
        self.computer = ComputerPlayer(None)
        self.player_turn = True
        
        self.window = ctk.CTk()
        self.window.title("Tic-Tac-Toe")
        
        board_width = self.board.size * 98 + 20
        board_height = self.board.size * 98 + 150
        self.window.geometry(f"{board_width}x{board_height}")
        self.window.resizable(False, False)
        
        ctk.set_appearance_mode("dark")
        self.create_widgets()
        self.show_start_popup()

    def create_widgets(self):
        """
        Create all buttons and labels for the game.
        """
        self.title_label = ctk.CTkLabel(
            self.window,
            text="Tic-Tac-Toe",
            font=("Arial", 28, "bold")
        )
        self.title_label.pack(pady=10)

        self.status_label = ctk.CTkLabel(
            self.window,
            text="Choose your piece",
            font=("Arial", 16)
        )
        self.status_label.pack(pady=5)

        self.board_frame = ctk.CTkFrame(self.window)
        self.board_frame.pack(pady=20)

        self.buttons = []
        for row in range(self.board.size):
            row_buttons = []
            for col in range(self.board.size):
                button = ctk.CTkButton(
                    self.board_frame,
                    text="",
                    width=90,
                    height=90,
                    font=("Arial", 36, "bold"),
                    fg_color="gray30",
                    hover_color="gray40",
                    command=lambda r=row, c=col: self.button_clicked(r, c)
                )
                button.grid(row=row, column=col, padx=4, pady=4)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

        self.new_game_button = ctk.CTkButton(
            self.window,
            text="New Game",
            width=150,
            height=40,
            font=("Arial", 16),
            fg_color="green",
            hover_color="darkgreen",
            command=self.new_game
        )
        self.new_game_button.pack(pady=20)

    def button_clicked(self, row, col):
        """
        Handle when a player clicks a button.
        
        Parameters:
            row: Which row was clicked
            col: Which column was clicked
        """
        if self.game_over:
            return
        
        if self.player_piece is None:
            self.show_start_popup()
            return
        
        if not self.player_turn:
            return
        
        if not self.board.is_cell_empty(row, col):
            return
        
        self.player_turn = False
        
        self.board.place_piece(row, col, self.player_piece)
        self.update_button(row, col, self.player_piece)
        
        if self.check_for_winner("You win!"):
            return
        
        if self.check_for_tie():
            return
        
        self.status_label.configure(text="Computer thinking...")
        self.window.after(500, self.computer_turn)

    def computer_turn(self):
        """
        Let the computer make a move.
        """
        move = self.computer.get_move(self.board)
        
        if move:
            row, col = move
            self.board.place_piece(row, col, self.computer.piece)
            self.update_button(row, col, self.computer.piece)
        
        if self.check_for_winner("Computer wins!"):
            return
        
        if self.check_for_tie():
            return
        
        self.player_turn = True
        self.status_label.configure(text=f"Your turn ({self.player_piece})")

    def update_button(self, row, col, piece):
        """
        Update a button to show X or O.
        
        Parameters:
            row: Button row
            col: Button column
            piece: "X" or "O"
        """
        if piece == "X":
            color = "#3498db"
        else:
            color = "#e74c3c"
        
        self.buttons[row][col].configure(
            text=piece,
            fg_color=color,
            hover_color=color
        )

    def check_for_winner(self, message):
        """
        Check if someone won and end the game.
        
        Parameters:
            message: Message to display
        """
        if self.rules.check_winner(self.board):
            self.game_over = True
            self.status_label.configure(text=message)
            self.window.after(500, lambda: self.show_end_popup(message))
            return True
        return False

    def check_for_tie(self):
        """
        Check if the game is a tie and end the game.
        """
        if len(self.board.get_empty_cells()) == 0:
            self.game_over = True
            self.status_label.configure(text="It's a tie!")
            self.window.after(500, lambda: self.show_end_popup("It's a tie!"))
            return True
        return False

    def new_game(self):
        """
        Reset everything for a new game.
        """
        self.board.reset()
        self.game_over = False
        self.player_turn = True
        self.player_piece = None
        
        for row in range(self.board.size):
            for col in range(self.board.size):
                self.buttons[row][col].configure(
                    text="",
                    fg_color="gray30",
                    hover_color="gray40"
                )
        
        self.show_start_popup()

    def show_start_popup(self):
        """
        Show a popup to let player choose which piece to play.
        """
        popup = ctk.CTkToplevel(self.window)
        popup.title("Welcome!")
        popup.geometry("300x200")
        popup.resizable(False, False)
        popup.grab_set()
        
        popup.transient(self.window)

        def on_close():
            pass
        
        popup.protocol("WM_DELETE_WINDOW", on_close)
        
        title = ctk.CTkLabel(
            popup,
            text="Choose Your Piece",
            font=("Arial", 20, "bold")
        )
        title.pack(pady=20)
        
        def play_as_x():
            self.player_piece = "X"
            self.computer.piece = "O"
            self.player_turn = True
            self.status_label.configure(text="Your turn (X)")
            popup.destroy()
        
        x_btn = ctk.CTkButton(
            popup,
            text="Play as X",
            width=200,
            height=40,
            font=("Arial", 16),
            fg_color="#3498db",
            hover_color="#2980b9",
            command=play_as_x
        )
        x_btn.pack(pady=10)
        
        def play_as_o():
            self.player_piece = "O"
            self.computer.piece = "X"
            self.player_turn = False
            self.status_label.configure(text="Computer thinking...")
            popup.destroy()
            self.window.after(500, self.computer_turn)
        
        o_btn = ctk.CTkButton(
            popup,
            text="Play as O",
            width=200,
            height=40,
            font=("Arial", 16),
            fg_color="#e74c3c",
            hover_color="#c0392b",
            command=play_as_o
        )
        o_btn.pack(pady=10)

    def show_end_popup(self, message):
        """
        Show a popup when game ends to ask for rematch.
        
        Parameters:
            message: Message to display
        """
        popup = ctk.CTkToplevel(self.window)
        popup.title("Game Over")
        popup.geometry("300x180")
        popup.resizable(False, False)
        popup.grab_set()
        
        popup.transient(self.window)
        
        result_label = ctk.CTkLabel(
            popup,
            text=message,
            font=("Arial", 22, "bold")
        )
        result_label.pack(pady=20)
        
        question_label = ctk.CTkLabel(
            popup,
            text="Play again?",
            font=("Arial", 16)
        )
        question_label.pack(pady=5)
        
        btn_frame = ctk.CTkFrame(popup, fg_color="transparent")
        btn_frame.pack(pady=15)
        
        def play_again():
            popup.destroy()
            self.new_game()
        
        yes_btn = ctk.CTkButton(
            btn_frame,
            text="Yes",
            width=100,
            height=35,
            font=("Arial", 14),
            fg_color="green",
            hover_color="darkgreen",
            command=play_again
        )
        yes_btn.pack(side="left", padx=10)
        
        def quit_game():
            popup.destroy()
            self.window.destroy()
        
        no_btn = ctk.CTkButton(
            btn_frame,
            text="No",
            width=100,
            height=35,
            font=("Arial", 14),
            fg_color="#e74c3c",
            hover_color="#c0392b",
            command=quit_game
        )
        no_btn.pack(side="left", padx=10)

    def run(self):
        """
        Start the game.
        """
        self.window.mainloop()
