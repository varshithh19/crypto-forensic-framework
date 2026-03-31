from modules.scanner import scan_directory
from modules.entropy_detector import detect_encryption
from modules.entropy_visualizer import visualize_entropy
from modules.hash_integrity import generate_sha256
from modules.metadata_analyzer import analyze_metadata
from modules.evidence_extractor import extract_evidence
from modules.logger_module import log_event
from modules.timeline_analyzer import generate_timeline, print_timeline
from modules.report_generator import generate_report

import os

evidence_path = "evidence"
destination = "output/extracted_evidence"

files = scan_directory(evidence_path)

visualize_entropy(files)

timeline = generate_timeline(files)
print_timeline(timeline)

encrypted_files = []
hashes = {}
metadata_list = []

log_event("Scanning started")

for file in files:

    if detect_encryption(file):
        encrypted_files.append(file)

    hash_value = generate_sha256(file)

    hashes[file] = hash_value

    metadata = analyze_metadata(file)

    metadata_list.append(metadata)

    extract_evidence(file, destination)

log_event("Evidence extraction completed")

generate_report(files, encrypted_files, hashes, metadata_list)

log_event("Report generated")

print("\nForensic analysis complete.")