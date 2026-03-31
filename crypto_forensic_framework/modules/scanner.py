import os

def scan_directory(path):
    file_list = []

    for root, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)
            file_list.append(full_path)

    return file_list