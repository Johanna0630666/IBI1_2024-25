# spatial_SIR.py

import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# 1. Define simulation parameters
# ----------------------------
grid_size = 100          # Grid size (100x100)
beta = 0.2               # Infection probability per neighbor
gamma = 0.05             # Recovery probability
time_steps = 101         # Simulate 101 time points (from t=0 to t=100)

# ----------------------------
# 2. Initialize the population grid
# ----------------------------
# State encoding:
# 0 = susceptible
# 1 = infected
# 2 = recovered
population = np.zeros((grid_size, grid_size), dtype=int)

# Randomly select one individual to start the outbreak
outbreak = np.random.choice(grid_size, size=2)
population[outbreak[0], outbreak[1]] = 1

# ----------------------------
# 3. Setup plotting (animated)
# ----------------------------
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots(figsize=(6, 4), dpi=150)

# ----------------------------
# 4. Simulate disease spread
# ----------------------------

# Pseudocode:
# For each time step:
#   1. Copy the current population grid to avoid in-place updates
#   2. Find coordinates of all infected individuals
#   3. For each infected individual:
#       a. Possibly recover (with probability gamma)
#       b. Try to infect all 8 neighboring cells (with probability beta)
#   4. Replace the population grid with the updated version
#   5. Plot the current grid as a heat map

for t in range(time_steps):
    new_population = population.copy()

    # Step 1: Find all currently infected cells
    infected_x, infected_y = np.where(population == 1)

    # Step 2: Process each infected cell
    for x, y in zip(infected_x, infected_y):

        # Step 2a: Recovery check
        if np.random.rand() < gamma:
            new_population[x, y] = 2
            continue

        # Step 2b: Attempt to infect neighbors
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue  # Skip self
                nx, ny = x + dx, y + dy
                if 0 <= nx < grid_size and 0 <= ny < grid_size:
                    if population[nx, ny] == 0 and np.random.rand() < beta:
                        new_population[nx, ny] = 1

    # Step 3: Update population grid
    population = new_population

    # Step 4: Plot current grid
    ax.clear()
    img = ax.imshow(population, cmap='viridis', interpolation='nearest')
    ax.set_title(f"Time step: {t}")
    ax.set_xlabel("X coordinate")
    ax.set_ylabel("Y coordinate")
    plt.pause(0.1)

# ----------------------------
# 5. Finish animation
# ----------------------------
plt.ioff()
plt.show()