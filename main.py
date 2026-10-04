from experiment import Experiment


def main():

    experiment = Experiment()

    # Run 10 AI vs AI games
    experiment.run_10_games()

    # Save game results
    experiment.save_results()

    # Display summary
    experiment.summary()

    # Run depth experiment
    experiment.run_depth_experiment()


if __name__ == "__main__":
    main()