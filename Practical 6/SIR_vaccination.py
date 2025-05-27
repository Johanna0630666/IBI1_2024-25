
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Simulation settings

N = 10000                     # Total population
initial_infected = 1          # Initially infected
initial_recovered = 0         # Initially recovered
beta = 0.3                    # Infection rate
gamma = 0.05                  # Recovery rate
time_steps = 1000             # Total time steps for simulation
vaccination_rates = [i / 10 for i in range(11)]  # 0% to 100% in 10% steps


# 2. Simulation function
def run_simulation(vaccinated_ratio):
    V = int(N * vaccinated_ratio)         
    S = max(N - initial_infected - initial_recovered - V, 0)
    I = initial_infected
    R = initial_recovered
    
    S_list = [S]
    I_list = [I]
    R_list = [R]

    for t in range(time_steps):
        prob_infection = beta * I / N

        if S > 0:
            new_infections = np.sum(np.random.choice(
                range(2), size=S, p=[1 - prob_infection, prob_infection]))
        else:
            new_infections = 0

        if I > 0:
            new_recoveries = np.sum(np.random.choice(
                range(2), size=I, p=[1 - gamma, gamma]))
        else:
            new_recoveries = 0

        S = max(S - new_infections, 0)
        I = max(I + new_infections - new_recoveries, 0)
        R = R + new_recoveries

        S_list.append(S)
        I_list.append(I)
        R_list.append(R)

    return I_list


# Plotting results
plt.figure(figsize=(12, 7))

for idx, vac_rate in enumerate(vaccination_rates):
    I_curve = run_simulation(vac_rate)
    color = cm.viridis(idx / len(vaccination_rates))  # Use colormap
    plt.plot(I_curve, label=f"{int(vac_rate * 100)}%", color=color)

plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR model with different vaccination rates")
plt.legend(title="Vaccination Rate")
plt.grid(True)
plt.tight_layout()
plt.show()