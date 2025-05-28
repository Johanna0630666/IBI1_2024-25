# largest_intron.py

# Define the gene sequence
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'

# Initialize variable to store the maximum intron length
max_intron_length = 0

# Loop through the sequence to find GT (splice donor) sites
for i in range(len(seq) - 1): # Ensure we don't go out of bounds
    if seq[i:i+2] == 'GT': # Found a GT site
        for j in range(i + 2, len(seq) - 1): # Start searching for AG (splice acceptor) sites after the GT
            if seq[j:j+2] == 'AG': # Found an AG site
                intron_length = j + 2 - i  # Include both GT and AG
                if intron_length > max_intron_length: # Update max intron length if current is larger
                    max_intron_length = intron_length # Update the maximum intron length

# Print the result
print("Length of the largest intron:", max_intron_length)