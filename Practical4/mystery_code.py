# What does this piece of code do?
# Answer: This code tests how many iterations are needed before two randomly generated integers, each within the range 1 to 6 inclusive, are equal.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5

from random import randint
# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5 

from math import ceil 
progress=0 # Initialize progress to 0.
while progress>=0: # Loop until progress is breaked.
	progress+=1 # Increment progress by 1.                       
	first_n = randint(1,6) # Draw a random number between 1 and 6.
	second_n = randint(1,6) # Draw a random number between 1 and 6.
	if first_n == second_n: # Check if the two numbers are equal.      
		print(progress) # print progress (indicating how many times the computer has run)
		break # Exit the loop if the two numbers are equal.
