import os
from datetime import datetime

def analyze_metadata(file_path):

    stats = os.stat(file_path)

    metadata = {
        "file_name": os.path.basename(file_path),
        "size_bytes": stats.st_size,
        "created": datetime.fromtimestamp(stats.st_ctime),
        "modified": datetime.fromtimestamp(stats.st_mtime),
        "accessed": datetime.fromtimestamp(stats.st_atime)
    }

    return metadata