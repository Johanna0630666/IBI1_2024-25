# Pseudocode:
# 1. The nth triangular number is the sum of integers from 1 to n.
# 2. Use a while loop to calculates the triangular sequence and displays the first ten values.
# 3. Print out the calculation results.

# Actual code:
total=0 # Initialize total to 0.
n=1 # Start with the first number.

# Loop to calculate the sum of the first ten numbers.
while n<=10:
    total=total+n  # Add n to total.
    print("The sum of the first",n,"numbers is",total) # Print the result. 
    n=n+1 # Increment n by 1 to move to the next number.
# The loop continues until n exceeds 10, at which point the program ends.
