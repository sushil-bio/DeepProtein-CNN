import pandas as pd
import random
import time

print("Forging 100,000 Protein Sequences... Your CPU is going to work hard.")
start_time = time.time()

amino_acids = list("ACDEFGHIKLMNPQRSTVWY")

# The Toxins (The "Bad Words" the AI must learn to read)
pathogenic_motifs = ["VWYFG", "CDEEF", "KKRRP", "MMIIL"]
healthy_motifs = ["AAAAA", "STTST", "GGGGG", "QQNND"]

data = []
total_sequences = 100000

for i in range(total_sequences):
    length = random.randint(100, 300) 
    sequence = "".join(random.choices(amino_acids, k=length))
    
    if i % 2 == 0:
        # Sick protein
        toxin = random.choice(pathogenic_motifs)
        insert = random.randint(0, length - len(toxin))
        sequence = sequence[:insert] + toxin + sequence[insert + len(toxin):]
        label = 1 # Pathogenic
    else:
        # Healthy protein
        structure = random.choice(healthy_motifs)
        insert = random.randint(0, length - len(structure))
        sequence = sequence[:insert] + structure + sequence[insert + len(structure):]
        label = 0 # Healthy
        
    data.append([sequence, label])

df = pd.DataFrame(data, columns=["Protein_Sequence", "Is_Pathogenic"])
df = df.sample(frac=1).reset_index(drop=True)
df.to_csv("deep_protein_dataset.csv", index=False)

print(f"Data Generation Complete! Created deep_protein_dataset.csv")
print(f"Time Taken: {time.time() - start_time:.2f} seconds")
