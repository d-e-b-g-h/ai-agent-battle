from minimax import SearchStats, choose_best_move
from heuristic import heuristic_h1, heuristic_h2


class Agent:

    def __init__(self, name, player, depth, heuristic):
        self.name = name
        self.player = player
        self.depth = depth
        self.heuristic = heuristic

    def choose_move(self, game):

        stats = SearchStats()

        move, score = choose_best_move(
            game,
            self.player,
            self.depth,
            self.heuristic,
            stats
        )

        return move, score, stats


class Nexus(Agent):

    def __init__(self, player="X", depth=3):

        super().__init__(
            name="NEXUS",
            player=player,
            depth=depth,
            heuristic=heuristic_h1
        )


class Titan(Agent):

    def __init__(self, player="O", depth=3):

        super().__init__(
            name="TITAN",
            player=player,
            depth=depth,
            heuristic=heuristic_h2
        )