from flask import Flask, render_template
import numpy as np

app = Flask(__name__)

# Set the size of the grid
grid_size = (20, 40)

# Create a grid with random initial state
grid = np.random.choice([0, 1], size=grid_size)

# Function to update the grid based on the transition rules
def update_grid(grid):
    new_grid = np.copy(grid)
    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            neighborhood = grid[i - 1:i + 2, j - 1:j + 2]  # if cell is (1,1) then grid[0,1,2 : 0,1,2]
            neighbors = np.sum(neighborhood)  - grid[i, j]
            if grid[i, j] == 1:
                # Death Loneliness/ Overpopulation
                if neighbors <= 1 or neighbors >= 4:
                    new_grid[i, j] = 0
            else:
                # Birth
                if neighbors == 3:
                    new_grid[i, j] = 1
    return new_grid

# Function to convert the grid to a list of lists for rendering in HTML
def grid_to_list(grid):
    grid_list = []
    for row in grid:
        row_list = []
        for cell in row:
            cell_str = str(cell)
            row_list.append(cell_str)
        grid_list.append(row_list)
    return grid_list

# Route to display the grid as an HTML table
@app.route('/')
def display_grid():
    return render_template('grid.html')

# Route to get the grid data as JSON
@app.route('/get_grid')
def get_grid():
    global grid
    grid = update_grid(grid)  # Update the grid
    print(f"grid {grid}")
    grid_list = grid_to_list(grid)
    print(f"grid_list {grid_list}")
    return {'result': grid_list}

# Function to randomize the grid with a new random configuration
def randomize_grid():
    global grid
    grid = np.random.choice([0, 1], size=grid_size)
    return {'result': 'Randomized'}

# Route to randomize the grid
@app.route('/randomize_grid')
def randomize_grid_route():
    return randomize_grid()

if __name__ == '__main__':
    app.run(debug=True)
