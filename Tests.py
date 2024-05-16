import unittest
from Game import Game

class TestGame(unittest.TestCase):
    def test_game_initialization(self):
        game = Game()
        # Assert that the game initializes without errors
        self.assertIsInstance(game, Game)

    def test_player_color_selection(self):
        # Test player color selection by confirming chosen colors
        game = Game()

        self.assertEqual(game.players[0].color, 'red')
        # Assuming player 2's color is automatically assigned as yellow
        self.assertEqual(game.players[1].color, 'yellow')

    def test_valid_column_selection(self):
        # Test placing disk in a valid and existing column
        game = Game()

        game.drop_disc(3)
        # Check if the disc is placed in the correct position
        self.assertEqual(game.board.board[5][3], 1)

    def test_invalid_column_selection(self):
        # Test placing disk in an invalid and non-existing column
        game = Game()
        # Attempt to place disk in column 8 (non-existing)
        with self.assertRaises(IndexError):
            game.drop_disc(8)

    def test_disk_placement_empty_column(self):
        # Test placing disk in an empty column
        game = Game()
        game.drop_disc(3)
        # Check if the disc is placed in the correct position
        self.assertEqual(game.board.board[5][3], 1)

    def test_disk_placement_solid_column(self):
        # Test placing disk in a solid column
        game = Game()
        for i in range(6):
            game.drop_disc(3)
        # Attempt to place disk in column 3 (solid)
        with self.assertRaises(ValueError):
            game.drop_disc(3)

    def test_victory_condition_vertical_alignment(self):
        # Test victory condition with vertical alignment of 4 discs
        game = Game()
        game.board.board[0][3] = 1
        game.board.board[1][3] = 1
        game.board.board[2][3] = 1
        game.board.board[3][3] = 1
        # Check if the game declares the first player as the winner
        self.assertTrue(game.check_win(1))

    # Add more test methods as needed

if __name__ == '__main__':
    unittest.main()
