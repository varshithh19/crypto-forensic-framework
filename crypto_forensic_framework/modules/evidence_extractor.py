import shutil
import os

def extract_evidence(file_path, destination):

    if not os.path.exists(destination):
        os.makedirs(destination)

    shutil.copy2(file_path, destination)