import os
import hashlib
import subprocess
import argparse
from datetime import datetime
from pathlib import Path

def create_disk_image(source, destination):
    """Creates a forensic disk image using dd."""
    try:
        print(f"Creating disk image from {source} to {destination}...")
        subprocess.run(["sudo", "dd", f"if={source}", f"of={destination}", "bs=4M", "status=progress"], check=True)
        print("Disk image created successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error creating disk image: {e}")


#supports md5, sha1, sha256, sha512, and blake2b
def generate_hash(file_path, algorithm='sha256'):
    """Generates a hash of a file using the specified algorithm."""
    try:
        hash_func = getattr(hashlib, algorithm)()
    except AttributeError:
        print(f"Unsupported hash algorithm: {algorithm}")
        return None
    
    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            hash_func.update(chunk)
    return hash_func.hexdigest()

def compare_files(file1, file2, algorithm='sha256'):
    """Compares the hash values of two files to check integrity."""
    hash1 = generate_hash(file1, algorithm)
    hash2 = generate_hash(file2, algorithm)
    
    if hash1 and hash2:
        print(f"{file1} ({algorithm}): {hash1}")
        print(f"{file2} ({algorithm}): {hash2}")
        if hash1 == hash2:
            print("✅ Files are identical.")
        else:
            print("⚠️ Files have been tampered with!")

def extract_metadata(file_path):
    """Extracts metadata from a given file."""
    file = Path(file_path)
    if not file.exists():
        print("File does not exist!")
        return
    
    metadata = {
        "File Name": file.name,
        "Size (bytes)": file.stat().st_size,
        "Created": datetime.fromtimestamp(file.stat().st_ctime),
        "Modified": datetime.fromtimestamp(file.stat().st_mtime),
    }
    for key, value in metadata.items():
        print(f"{key}: {value}")

def analyze_log(file_path):
    """Basic log analysis: Extracts error and warning messages."""
    with open(file_path, "r") as log:
        for line in log:
            if "ERROR" in line or "WARNING" in line:
                print(line.strip())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Digital Forensic Tool")
    parser.add_argument("--image", nargs=2, metavar=("SOURCE", "DEST"), help="Create disk image")
    parser.add_argument("--hash", nargs=2, metavar=("FILE", "ALGO"), help="Generate file hash (md5, sha1, sha256, sha512, blake2b)")
    parser.add_argument("--compare", nargs=3, metavar=("FILE1", "FILE2", "ALGO"), help="Compare hash values of two files")
    parser.add_argument("--meta", metavar="FILE", help="Extract file metadata")
    parser.add_argument("--log", metavar="FILE", help="Analyze log file for errors/warnings")
    
    args = parser.parse_args()
    
    if args.image:
        create_disk_image(args.image[0], args.image[1])
    elif args.hash:
        print(f"Hash ({args.hash[1]}):", generate_hash(args.hash[0], args.hash[1]))
    elif args.compare:
        compare_files(args.compare[0], args.compare[1], args.compare[2])
    elif args.meta:
        extract_metadata(args.meta)
    elif args.log:
        analyze_log(args.log)


'''

'''