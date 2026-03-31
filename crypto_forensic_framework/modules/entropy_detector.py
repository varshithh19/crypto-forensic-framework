import math

def calculate_entropy(file_path):

    with open(file_path, "rb") as f:
        data = f.read()

    if not data:
        return 0

    byte_counts = [0] * 256

    for byte in data:
        byte_counts[byte] += 1

    entropy = 0

    for count in byte_counts:
        if count == 0:
            continue

        probability = count / len(data)
        entropy -= probability * math.log2(probability)

    return entropy


def detect_encryption(file_path):

    entropy = calculate_entropy(file_path)

    if entropy > 7.5:
        return True
    else:
        return False