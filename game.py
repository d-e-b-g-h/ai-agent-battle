class TicTacToe:
    def __init__(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]

    def display(self):
        for row in self.board:
            print(" | ".join(cell if cell else " " for cell in row))
            print("-" * 9)

    def get_valid_moves(self):
        moves = []

        for r in range(3):
            for c in range(3):
                if self.board[r][c] == "":
                    moves.append((r, c))

        return moves

    def make_move(self, row, col, player):
        if self.board[row][col] != "":
            return False

        self.board[row][col] = player
        return True

    def check_winner(self):
        # Rows
        for row in self.board:
            if row[0] != "" and row[0] == row[1] == row[2]:
                return row[0]

        # Columns
        for col in range(3):
            if (
                self.board[0][col] != ""
                and self.board[0][col] == self.board[1][col] == self.board[2][col]
            ):
                return self.board[0][col]

        # Main diagonal
        if (
            self.board[0][0] != ""
            and self.board[0][0] == self.board[1][1] == self.board[2][2]
        ):
            return self.board[0][0]

        # Other diagonal
        if (
            self.board[0][2] != ""
            and self.board[0][2] == self.board[1][1] == self.board[2][0]
        ):
            return self.board[0][2]

        return None

    def is_draw(self):
        return self.check_winner() is None and not self.get_valid_moves()

    def is_terminal(self):
        return self.check_winner() is not None or self.is_draw()

    def copy(self):
        new_game = TicTacToe()
        new_game.board = [row[:] for row in self.board]
        return new_game