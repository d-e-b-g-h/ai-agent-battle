class SearchStats:
    def __init__(self):
        self.nodes_evaluated = 0
        self.nodes_pruned = 0

    def reset(self):
        self.nodes_evaluated = 0
        self.nodes_pruned = 0


def minimax(game, depth, maximizing_player, ai_player, heuristic):

    winner = game.check_winner()

    if winner is not None:
        if winner == ai_player:
            return 100 + depth
        else:
            return -100 - depth

    if game.is_draw():
        return 0

    if depth == 0:
        return heuristic(game.board, ai_player)

    valid_moves = game.get_valid_moves()

    # MAX
    if maximizing_player:

        best_score = float("-inf")

        for row, col in valid_moves:

            new_game = game.copy()
            new_game.make_move(row, col, ai_player)

            score = minimax(
                new_game,
                depth - 1,
                False,
                ai_player,
                heuristic
            )

            best_score = max(best_score, score)

        return best_score

    # MIN
    else:

        opponent = "O" if ai_player == "X" else "X"

        best_score = float("inf")

        for row, col in valid_moves:

            new_game = game.copy()
            new_game.make_move(row, col, opponent)

            score = minimax(
                new_game,
                depth - 1,
                True,
                ai_player,
                heuristic
            )

            best_score = min(best_score, score)

        return best_score


def minimax_alpha_beta(
    game,
    depth,
    maximizing_player,
    ai_player,
    heuristic,
    stats,
    alpha=float("-inf"),
    beta=float("inf")
):

    winner = game.check_winner()

    if winner is not None:

        stats.nodes_evaluated += 1

        if winner == ai_player:
            return 100 + depth
        else:
            return -100 - depth

    if game.is_draw():

        stats.nodes_evaluated += 1

        return 0

    if depth == 0:

        stats.nodes_evaluated += 1

        return heuristic(game.board, ai_player)

    valid_moves = game.get_valid_moves()

    # MAX
    if maximizing_player:

        best_score = float("-inf")

        for row, col in valid_moves:

            new_game = game.copy()
            new_game.make_move(row, col, ai_player)

            score = minimax_alpha_beta(
                new_game,
                depth - 1,
                False,
                ai_player,
                heuristic,
                stats,
                alpha,
                beta
            )

            best_score = max(best_score, score)

            alpha = max(alpha, best_score)

            if beta <= alpha:
                stats.nodes_pruned += 1
                break

        return best_score

    # MIN
    else:

        opponent = "O" if ai_player == "X" else "X"

        best_score = float("inf")

        for row, col in valid_moves:

            new_game = game.copy()
            new_game.make_move(row, col, opponent)

            score = minimax_alpha_beta(
                new_game,
                depth - 1,
                True,
                ai_player,
                heuristic,
                stats,
                alpha,
                beta
            )

            best_score = min(best_score, score)

            beta = min(beta, best_score)

            if beta <= alpha:
                stats.nodes_pruned += 1
                break

        return best_score


def choose_best_move(game, player, depth, heuristic, stats):

    stats.reset()

    valid_moves = game.get_valid_moves()

    best_move = None
    best_score = float("-inf")

    for row, col in valid_moves:

        new_game = game.copy()

        new_game.make_move(row, col, player)

        score = minimax_alpha_beta(
            new_game,
            depth - 1,
            False,
            player,
            heuristic,
            stats
        )

        if score > best_score:
            best_score = score
            best_move = (row, col)

    return best_move, best_score