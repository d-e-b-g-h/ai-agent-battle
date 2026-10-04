# 🤖 AI Agent Battle — Tic-Tac-Toe

> An AI-vs-AI Tic-Tac-Toe system implementing Minimax, Alpha-Beta Pruning, heuristic evaluation, configurable search depth, and performance analysis.

---

## 📌 Overview

**AI Agent Battle** is a Python-based Artificial Intelligence project that demonstrates intelligent decision-making in a competitive game environment.

Instead of implementing a simple human-vs-computer Tic-Tac-Toe game, this project focuses on **AI agent behavior, adversarial search, heuristic evaluation, and performance analysis**.

The system contains two independent AI agents:

- **NEXUS** — a threat-oriented strategic agent
- **TITAN** — a positional strategic agent

Both agents use **Minimax with Alpha-Beta Pruning**, while using different heuristic evaluation functions.

The agents compete against each other in automated matches, while the system records search and performance statistics such as:

- Nodes evaluated
- Nodes pruned
- Search depth
- Number of moves
- Execution time
- Game results

---

## 🎯 Objectives

The main objectives of this project are:

1. Implement a complete Tic-Tac-Toe game engine.
2. Implement the Minimax adversarial search algorithm.
3. Optimize Minimax using Alpha-Beta pruning.
4. Design heuristic evaluation functions for non-terminal states.
5. Create two AI agents with different strategies.
6. Support configurable search depth.
7. Run AI-vs-AI matches automatically.
8. Measure computational performance.
9. Analyze the effect of search depth on AI behavior.
10. Store experimental results in CSV format.

---

## 🧠 Artificial Intelligence Techniques

### Minimax Search

Minimax is a recursive adversarial search algorithm used by the AI agents to select the best possible move.

The search alternates between two roles:

- **MAX** — the AI agent attempts to maximize the evaluation score.
- **MIN** — the opponent attempts to minimize the evaluation score.

Terminal states are evaluated using the following scoring system:

| Game State | Score |
|------------|------:|
| AI Win | +100 |
| Draw | 0 |
| Opponent Win | -100 |

The search depth is configurable, allowing the effect of deeper look-ahead to be studied.

---

### Alpha-Beta Pruning

Alpha-Beta pruning is used to optimize Minimax by eliminating branches that cannot influence the final decision.

Two values are maintained:

- **Alpha** — the best value currently guaranteed for MAX.
- **Beta** — the best value currently guaranteed for MIN.

A branch is pruned when:

```text
Beta <= Alpha
```

This reduces unnecessary exploration while preserving the decision produced by Minimax.

The implementation also records:

- Nodes evaluated
- Nodes pruned

This allows the efficiency of the search process to be measured experimentally.

---

## 📊 Heuristic Evaluation

When the search reaches the configured depth before reaching a terminal game state, a heuristic function evaluates the board position.

Two different heuristics are used by the agents.

### NEXUS — Heuristic H1

NEXUS uses a threat-oriented heuristic based on:

- Winning lines
- Player alignment
- Opponent alignment
- Immediate winning threats

The heuristic rewards positions that create opportunities for NEXUS and penalizes positions that create threats for the opponent.

### TITAN — Heuristic H2

TITAN uses a positional heuristic based on:

- Winning lines
- Player alignment
- Opponent alignment
- Center control
- Corner control

This gives TITAN a different evaluation strategy from NEXUS.

---

## 🤖 AI Agents

### NEXUS

```text
Agent Name : NEXUS
Algorithm  : Minimax + Alpha-Beta Pruning
Heuristic  : H1
Default Depth : 3
Strategy   : Threat-oriented
```

NEXUS emphasizes creating and exploiting immediate threats.

### TITAN

```text
Agent Name : TITAN
Algorithm  : Minimax + Alpha-Beta Pruning
Heuristic  : H2
Default Depth : 3
Strategy   : Positional
```

TITAN places additional importance on center and corner control.

Both agents use deterministic search-based decision making rather than random moves.

---

## 🎮 Game Engine

The Tic-Tac-Toe game engine provides the environment in which the AI agents operate.

The engine supports:

- 3×3 board representation
- Legal move detection
- Move execution
- Winner detection
- Draw detection
- Terminal-state detection
- Board copying

The game engine is implemented in:

```text
game.py
```

---

## 🔄 AI Decision Pipeline

The overall decision-making process is:

