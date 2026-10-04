def winning_lines(board):
    lines = []

    # Rows
    lines.extend(board)

    # Columns
    for col in range(3):
        lines.append([
            board[0][col],
            board[1][col],
            board[2][col]
        ])

    # Diagonals
    lines.append([
        board[0][0],
        board[1][1],
        board[2][2]
    ])

    lines.append([
        board[0][2],
        board[1][1],
        board[2][0]
    ])

    return lines


def count_threats(board, player):
    count = 0

    for line in winning_lines(board):
        if line.count(player) == 2 and line.count("") == 1:
            count += 1

    return count


def heuristic_h1(board, player):
    opponent = "O" if player == "X" else "X"

    score = 0

    for line in winning_lines(board):

        if opponent not in line:
            score += line.count(player) ** 2

        if player not in line:
            score -= line.count(opponent) ** 2

    score += 10 * count_threats(board, player)
    score -= 10 * count_threats(board, opponent)

    return score


def heuristic_h2(board, player):
    opponent = "O" if player == "X" else "X"

    score = 0

    for line in winning_lines(board):

        if opponent not in line:
            score += 2 ** line.count(player)

        if player not in line:
            score -= 2 ** line.count(opponent)

    # Center preference
    if board[1][1] == player:
        score += 4
    elif board[1][1] == opponent:
        score -= 4

    # Corner preference
    corners = [
        board[0][0],
        board[0][2],
        board[2][0],
        board[2][2]
    ]

    score += 2 * corners.count(player)
    score -= 2 * corners.count(opponent)

    return score