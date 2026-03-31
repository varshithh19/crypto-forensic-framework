import os
from datetime import datetime

def generate_timeline(files):

    timeline = []

    for file in files:

        stats = os.stat(file)

        created = datetime.fromtimestamp(stats.st_ctime)
        modified = datetime.fromtimestamp(stats.st_mtime)
        accessed = datetime.fromtimestamp(stats.st_atime)

        timeline.append({
            "file": os.path.basename(file),
            "created": created,
            "modified": modified,
            "accessed": accessed
        })

    return timeline


def print_timeline(timeline):

    print("\n----- Evidence Timeline -----")

    for entry in timeline:

        print(f"\nFile: {entry['file']}")
        print(f"Created: {entry['created']}")
        print(f"Modified: {entry['modified']}")
        print(f"Accessed: {entry['accessed']}")