```text
                Current Board
                     │
                     ▼
             Generate Legal Moves
                     │
                     ▼
              Apply Candidate Move
                     │
                     ▼
                Minimax Search
                 /          \
                /            \
              MAX            MIN
               │              │
              AI           Opponent
                \            /
                 \          /
                  ▼        ▼
              Alpha-Beta Pruning
                     │
                     ▼
             Evaluate Board State
                     │
                     ▼
             Compare All Moves
                     │
                     ▼
                Best Move
```

---

# 📁 Project Structure

```text
ai-agent-battle/
│
├── main.py
├── game.py
├── minimax.py
├── heuristic.py
├── agents.py
├── experiment.py
├── README.md
│
└── results/
    ├── results.csv
    └── depth_experiment.csv
```

### File Description

| File | Description |
|------|-------------|
| `main.py` | Main entry point of the project |
| `game.py` | Tic-Tac-Toe game engine |
| `minimax.py` | Minimax and Alpha-Beta implementation |
| `heuristic.py` | Heuristic evaluation functions |
| `agents.py` | NEXUS and TITAN AI agents |
| `experiment.py` | AI-vs-AI and depth experiments |
| `results/results.csv` | Results of the 10 AI-vs-AI games |
| `results/depth_experiment.csv` | Results of the search-depth experiment |
| `README.md` | Project documentation |

---

# 🧪 Experiments

## Experiment 1 — Search Depth

The first experiment studies the effect of search depth on AI decision-making and computational cost.

NEXUS is tested at the following depths:

```text
Depth 1
Depth 2
Depth 3
Depth 4
```

TITAN remains fixed at depth 3.

The following metrics are recorded:

- Search depth
- Game result
- Number of moves
- Nodes evaluated
- Nodes pruned
- Execution time

Results are stored in:

```text
results/depth_experiment.csv
```

### Purpose

The experiment demonstrates the relationship between search depth and computational cost.

Increasing the search depth allows the agent to look further into possible future states, but also increases the number of states that must be evaluated.

The experiment therefore provides a practical comparison between:

```text
Search Depth
     ↓
Look-Ahead Capability
     ↓
Search Space
     ↓
Computational Cost
```

---

## Experiment 2 — AI Agent Battle

The second experiment consists of **10 AI-vs-AI matches** between NEXUS and TITAN.

The starting player alternates between the two agents.

```text
Game 1  → NEXUS starts
Game 2  → TITAN starts
Game 3  → NEXUS starts
Game 4  → TITAN starts
Game 5  → NEXUS starts
Game 6  → TITAN starts
Game 7  → NEXUS starts
Game 8  → TITAN starts
Game 9  → NEXUS starts
Game 10 → TITAN starts
```

For every game, the following information is recorded:

- Game number
- Starting agent
- Winner
- Number of moves
- NEXUS nodes evaluated
- TITAN nodes evaluated
- NEXUS nodes pruned
- TITAN nodes pruned
- Execution time

Results are stored in:

```text
results/results.csv
```

---

# 📈 Experimental Results

The completed 10-game AI-vs-AI experiment produced the following results:

| Metric | Result |
|--------|-------:|
| Total Games | 10 |
| NEXUS Starts | 5 |
| TITAN Starts | 5 |
| NEXUS Wins | 0 |
| TITAN Wins | 0 |
| Draws | 10 |
| Moves per Game | 9 |

### Observation

All 10 games ended in draws.

This indicates that, under the selected depth and heuristic configurations, both agents were able to consistently avoid losing against the other agent.

The experiment also demonstrates the effect of different heuristics on search behavior through the recorded node counts and pruning statistics.

---

# 📊 Performance Metrics

The project measures both search performance and execution performance.

### Nodes Evaluated

The number of evaluated nodes indicates how many search states reached an evaluation point during the search.

### Nodes Pruned

The number of pruning events indicates how often Alpha-Beta pruning eliminated further exploration of a branch.

### Execution Time

Execution time measures the computational cost required to make decisions and complete the games.

These metrics allow the AI agents to be compared beyond simply counting wins and losses.

---

# ⚙️ Technologies Used

- **Python 3**
- Minimax Search
- Alpha-Beta Pruning
- Heuristic Evaluation
- Object-Oriented Programming
- CSV Data Storage
- Performance Measurement

No external Tic-Tac-Toe AI or Minimax library is used.

