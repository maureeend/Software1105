import unittest
from Game import Game
from unittest.mock import patch
from tkinter import messagebox

class TestGame(unittest.TestCase):
    def test_game_initialization(self):
        game = Game()
        self.assertIsInstance(game, Game)

    def test_player_color_selection(self):
        game = Game()

        self.assertEqual(game.players[0].color, 'red')
        self.assertEqual(game.players[1].color, 'yellow')

    def test_valid_column_selection(self):
        game = Game()

        game.drop_disc(3)
        self.assertEqual(game.board.board[5][3], 1)

    def test_invalid_column_selection(self):
        game = Game()
        with self.assertRaises(IndexError):
            game.drop_disc(8)

    def test_disk_placement_empty_column(self):
        game = Game()
        game.drop_disc(3)
        self.assertEqual(game.board.board[5][3], 1)

    def test_disk_placement_solid_column(self):
        game = Game()
        
        for _ in range(6):
            game.drop_disc(3)
        
        with patch.object(messagebox, 'showerror') as mock_showerror:
            game.drop_disc(3)
            mock_showerror.assert_called_once_with("Invalid Move", "This column is full. Please choose another one.")

    def test_victory_condition_vertical_alignment(self):
        game = Game()
        game.board.board[0][3] = 1
        game.board.board[1][3] = 1
        game.board.board[2][3] = 1
        game.board.board[3][3] = 1

        self.assertTrue(game.check_win(1))


if __name__ == '__main__':
    unittest.main()
