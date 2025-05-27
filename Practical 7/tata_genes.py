import re # Importing the regular expression module

def parse_fasta(file_path): # Function to parse a FASTA file
    sequences = {} # Dictionary to hold gene names and their sequences
    gene_name = "" 
    seq_lines = [] 

    with open(file_path, 'r') as file: # Open the FASTA file for reading
        for line in file:
            line = line.strip() # Remove leading and trailing whitespace
            if line.startswith(">"): # If the line starts with '>', it indicates a new gene
                if gene_name and seq_lines: # Store the previous gene sequence
                    sequences[gene_name] = ''.join(seq_lines) # Join the sequence lines into a single string
                # Keep only the gene name (the first underscore-separated part after '>')
                gene_name = line[1:].split()[0].split('_')[0] # Reset gene name
                seq_lines = [] # Reset sequence lines for the new gene
            else:
                seq_lines.append(line) # Append the sequence line to the list

        # Store the last sequence in the dictionary
        if gene_name and seq_lines:
            sequences[gene_name] = ''.join(seq_lines)

    return sequences


def find_tata_box_sequences(sequences): # Function to find sequences with TATA box
    tata_pattern = re.compile(r'TATA[AT]A[AT]') # Regular expression to match TATA box sequences
    matched_sequences = {} # Dictionary to hold sequences that match the TATA box pattern

    for gene, sequence in sequences.items(): # Iterate through each gene and its sequence
        if tata_pattern.search(sequence): # If the TATA box pattern is found in the sequence
            matched_sequences[gene] = sequence # Store the gene and its sequence

    return matched_sequences


def write_fasta(output_path, matched_sequences): # Function to write matched sequences to a FASTA file

    with open(output_path, 'w') as out_file: # Open the output file for writing
        for gene, seq in matched_sequences.items(): # Iterate through each matched sequence
            out_file.write(f">{gene}\n") # Write the gene name as a header
            for i in range(0, len(seq), 60): # Write the sequence in lines of 60 characters
                out_file.write(seq[i:i+60] + '\n')


if __name__ == "__main__": # Main function to execute the script
    input_file = "C:/Users/frank/Desktop/IBI1/IBI1_2024-25/Practical7/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
    output_file = "C:/Users/frank/Desktop/IBI1/IBI1_2024-25/Practical7/tata_genes.fa"

    sequences = parse_fasta(input_file) # Parse the input FASTA file to get gene sequences
    matched_sequences = find_tata_box_sequences(sequences) # Find sequences that contain the TATA box
    write_fasta(output_file, matched_sequences) # Write the matched sequences to the output FASTA file

    print(f"{len(matched_sequences)} sequences with TATA box written to {output_file}") # Print the number of sequences found with TATA box