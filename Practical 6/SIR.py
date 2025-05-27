
# SIR.py

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
# Initialize parameters

N = 10000          # Total population
I = 1              # Initially infected
R = 0              # Initially recovered
S = N - I - R      # Initially susceptible

beta = 0.3         # Infection rate (probability of transmission per contact)
gamma = 0.05       # Recovery rate (probability of recovery per time step)

# Create arrays to store results
S_list = [S]
I_list = [I]
R_list = [R]

# Run simulation over 1000 time steps
time_steps = 1000

for t in range(time_steps):
    # Calculate the number of susceptible individuals
    # who can potentially get infected
    prob_infection = beta * I / N

    # Randomly determine new infections among susceptible individuals
    # Using np.random.choice to simulate the infection process
    new_infections = np.sum(np.random.choice(
        range(2), size=S, p=[1 - prob_infection, prob_infection]))

    # Randomly determine new recoveries among infected individuals
    new_recoveries = np.sum(np.random.choice(
        range(2), size=I, p=[1 - gamma, gamma]))

    # Update the counts of susceptible, infected, and recovered individuals
    S = max(S - new_infections, 0)
    I = max(I + new_infections - new_recoveries, 0)
    R = min(R + new_recoveries, N)

    # Store updated values for plotting
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)

# 4. Plot the results
plt.figure(figsize=(6, 4), dpi=150)

plt.plot(S_list, label='Susceptible', color='blue')
plt.plot(I_list, label='Infected', color='orange')
plt.plot(R_list, label='Recovered', color='green')

plt.xlabel('Time (days)')
plt.ylabel('Number of people')
plt.title('SIR Model Simulation')
plt.legend(loc='upper right')
plt.grid(True)

# Save the plot as PNG file
plt.savefig("SIR_model.png", format="png")

# Show the plot
plt.show()