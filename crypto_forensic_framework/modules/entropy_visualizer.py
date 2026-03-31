import matplotlib.pyplot as plt
import os
from modules.entropy_detector import calculate_entropy

def visualize_entropy(files):

    file_names = []
    entropy_values = []

    for file in files:
        entropy = calculate_entropy(file)
        entropy_values.append(entropy)
        file_names.append(os.path.basename(file))

    plt.figure(figsize=(8,5))
    plt.bar(file_names, entropy_values)

    plt.title("Entropy Analysis of Evidence Files")
    plt.xlabel("Files")
    plt.ylabel("Entropy Value")

    plt.axhline(y=7.5, color='r', linestyle='--', label="Encryption Threshold")
    plt.legend()

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()