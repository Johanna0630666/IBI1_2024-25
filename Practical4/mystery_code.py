# What does this piece of code do?
# Answer:Generate two random numbers from 1 to 6 until they are equal. If they are equal,terminate the loop; otherwise, continue.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0
while progress>=0:
	progress+=1                         #if not end, progress+1
	first_n = randint(1,6)
	second_n = randint(1,6)
	if first_n == second_n:             #if equal, break, which means that the probability of the end is 1/6
		print(progress)
		break

