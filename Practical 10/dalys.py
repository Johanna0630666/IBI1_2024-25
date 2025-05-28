# dalys.py - Practical 10: Global Health Data Analysis

import os
import pandas as pd
import matplotlib.pyplot as plt

#  Import the .csv file
file_path = "C:/Users/frank/Desktop/IBI1/IBI1_2024-25/Practical 10/dalys-rate-from-all-causes.csv"
dalys_data = pd.read_csv(file_path)

# Show the third column (the year) for the first 10 rows (inclusive)
print("\nFirst 10 years (column 3):")
print(dalys_data.iloc[0:10, 2])

# Get the 10th year of DALYs data for Afghanistan
afghanistan_years = dalys_data.loc[dalys_data.Entity == "Afghanistan", "Year"]
print("\nThe 10th year with DALYs data recorded in Afghanistan was:", afghanistan_years.iloc[9])

# Use a Boolean to show DALYs for all countries in 1990
print("\nDALYs for all countries in 1990:")
dalys_1990 = dalys_data[dalys_data.Year == 1990]
print(dalys_1990[["Entity", "DALYs"]])

# Compute mean DALYs in the UK and France
uk = dalys_data[dalys_data.Entity == "United Kingdom"]
france = dalys_data[dalys_data.Entity == "France"]
mean_uk = uk.DALYs.mean()
mean_france = france.DALYs.mean()
print("\nMean DALYs in the United Kingdom:", mean_uk)
print("Mean DALYs in France:", mean_france)
# Comment: Compare UK and France
if mean_uk > mean_france:
    print("The mean DALYs in the UK is greater than in France.")
else:
    print("The mean DALYs in the UK is smaller than in France.")

# Create a plot showing the DALYS over time in the UK
plt.figure(figsize=(10, 5))
plt.plot(uk.Year, uk.DALYs, 'bo-', label='UK DALYs')
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title("DALYs Over Time in the United Kingdom")
plt.xticks(uk.Year, rotation=90)
plt.legend()
plt.tight_layout()
plt.show()

# Question: What country or countries have recorded a DALYs greater than 650,000 in a single year?
high_dalys = dalys_data[dalys_data.DALYs > 650000][["Entity", "Year", "DALYs"]]
print("\nCountries with DALYs > 650,000:")
print(high_dalys)
