
import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.current_player = None
        self.players = {"X": "", "O": ""}
        self.game_over = False
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")

        # Create player name entry fields and assign symbols
        player_labels = []
        for symbol in self.players:
            label = tk.Label(self.root, text=f"Enter name for player '{symbol}':",font=("Arial",10))
            label.grid(row=len(player_labels), column=0, padx=15, pady=10)
            player_labels.append(label)
            entry = tk.Entry(self.root)
            entry.grid(row=len(player_labels)-1, column=1, padx=10, pady=10)
            self.players[symbol] = entry
        self.current_player = "X"  # Start with X as the first player

        # Create buttons for the game board
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.root, text="", font=("Arial", 50), width=4, height=1,
                                   bg="black",fg="white",command=lambda i=i, j=j: self.button_click(i, j))
                button.grid(row=i+3, column=j, padx=10, pady=10)
                row.append(button)
            self.buttons.append(row)

        # Create a reset button
        reset_button = tk.Button(self.root, text="Reset", font=("Arial", 30),fg="red",bg="grey",
                                  command=self.reset)
        reset_button.grid(row=6, column=1, pady=30)
        self.root.mainloop()

    def button_click(self, row, col):
        if self.game_over:
            return
        if self.board[row][col] == "":
            self.buttons[row][col].config(text=self.current_player)
            self.board[row][col] = self.current_player
            if self.check_win():
                messagebox.showinfo("Tic Tac Toe", f"{self.players[self.current_player].get()} wins!")
                self.game_over = True
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.game_over = True
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_win(self):
        # Check rows
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
        # Check columns
        for j in range(3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] != "":
                return True
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def check_draw(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    return False
        return True

    def reset(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")
                self.board[i][j] = ""
        self.current_player = "X"
        self.game_over = False

game = TicTacToe()