---

# ▶️ Installation and Execution

## 1. Clone the Repository

```bash
git clone <your-repository-url>
cd ai-agent-battle
```

## 2. Verify Python

```bash
python3 --version
```

Python 3 is required.

## 3. Run the Project

```bash
python3 main.py
```

The program will:

1. Run 10 AI-vs-AI games.
2. Alternate the starting player.
3. Record game statistics.
4. Save the results to `results/results.csv`.
5. Display an overall performance summary.
6. Run the search-depth experiment.
7. Save the depth experiment results to `results/depth_experiment.csv`.

---

# 📄 Output Files

## `results/results.csv`

Contains the results of the 10 AI-vs-AI games.

Example structure:

```csv
game,first,winner,moves,nexus_nodes,titan_nodes,nexus_pruned,titan_pruned,time
1,NEXUS,DRAW,9,386,207,94,70,0.003056
2,TITAN,DRAW,9,248,367,66,94,0.002644
3,NEXUS,DRAW,9,386,207,94,70,0.002767
```

---

## `results/depth_experiment.csv`

Contains the results of the search-depth experiment.

Example structure:

```csv
depth,result,moves,nodes_evaluated,nodes_pruned,time
1,DRAW,...
2,DRAW,...
3,DRAW,...
4,DRAW,...
```

---

# 🧩 Object-Oriented Design

The project uses classes where they naturally fit the problem.

### `TicTacToe`

Represents the game environment and manages:

- Board state
- Legal moves
- Moves
- Game termination
- Winner detection

### `Agent`

Provides the base structure for AI agents.

### `Nexus`

Represents the NEXUS AI agent.

### `Titan`

Represents the TITAN AI agent.

### `SearchStats`

Stores search-related performance statistics.

### `Experiment`

Manages:

- AI-vs-AI matches
- Search-depth experiments
- Result collection
- CSV generation
- Performance summaries

---

# 📚 Learning Outcomes

This project demonstrates practical implementation and understanding of:

- Artificial Intelligence
- Adversarial Search
- Minimax
- Alpha-Beta Pruning
- Heuristic Evaluation
- Game-State Representation
- Search Depth
- Intelligent Agent Design
- AI-vs-AI Competition
- Performance Measurement
- Experimental Analysis
- CSV-based Result Storage
- Object-Oriented Programming

---

# 🔍 Key Observations

### 1. Adversarial Decision Making

Both agents make decisions by considering not only their own possible moves but also the moves available to the opponent.

### 2. Effect of Search Depth

Increasing search depth allows an agent to consider more future possibilities.

However, deeper searches require more computational work.

### 3. Alpha-Beta Pruning

Alpha-Beta pruning reduces unnecessary search by eliminating branches that cannot influence the final Minimax decision.

### 4. Different Heuristics

NEXUS and TITAN use different board evaluation strategies.

Therefore, even though both agents use the same underlying Minimax + Alpha-Beta framework, their evaluation of non-terminal positions can differ.

### 5. First-Player Advantage

The experiment alternates the starting player to reduce the effect of always allowing the same agent to move first.

### 6. AI-vs-AI Performance

The 10-game experiment resulted in:

```text
NEXUS Wins : 0
TITAN Wins : 0
Draws      : 10
```

This shows that the selected configurations produced highly competitive gameplay between the two agents.

---

# 🚀 Future Improvements

The project can be extended in several ways:

- Human-vs-AI gameplay
- Graphical user interface
- Larger board sizes
- Adaptive search depth
- Additional heuristic functions
- Randomized tie-breaking
- Opening-book strategies
- Additional AI agents
- Tournament mode
- Automated performance graphs
- Larger statistical experiments
- Persistent experiment history
- Agent training and learning

---

# 🎓 Academic Relevance

This project provides a practical implementation of concepts from Artificial Intelligence, particularly:

```text
State Space Search
       ↓
Adversarial Search
       ↓
Minimax
       ↓
Alpha-Beta Pruning
       ↓
Heuristic Evaluation
       ↓
Intelligent Agents
       ↓
Performance Analysis
```

It demonstrates how theoretical AI algorithms can be implemented, tested, and evaluated using measurable experimental results.

---

# 👨‍💻 Author

**Debmalya Ghosh**

B.Tech Computer Science & Engineering  
University of Calcutta

---

# 📜 License

This project was developed for academic and educational purposes.