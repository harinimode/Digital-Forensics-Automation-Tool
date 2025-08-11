🔍 Digital Forensics Automation Tool
A Python-based command-line digital forensics toolkit designed to automate essential investigation tasks like disk imaging, file hashing, integrity checks, metadata extraction, and log analysis. Ideal for incident response, evidence validation, and forensic analysis.

📌 Features
🖴 Disk Imaging – Create bit-by-bit copies of drives using dd.

🔑 Hash Generation – Supports MD5, SHA1, SHA256, SHA512, and BLAKE2b.

📂 Integrity Verification – Compare two files’ hashes to detect tampering.

📊 Metadata Extraction – Retrieve file name, size, creation, and modification timestamps.

📜 Log Analysis – Detect ERROR and WARNING messages from logs.

📂 File Structure
bash
Copy code
Digital-Forensics-Automation-Tool/
│
├── forensic.py                 # Main forensic tool script
├── README.md                   # Project documentation
├── sample.log                   # Example log file for testing
└── requirements.txt            # Optional dependencies file
⚙️ Installation
bash
Copy code
# Clone the repository
git clone https://github.com/harinimode/Digital-Forensics-Automation-Tool.git
cd Digital-Forensics-Automation-Tool

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
▶️ Usage
Run the tool using Python with the following commands:

1. Create a Disk Image
sudo python forensic.py --image /dev/sda /path/to/output.img
2. Generate a File Hash
python forensic.py --hash file.txt sha256
3. Compare Two Files
python forensic.py --compare file1.txt file2.txt sha256
4. Extract Metadata
python forensic.py --meta file.txt
5. Analyze Log Files
python forensic.py --log system.log

📜 Legal Disclaimer
This tool is intended only for ethical and lawful purposes. The author is not responsible for any misuse. Always have proper authorization before conducting forensic activities.

🚀 Future Improvements
Add GUI/Web Interface for ease of use

Support network forensics

Include report generation in PDF/HTML format

