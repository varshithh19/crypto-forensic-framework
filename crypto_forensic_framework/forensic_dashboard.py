import streamlit as st
import os
import pandas as pd

from modules.scanner import scan_directory
from modules.entropy_detector import detect_encryption, calculate_entropy
from modules.hash_integrity import generate_sha256
from modules.timeline_analyzer import generate_timeline
from modules.metadata_analyzer import analyze_metadata

import matplotlib.pyplot as plt

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Crypto Forensic Dashboard",
    page_icon="🔐",
    layout="wide"
)

# ---------- CUSTOM DARK STYLE ----------
st.markdown("""
<style>
body {
    background-color: #0e1117;
}

.big-title {
    font-size:40px;
    font-weight:bold;
    color:#4db8ff;
}

.metric-card {
    background-color:#1c1f26;
    padding:15px;
    border-radius:10px;
}
</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown('<p class="big-title">🔐 Cryptography-Aware Digital Forensics Dashboard</p>', unsafe_allow_html=True)

st.write("Interactive forensic analysis platform for secure evidence investigation.")

# ---------- INPUT ----------
evidence_folder = st.text_input("📁 Evidence Folder Path", "evidence")

if st.button("🚀 Run Forensic Analysis"):

    files = scan_directory(evidence_folder)

    encrypted_files = []
    hashes = {}
    entropies = []
    names = []
    metadata_list = []

    for file in files:

        entropy = calculate_entropy(file)
        entropies.append(entropy)
        names.append(os.path.basename(file))

        if detect_encryption(file):
            encrypted_files.append(file)

        hashes[file] = generate_sha256(file)

        metadata_list.append(analyze_metadata(file))

    timeline = generate_timeline(files)

    # ---------- METRICS ----------
    col1, col2, col3 = st.columns(3)

    col1.metric("Total Files", len(files))
    col2.metric("Encrypted Files", len(encrypted_files))
    col3.metric("Normal Files", len(files) - len(encrypted_files))

    st.divider()

    # ---------- FILE LIST ----------
    st.subheader("📂 Files Detected")
    st.write(files)

    # ---------- ENTROPY GRAPH ----------
    st.subheader("📊 Entropy Analysis")

    fig, ax = plt.subplots()

    ax.bar(names, entropies)
    ax.axhline(y=7.5, color='red', linestyle='--', label="Encryption Threshold")

    ax.set_ylabel("Entropy Value")
    ax.set_xlabel("Files")
    ax.set_title("Entropy Analysis of Evidence")

    plt.xticks(rotation=30)

    ax.legend()

    st.pyplot(fig)

    # ---------- ENCRYPTED FILES ----------
    st.subheader("⚠️ Encrypted / Suspicious Files")
    st.write(encrypted_files)

    # ---------- HASH TABLE ----------
    st.subheader("🔑 SHA256 Hash Values")

    hash_df = pd.DataFrame(list(hashes.items()), columns=["File", "SHA256"])
    st.dataframe(hash_df)

    # ---------- METADATA ----------
    st.subheader("🧾 Metadata Analysis")

    meta_df = pd.DataFrame(metadata_list)
    st.dataframe(meta_df)

    # ---------- TIMELINE ----------
    st.subheader("⏱ Evidence Timeline")

    timeline_df = pd.DataFrame(timeline)
    st.dataframe(timeline_df)

    # ---------- DOWNLOAD REPORT ----------
    report_path = "output/reports/forensic_report.txt"

    if os.path.exists(report_path):
        with open(report_path, "r") as f:
            st.download_button(
                "⬇ Download Forensic Report",
                f,
                file_name="forensic_report.txt"
            )

    st.success("Forensic Analysis Completed Successfully ✔")