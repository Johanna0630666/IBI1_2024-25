from Bio import SeqIO
import blosum as bl # Importing the BLOSUM module

matrix = bl.BLOSUM(62) # Load the BLOSUM62 matrix

def load_fasta_sequence(filepath): # Function to load a single sequence from a FASTA file
    return str(next(SeqIO.parse(filepath, "fasta")).seq)

def compare_sequences(seq1, seq2): # Function to compare two sequences using the BLOSUM62 matrix
    if len(seq1) != len(seq2): # Check if sequences are of equal length
        raise ValueError("Sequences must be of equal length for comparison.") # Raise an error if lengths differ
    
    score = 0   # Initialize score to 0
    identical_count = 0  # Initialize count of identical amino acids

    for i in range(len(seq1)): 
        aa1 = seq1[i]
        aa2 = seq2[i]
        score += matrix[aa1][aa2] # Get the score from the BLOSUM62 matrix for the pair of amino acids
        if aa1 == aa2:
            identical_count += 1 # Count identical amino acids

    identity_percent = (identical_count / len(seq1)) * 100
    return score, identity_percent # Return the alignment score and identity percentage

# Load sequences
human_seq = load_fasta_sequence("C:/Users/frank/Desktop/IBI1/IBI1_2024-25/Practical13/human.fasta")
mouse_seq = load_fasta_sequence("C:/Users/frank/Desktop/IBI1/IBI1_2024-25/Practical13/mouse.fasta")
random_seq = load_fasta_sequence("C:/Users/frank/Desktop/IBI1/IBI1_2024-25/Practical13/random.fasta")

# Pairwise comparisons
score_hm, id_hm = compare_sequences(human_seq, mouse_seq)
score_hr, id_hr = compare_sequences(human_seq, random_seq)
score_mr, id_mr = compare_sequences(mouse_seq, random_seq)

# Output
print("Alignment scores and identities:")
print(f"- Human vs Mouse:   Score = {score_hm},  Identity = {id_hm:.2f}%")
print(f"- Human vs Random:  Score = {score_hr},  Identity = {id_hr:.2f}%")
print(f"- Mouse vs Random:  Score = {score_mr},  Identity = {id_mr:.2f}%")