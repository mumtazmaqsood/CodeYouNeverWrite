import os
import hashlib
import csv
from pathlib import Path
from collections import defaultdict
from datetime import datetime

# =====================================================
# CHANGE THIS TO YOUR BACKUP FOLDER
# =====================================================

ROOT = r"C:\Users\HP\Documents\Downloads"

# =====================================================

LARGE_FILE_MB = 100
OLD_DAYS = 365

duplicate_hashes = defaultdict(list)
same_names = defaultdict(list)
type_count = defaultdict(int)

large_files = []
old_files = []

total_files = 0
total_size = 0


def sha256(filename):
    h = hashlib.sha256()
    with open(filename, "rb") as f:
        while True:
            chunk = f.read(1024 * 1024)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


print("Scanning...")

for root, dirs, files in os.walk(ROOT):

    for file in files:

        full = os.path.join(root, file)

        try:

            size = os.path.getsize(full)

            total_files += 1
            total_size += size

            ext = Path(file).suffix.lower()

            if ext == "":
                ext = "(no extension)"

            type_count[ext] += 1

            same_names[file.lower()].append(full)

            if size > LARGE_FILE_MB * 1024 * 1024:
                large_files.append((full, size))

            modified = datetime.fromtimestamp(os.path.getmtime(full))

            age = (datetime.now() - modified).days

            if age > OLD_DAYS:
                old_files.append((full, age))

            try:
                h = sha256(full)
                duplicate_hashes[h].append(full)
            except Exception:
                pass

        except Exception:
            pass

print("Writing reports...")

# -----------------------
# Summary
# -----------------------

with open("summary.txt", "w", encoding="utf8") as f:

    f.write(f"Total files : {total_files}\n")
    f.write(f"Total size  : {total_size/1024/1024:.2f} MB\n\n")

    f.write("File Types\n")
    f.write("--------------------------\n")

    for ext, count in sorted(type_count.items()):
        f.write(f"{ext:15} {count}\n")

# -----------------------
# Duplicate Files
# -----------------------

with open("duplicates.csv", "w", newline="", encoding="utf8") as f:

    writer = csv.writer(f)

    writer.writerow(["Hash", "File"])

    for h, files in duplicate_hashes.items():

        if len(files) > 1:

            for file in files:

                writer.writerow([h, file])

# -----------------------
# Same Names
# -----------------------

with open("same_names.csv", "w", newline="", encoding="utf8") as f:

    writer = csv.writer(f)

    writer.writerow(["Filename", "Path"])

    for name, files in same_names.items():

        if len(files) > 1:

            for file in files:

                writer.writerow([name, file])

# -----------------------
# Large Files
# -----------------------

with open("large_files.csv", "w", newline="", encoding="utf8") as f:

    writer = csv.writer(f)

    writer.writerow(["File", "Size (MB)"])

    for file, size in sorted(large_files, key=lambda x: x[1], reverse=True):

        writer.writerow([file, round(size / 1024 / 1024, 2)])

# -----------------------
# Old Files
# -----------------------

with open("old_files.csv", "w", newline="", encoding="utf8") as f:

    writer = csv.writer(f)

    writer.writerow(["File", "Age (Days)"])

    for file, age in sorted(old_files, key=lambda x: x[1], reverse=True):

        writer.writerow([file, age])

print()
print("DONE")
print()
print("Generated:")
print(" summary.txt")
print(" duplicates.csv")
print(" same_names.csv")
print(" large_files.csv")
print(" old_files.csv")
print()
print("No files were modified.")