def generate_report(scanned_files, encrypted_files, hashes, metadata_list):

    report_path = "output/reports/forensic_report.txt"

    with open(report_path, "w") as report:

        report.write("Cryptography-Aware Digital Forensics Report\n")
        report.write("="*50 + "\n\n")

        report.write(f"Total Files Scanned: {len(scanned_files)}\n")
        report.write(f"Encrypted Files Detected: {len(encrypted_files)}\n\n")

        report.write("Encrypted Files:\n")

        for f in encrypted_files:
            report.write(f"{f}\n")

        report.write("\nSHA256 Hash Values:\n")

        for file, h in hashes.items():
            report.write(f"{file} : {h}\n")

        report.write("\nFile Metadata Analysis:\n")

        for meta in metadata_list:

            report.write(f"\nFile: {meta['file_name']}\n")
            report.write(f"Size: {meta['size_bytes']} bytes\n")
            report.write(f"Created: {meta['created']}\n")
            report.write(f"Modified: {meta['modified']}\n")
            report.write(f"Accessed: {meta['accessed']}\n")