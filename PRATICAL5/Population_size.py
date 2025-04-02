# Procedures:
# 1. Create two lists of the population of UK countries and Zhejiang-neighbouring provinces.
# 2. Sort the lists.
# 3. Print the sorted lists.
# 4. Create a pie chart to visualize the population of UK countries and Zhejiang-neighbouring provinces.
# 5. actual code 
uk_countries=[57.11,3.13,1.91,5.45] # Create a list of the population of UK countries.
China_countries=[65.77,41.88,45.28,61.27,85.15] # Create a list of the population of Zhejiang-neighbouring provinces.
uk_sorted=sorted(uk_countries)
China_sorted=sorted(China_countries) # Sort the lists.
print("Sorted UK countries by population:",uk_sorted)
print("Sorted Zhejiang-neighbouring provinces by population:",China_sorted) # Print the sorted lists.
uk_countries_dic={"England": 57.11, "Wales": 3.13, "Northern Ireland": 1.91, "Scotland": 5.45}
China_countries_dic={"Zhejiang": 65.77, "Fujian": 41.88, "Jiangxi": 45.28, "Anhui": 61.27, "Jiangsu": 85.15} # Create dictionaries for UK countries and Zhejiang-neighbouring provinces.

import matplotlib.pyplot as plt # Import matplotlib for visualization.
plt.figure(figsize=(8, 6)) # Set the figure size.
uk_values=list(uk_countries_dic.values())
uk_labels=list(uk_countries_dic.keys()) # Get the labels and values for UK countries.
China_labels=list(China_countries_dic.keys())
China_values=list(China_countries_dic.values()) # Get the labels and values for Zhejiang-neighbouring provinces.

plt.subplot(1, 2, 1) # Create a subplot for UK countries.
plt.pie(uk_values,labels=uk_labels,autopct='%1.1f%%',startangle=90) # Create a pie chart for UK countries.
plt.title("Population of UK countries") # Set a title.
plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.

plt.subplot(1, 2, 2) # Create a subplot for Zhejiang-neighbouring provinces.
plt.pie(China_values,labels=China_labels,autopct='%1.1f%%',startangle=90) # Create a pie chart for Zhejiang-neighbouring provinces.
plt.title("Population of Zhejiang-neighbouring provinces") # Set a title.
plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show() # Show the pie charts.



