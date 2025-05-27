import re

def parse_fasta(file_path): # Function to parse a FASTA file and extract gene sequences
    sequences = {}
    gene_name = ""
    seq_lines = []

    with open(file_path, 'r') as file: # Open the FASTA file for reading
        for line in file: 
            line = line.strip() # Remove leading and trailing whitespace
            if line.startswith(">"):
                if gene_name and seq_lines: # Store the previous gene sequence
                    sequences[gene_name] = ''.join(seq_lines)
                gene_name = line[1:].split()[0].split('_')[0] # Reset gene name to the first part after '>'
                seq_lines = [] # Reset sequence lines for the new gene
            else: # If the line is a sequence line, append it to seq_lines
                seq_lines.append(line)
        if gene_name and seq_lines: # Store the last sequence in the dictionary
            sequences[gene_name] = ''.join(seq_lines) # Join the sequence lines into a single string
    return sequences


def count_tata_and_filter(sequences, splice_pattern): # Function to count TATA boxes in sequences and filter based on splice motif
    tata_pattern = re.compile(r'TATA[AT]A[AT]') # Regular expression to match TATA box sequences
    filtered = {} # Dictionary to hold filtered sequences with TATA box and splice motif

    for gene, seq in sequences.items(): # Iterate through each gene and its sequence
        if splice_pattern in seq: # Check if the splice motif is present in the sequence
            tata_matches = tata_pattern.findall(seq)
            if tata_matches: # If TATA box matches are found
                tata_count = len(tata_matches)
                filtered[f"{gene}|{tata_count}"] = seq # Store the gene name with TATA count in the header
    return filtered


def write_fasta(output_path, gene_seqs): # Function to write gene sequences to a FASTA file
    with open(output_path, 'w') as out_file: # Open the output file for writing
        for header, seq in gene_seqs.items(): 
            out_file.write(f">{header}\n{seq}\n") # Write the gene name and sequence to the file


if __name__ == "__main__": # Main function to execute the script
    valid_motifs = {"GTAG", "GCAG", "ATAC"} # Set of valid splice motifs
    splice = input("Enter a splice motif (GTAG, GCAG, or ATAC): ").strip().upper() 

    if splice not in valid_motifs: # Check if the entered motif is valid
        print("Invalid motif. Please enter one of: GTAG, GCAG, ATAC")
        exit()

    # Read file and process sequences
    input_file = "C:/Users/frank/Desktop/IBI1/IBI1_2024-25/Practical7/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
    output_file = f"C:/Users/frank/Desktop/IBI1/IBI1_2024-25/Practical7/{splice}_spliced_genes.fa"

    sequences = parse_fasta(input_file) # Parse the input FASTA file to get gene sequences
    filtered_sequences = count_tata_and_filter(sequences, splice) # Count TATA boxes and filter sequences based on the splice motif
    write_fasta(output_file, filtered_sequences) # Write the filtered sequences to the output FASTA file

    # Print result
    print(f"{len(filtered_sequences)} sequences with TATA box and {splice} motif written to {output_file}")