#Pseudicode:
# 1. Create a dictionary with programming languages and their popularity percentages.
# 2. Let the user to input a programming language to check.
# 3. Give the user the percentage of developers using that language.
# 4. If the language is not in the dictionary, inform the user.
# 5. Create a bar chart to visualize the popularity of programming languages.
# Actual code:
language={"JavaScript": 62.3, "HTML":52.9, "Python":51, "SQL":51, "TypeScript": 38.5} # Create a dictionary with programming languages and their popularity percentages.
print("Current language popularity dictionary:")
print(language)  # Print the dictionary so users can see the full list
target_language=input("Enter the programming language you want to check: ") # Let the user to input a programming language to check.
if target_language in language:
    target_percentage=language[target_language] 
    print(f"{target_language} is used by {target_percentage}% of developers") # If the language is in the dictionary, give the user the percentage of developers using that language.
else:
    print(f"{target_language} is not in the list") # If the language is not in the dictionary, inform the user.
import numpy as np # Import numpy for numerical operations.
import matplotlib.pyplot as plt # Import matplotlib for visualization.
N=len(language) # Get the number of programming languages.  
percentage=list(language.values()) # Get the popularity percentages of programming languages.
x=np.arange(N) # Create an array of x-coordinates
width=0.3 # Set the width of the bars
plt.bar(x, percentage, width, color="blue") 
plt.title("Programming language popularity") # Set the title of the bar chart.
plt.xlabel("programming languages") # Set the x-axis label.
plt.ylabel("percentage(%)") # Set the y-axis label.
plt.xticks(x,language.keys()) # Set the x-ticks to the programming language names.
plt.yticks(np.arange(0, 101, 10)) # Set the y-ticks to range from 0 to 100 with a step of 10.
plt.show() # Show the bar chart.
