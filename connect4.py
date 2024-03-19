def create_grid():
    return [[' ' for _ in range(7)] for _ in range(6)]

def print_grid(grid):
    for row in grid:
        print('|' + '|'.join(row) + '|')
    print('+---' * 7 + '+')

def check_winner(grid):
    # Vérifie horizontalement
    for row in range(6):
        for col in range(4):
            if grid[row][col] == grid[row][col+1] == grid[row][col+2] == grid[row][col+3] != ' ':
                return grid[row][col]

    # Vérifie verticalement
    for col in range(7):
        for row in range(3):
            if grid[row][col] == grid[row+1][col] == grid[row+2][col] == grid[row+3][col] != ' ':
                return grid[row][col]

    # Vérifie diagonalement (montante et descendante)
    for row in range(3, 6):
        for col in range(4):
            if grid[row][col] == grid[row-1][col+1] == grid[row-2][col+2] == grid[row-3][col+3] != ' ':
                return grid[row][col]
    for row in range(3):
        for col in range(4):
            if grid[row][col] == grid[row+1][col+1] == grid[row+2][col+2] == grid[row+3][col+3] != ' ':
                return grid[row][col]

    return None

def drop_disc(grid, col, disc):
    for row in range(5, -1, -1):
        if grid[row][col] == ' ':
            grid[row][col] = disc
            return True
    return False

def main():
    grid = create_grid()
    turn = 0

    while True:
        print_grid(grid)
        if turn % 2 == 0:
            disc = 'R'
        else:
            disc = 'Y'

        try:
            col = int(input(f"Joueur {disc}, choisissez une colonne (0-6): "))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue

        if col < 0 or col > 6:
            print("Cette colonne n'existe pas. Veuillez choisir une colonne entre 0 et 6.")
            continue

        if not drop_disc(grid, col, disc):
            print("Cette colonne est pleine. Veuillez en choisir une autre.")
            continue

        winner = check_winner(grid)
        if winner:
            print_grid(grid)
            print(f"Joueur {winner} a gagné!")
            break

        if all(grid[0][col] != ' ' for col in range(7)):
            print("Match nul!")
            break

        turn += 1

if __name__ == "__main__":
    main()
