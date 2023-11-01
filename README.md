# Conway's Game of Life

Conway's Game of Life is a classic cellular automaton that simulates the evolution of a grid of cells. The cells can be in one of two states: alive (1) or dead (0). The state of each cell in the grid evolves over time based on simple rules.

## Getting Started

To run this implementation of Conway's Game of Life, you'll need Python and the Flask web framework. You can install Flask using pip:

```bash
pip install flask
pip install numpy
```

Once you have Flask installed, you can run the application by executing the following code in your terminal:

```python
python app.py
```

This will start a local web server, and you can access the application in your web browser at `http://localhost:5000`.

## Code Overview

### Grid Initialization

In this implementation, we create a grid of cells with a random initial state. You can set the size of the grid by modifying the `grid_size` variable. The grid is represented as a NumPy array where each cell is either 0 (dead) or 1 (alive).

### Updating the Grid

The `update_grid` function defines the rules for updating the grid. The rules are as follows:

- If a live cell has fewer than 2 live neighbors or more than 3 live neighbors, it dies.
- If a dead cell has exactly 3 live neighbors, it becomes alive.

The `get_grid` route updates the grid based on these rules and returns the new state as JSON.

### Displaying the Grid

The `/` route renders the current grid as an HTML table using the `grid.html` template.

### Randomizing the Grid

You can randomize the grid with a new random configuration by accessing the `/randomize_grid` route.

## Usage

- Visit `http://localhost:5000` in your web browser to see the grid and its evolution.
- Click the "Randomize" button to randomize the grid with a new configuration.
- Use the "Start" button to begin the Game of Life simulation, allowing the grid to evolve over time.
- If you want to pause the simulation temporarily, click the "Pause" button. This allows you to closely examine the current state of the grid.


![First page](https://github.com/IuliaVrabie/Game-of-Life/blob/d54003f70ec95486a394cc0fc17a6efee46b5a6d/Interface.png)
