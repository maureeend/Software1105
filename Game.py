import tkinter as tk
from tkinter import messagebox
import numpy as np
from Board import Board
from Player import Player

class Game:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Connect 4")
        self.root.configure(bg='#2c3e50')

        self.board = Board()
        self.current_player = 0
        self.colors = ['white', '#e74c3c', '#f1c40f']
        self.players = [Player("Player 1", 'red'), Player("Player 2", 'yellow')]
        self.game_over = False

        self.create_widgets()
        self.display_current_player()

    def create_widgets(self):
        self.buttons = []
        for i in range(6):
            row_buttons = []
            for j in range(7):
                btn = tk.Button(self.root, width=6, height=3, bg='blue', relief='raised', borderwidth=2,
                                command=lambda col=j: self.drop_disc(col))
                btn.grid(row=i, column=j, padx=5, pady=5, sticky='nsew')
                btn.config(bg='blue', activebackground='#3498db')  # Gradient effect
                row_buttons.append(btn)
            self.buttons.append(row_buttons)

        self.play_again_button = tk.Button(self.root, text="Play Again", bg='#16a085', fg='white',
                                           command=self.play_again)
        self.play_again_button.grid(row=6, column=0, columnspan=7, pady=10, sticky='ew')

    def drop_disc(self, col):
        if not self.game_over:
            if self.is_valid_move(col):
                row = self.board.drop_disc(col, self.current_player + 1)
                disc = self.current_player + 1
                self.animate_disc_drop(row, col, disc)
                if self.check_win(disc):
                    self.show_winner(self.players[self.current_player].name)
                elif self.board.is_full():
                    messagebox.showinfo("Draw", "It's a draw!")
                    self.game_over = True
                else:
                    self.switch_player()
                    self.display_current_player()
            else:
                raise ValueError
            
    def animate_disc_drop(self, row, col, disc):
        for r in range(row + 1):
            if r > 0:
                self.buttons[r-1][col].config(bg='blue')
            self.buttons[r][col].config(bg=self.colors[disc])
            self.root.update()
            self.root.after(50)

    def display_current_player(self):
        self.root.title(f"Connect 4 - {self.players[self.current_player].name}'s Turn")

    def is_valid_move(self, col):
        return self.board.board[0][col] == 0

    def check_win(self, disc):
        for row in range(6):
            for col in range(7 - 3):
                if np.all(self.board.board[row, col:col + 4] == disc):
                    return True
        for col in range(7):
            for row in range(6 - 3):
                if np.all(self.board.board[row:row + 4, col] == disc):
                    return True
        for row in range(6 - 3):
            for col in range(7 - 3):
                if np.all(self.board.board[row:row + 4, col:col + 4].diagonal() == disc):
                    return True
                if np.all(np.fliplr(self.board.board[row:row + 4, col:col + 4]).diagonal() == disc):
                    return True
        return False

    def show_winner(self, winner):
        for row in self.buttons:
            for button in row:
                button.config(state='disabled')
        messagebox.showinfo("Winner", f"{winner} wins!")


    def switch_player(self):
        self.current_player = 1 - self.current_player

    def play_again(self):
        self.root.destroy()
        new_game = Game()
        new_game.start_game()

    def start_game(self):
        self.root.mainloop()

if __name__ == '__main__':
    game = Game()
    game.start_game()



