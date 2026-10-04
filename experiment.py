import time
import csv

from game import TicTacToe
from agents import Nexus, Titan


class Experiment:

    def __init__(self):
        self.results = []

    # =========================================================
    # 10 AI vs AI GAMES
    # =========================================================

    def run_game(self, first_agent, second_agent, game_number):

        game = TicTacToe()

        agents = {
            first_agent.player: first_agent,
            second_agent.player: second_agent
        }

        current_player = first_agent.player

        move_count = 0

        nexus_nodes = 0
        titan_nodes = 0

        nexus_pruned = 0
        titan_pruned = 0

        start_time = time.perf_counter()

        while not game.is_terminal():

            agent = agents[current_player]

            move, score, stats = agent.choose_move(game)

            if move is None:
                break

            game.make_move(
                move[0],
                move[1],
                current_player
            )

            move_count += 1

            if agent.name == "NEXUS":

                nexus_nodes += stats.nodes_evaluated
                nexus_pruned += stats.nodes_pruned

            elif agent.name == "TITAN":

                titan_nodes += stats.nodes_evaluated
                titan_pruned += stats.nodes_pruned

            current_player = (
                "O" if current_player == "X" else "X"
            )

        elapsed_time = time.perf_counter() - start_time

        winner = game.check_winner()

        if winner is None:
            winner_name = "DRAW"
        else:
            winner_name = agents[winner].name

        result = {
            "game": game_number,
            "first": first_agent.name,
            "winner": winner_name,
            "moves": move_count,
            "nexus_nodes": nexus_nodes,
            "titan_nodes": titan_nodes,
            "nexus_pruned": nexus_pruned,
            "titan_pruned": titan_pruned,
            "time": round(elapsed_time, 6)
        }

        self.results.append(result)

        return result

    def run_10_games(self):

        print("\n========== 10 AI VS AI GAMES ==========\n")

        for game_number in range(1, 11):

            # Alternate player symbols
            nexus = Nexus(
                player="X" if game_number % 2 == 1 else "O",
                depth=3
            )

            titan = Titan(
                player="O" if game_number % 2 == 1 else "X",
                depth=3
            )

            # Alternate starting player
            if game_number % 2 == 1:

                first_agent = nexus
                second_agent = titan

            else:

                first_agent = titan
                second_agent = nexus

            result = self.run_game(
                first_agent,
                second_agent,
                game_number
            )

            print(
                f"Game {result['game']}: "
                f"{result['first']} starts | "
                f"Winner: {result['winner']} | "
                f"Moves: {result['moves']} | "
                f"Time: {result['time']}s"
            )

    # =========================================================
    # SAVE 10 GAME RESULTS
    # =========================================================

    def save_results(
        self,
        filename="results/results.csv"
    ):

        if not self.results:
            return

        fieldnames = [
            "game",
            "first",
            "winner",
            "moves",
            "nexus_nodes",
            "titan_nodes",
            "nexus_pruned",
            "titan_pruned",
            "time"
        ]

        with open(
            filename,
            "w",
            newline=""
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()
            writer.writerows(self.results)

        print(
            f"\nResults saved to {filename}"
        )

    # =========================================================
    # SUMMARY
    # =========================================================

    def summary(self):

        nexus_wins = sum(
            1
            for r in self.results
            if r["winner"] == "NEXUS"
        )

        titan_wins = sum(
            1
            for r in self.results
            if r["winner"] == "TITAN"
        )

        draws = sum(
            1
            for r in self.results
            if r["winner"] == "DRAW"
        )

        avg_nodes_nexus = (
            sum(
                r["nexus_nodes"]
                for r in self.results
            )
            / len(self.results)
        )

        avg_nodes_titan = (
            sum(
                r["titan_nodes"]
                for r in self.results
            )
            / len(self.results)
        )

        avg_time = (
            sum(
                r["time"]
                for r in self.results
            )
            / len(self.results)
        )

        print("\n========== SUMMARY ==========")

        print(
            "NEXUS wins :",
            nexus_wins
        )

        print(
            "TITAN wins :",
            titan_wins
        )

        print(
            "Draws      :",
            draws
        )

        print(
            "Average NEXUS nodes :",
            round(avg_nodes_nexus, 2)
        )

        print(
            "Average TITAN nodes :",
            round(avg_nodes_titan, 2)
        )

        print(
            "Average time/game   :",
            round(avg_time, 6),
            "seconds"
        )

    # =========================================================
    # DEPTH EXPERIMENT
    # =========================================================

    def run_depth_experiment(self):

        print(
            "\n========== DEPTH EXPERIMENT ==========\n"
        )

        depth_results = []

        # Only NEXUS depth changes.
        # TITAN remains fixed at depth 3.
        for depth in [1, 2, 3, 4]:

            game = TicTacToe()

            nexus = Nexus(
                player="X",
                depth=depth
            )

            titan = Titan(
                player="O",
                depth=3
            )

            agents = {
                "X": nexus,
                "O": titan
            }

            current_player = "X"

            move_count = 0

            nexus_nodes = 0
            nexus_pruned = 0

            start_time = time.perf_counter()

            while not game.is_terminal():

                agent = agents[current_player]

                move, score, stats = agent.choose_move(
                    game
                )

                if move is None:
                    break

                game.make_move(
                    move[0],
                    move[1],
                    current_player
                )

                move_count += 1

                if agent.name == "NEXUS":

                    nexus_nodes += stats.nodes_evaluated
                    nexus_pruned += stats.nodes_pruned

                current_player = (
                    "O"
                    if current_player == "X"
                    else "X"
                )

            elapsed_time = (
                time.perf_counter()
                - start_time
            )

            winner = game.check_winner()

            if winner is None:

                result = "DRAW"

            elif winner == "X":

                result = "NEXUS WIN"

            else:

                result = "TITAN WIN"

            row = {
                "depth": depth,
                "result": result,
                "moves": move_count,
                "nodes_evaluated": nexus_nodes,
                "nodes_pruned": nexus_pruned,
                "time": round(
                    elapsed_time,
                    6
                )
            }

            depth_results.append(row)

            print(
                f"Depth {depth} | "
                f"Result: {result} | "
                f"Moves: {move_count} | "
                f"Nodes: {nexus_nodes} | "
                f"Pruned: {nexus_pruned} | "
                f"Time: {elapsed_time:.6f}s"
            )

        # Save depth experiment
        filename = (
            "results/depth_experiment.csv"
        )

        with open(
            filename,
            "w",
            newline=""
        ) as file:

            fieldnames = [
                "depth",
                "result",
                "moves",
                "nodes_evaluated",
                "nodes_pruned",
                "time"
            ]

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()
            writer.writerows(depth_results)

        print(
            f"\nDepth experiment saved to {filename}"
        )