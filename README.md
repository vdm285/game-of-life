# Conway's Game of Life

This repository contains a Python implementation of Conway's Game of Life, a cellular automaton devised by mathematician John Conway. The script simulates the evolution of a grid of cells, where each cell can either be alive or dead. The state of the grid evolves over time based on a simple set of rules.

## Features

- **Random Initialization**: The initial state of the grid is randomly generated.
- **Customizable Grid Size**: Modify the grid size to explore different patterns and behaviors.
- **Iteration Simulation**: The script efficiently computes and displays the next state of the grid at each iteration.

## How It Works

Conway's Game of Life follows these rules:
1. Any live cell with fewer than two live neighbors dies (underpopulation).
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies (overpopulation).
4. Any dead cell with exactly three live neighbors becomes a live cell (reproduction).

The script handles these rules by first creating a translation table that maps the current state and number of neighbors to the next state. It then iterates over the grid, updating each cell according to this table.

## Usage

1. **Run the Script**: Execute the `conway.py` script directly in a Python environment:
   ```bash
   python conway.py
