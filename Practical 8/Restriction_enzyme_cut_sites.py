# Restriction Enzyme Cut Sites Finder

def find_cut_sites(dna_sequence, recognition_sequence): # Function to find cut sites of a restriction enzyme in a DNA sequence
    dna_sequence = dna_sequence.upper() 
    recognition_sequence = recognition_sequence.upper() # Convert both sequences to uppercase for case-insensitive comparison

    # Validate sequences (must only contain A, C, G, T)
    valid_nucleotides = {'A', 'C', 'G', 'T'}
    if not set(dna_sequence).issubset(valid_nucleotides): # Check if DNA sequence contains only valid nucleotides
        return "Error: DNA sequence contains invalid characters."
    if not set(recognition_sequence).issubset(valid_nucleotides): # Check if recognition sequence contains only valid nucleotides
        return "Error: Recognition sequence contains invalid characters."

    positions = [] # List to store positions of cut sites
    for i in range(len(dna_sequence) - len(recognition_sequence) + 1): # Iterate through the DNA sequence
        if dna_sequence[i:i+len(recognition_sequence)] == recognition_sequence:
            positions.append(i)

    return [pos + 1 for pos in positions]  # Convert to 1-based biological positions


# Input usage
if __name__ == "__main__":
    dna = input("Enter the DNA sequence: ").strip()
    enzyme_site = input("Enter the recognition site sequence: ").strip()

    result = find_cut_sites(dna, enzyme_site)
    print("Cut positions:", result)

# Example usage
    print("\n--- Example Call ---")
    example_result = find_cut_sites("ATCGAATTCGGAATTC", "GAATTC")
    print("Example DNA: ATCGAATTCGGAATTC")
    print("Recognition site: GAATTC")
    print("Cut positions:", example_result)