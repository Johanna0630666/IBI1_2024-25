import random

# 读取FASTA文件
def read_fasta(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        name = lines[0].strip()
        sequence = ''.join([line.strip() for line in lines[1:]])
        return name, sequence

# 读取BLOSUM62矩阵
def read_blosum62(file_path):
    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f if not line.startswith('#') and line.strip()]
        headers = lines[0].split()
        blosum = {}
        for line in lines[1:]:
            parts = line.split()
            row_aa = parts[0]
            scores = parts[1:]
            for i in range(len(headers)):
                blosum[(row_aa, headers[i])] = int(scores[i])
        return blosum

# 计算非间隙全局比对得分与identity百分比
def align_sequences(seq1, seq2, blosum):
    score = 0
    identical = 0
    aligned_pairs = []
    for a1, a2 in zip(seq1, seq2):
        score += blosum.get((a1, a2), -4)  # -4 是默认penalty值，如果配对不存在
        aligned_pairs.append((a1, a2))
        if a1 == a2:
            identical += 1
    identity_percent = (identical / len(seq1)) * 100
    return score, identity_percent, aligned_pairs

# 输出比对结果
def print_alignment_result(name1, seq1, name2, seq2, score, identity_percent):
    print(f"\n{name1}\n{seq1}")
    print(f"\n{name2}\n{seq2}")
    print(f"\nAlignment score: {score}")
    print(f"Percentage identity: {identity_percent:.2f}%")

# 主程序入口
def run_alignment():
    # 替换为你自己的文件路径
    seq_files = {
        'human': 'C:/Users/frank/Desktop/IBI1/IBI1_2024-25/Practical13/PO4179.fasta',
        'mouse': 'C:/Users/frank/Desktop/IBI1/IBI1_2024-25/Practical13/PO9671.fasta',
        'random': 'C:/Users/frank/Desktop/IBI1/IBI1_2024-25/Practical13/random.fasta'
    }
    blosum_file = 'C:/Users/frank/Desktop/IBI1/IBI1_2024-25/Practical13/blosum62.txt'

    blosum = read_blosum62(blosum_file)
    sequences = {name: read_fasta(path) for name, path in seq_files.items()}

    pairs = [('human', 'mouse'), ('human', 'random'), ('mouse', 'random')]
    for name1, name2 in pairs:
        title1, seq1 = sequences[name1]
        title2, seq2 = sequences[name2]
        score, identity, _ = align_sequences(seq1, seq2, blosum)
        print(f"\n--- Comparison: {name1.upper()} vs {name2.upper()} ---")
        print_alignment_result(title1, seq1, title2, seq2, score, identity)

if __name__ == "__main__":
    run_alignment()