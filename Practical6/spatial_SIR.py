# spatial_SIR.py

import numpy as np # Import NumPy for numerical operations
import matplotlib.pyplot as plt # Import Matplotlib for plotting

# 1. Define simulation parameters

grid_size = 100          # Grid size (100x100)
beta = 0.2               # Infection probability per neighbor
gamma = 0.05             # Recovery probability
time_steps = 101         # Simulate 101 time points (from t=0 to t=100)

# 2. Initialize the population grid
# State encoding:
# 0 = susceptible
# 1 = infected
# 2 = recovered
population = np.zeros((grid_size, grid_size), dtype=int) # Create a grid of zeros (susceptible individuals)

# Randomly select one individual to start the outbreak
outbreak = np.random.choice(grid_size, size=2) # Randomly select a position in the grid for the outbreak
population[outbreak[0], outbreak[1]] = 1 # Mark the selected individual as infected


# 3. Setup plotting (animated)
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots(figsize=(6, 4), dpi=150) # Create a figure and axis for plotting


# 4. Simulate disease spread
for t in range(time_steps): 
    new_population = population.copy() # Create a copy of the current population grid to update

    infected_x, infected_y = np.where(population == 1) # Get coordinates of infected individuals
    for x, y in zip(infected_x, infected_y): # Iterate over each infected individual

        if np.random.rand() < gamma: # Randomly decide if the infected individual recovers
            new_population[x, y] = 2 # Mark as recovered
            continue # Recover infected individual

        for dx in [-1, 0, 1]: # Iterate over neighboring cells
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0: # Skip the current cell (self)
                    continue  # Skip self
                nx, ny = x + dx, y + dy # Calculate neighbor coordinates
                if 0 <= nx < grid_size and 0 <= ny < grid_size: # Check if neighbor coordinates are within grid bounds
                    if population[nx, ny] == 0 and np.random.rand() < beta: # If neighbor is susceptible and infection occurs
                        new_population[nx, ny] = 1 # Mark neighbor as infected

    population = new_population # Update the population grid with the new state

    # Plot current grid
    ax.clear() # Clear the axis for the new plot
    img = ax.imshow(population, cmap='viridis', interpolation='nearest') # Display the population grid
    ax.set_title(f"Time step: {t}") # Set the title to show the current time step
    ax.set_xlabel("X coordinate") # Set the x-axis label
    ax.set_ylabel("Y coordinate") # Set the y-axis label
    plt.pause(0.1) # Pause to update the plot


# 5. Finish animation
plt.ioff() # Turn off interactive mode
plt.show() # Show the final plot after the simulation ends