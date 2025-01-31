We explored three approaches to extract logs from a 1 TB file:

Linear Search: Read the entire file line by line. Simple but slow for large files.

Binary Search with Indexing: Build an index for fast lookups. Fast for queries but requires heavy preprocessing.

Approximate Seek with Linear Scan: Estimate the log position based on date distribution and scan from there. Balanced and efficient.

Final Solution Summary
We chose Approximate Seek with Linear Scan because:

It’s fast and avoids reading the entire file.

No preprocessing is needed.

It works well for evenly distributed logs and large files.

Steps to Run
Install Python (if not already installed).

Clone the repo and navigate to the src/ folder.

Run the script with the date you want:

python extract_logs.py 2024-12-01
Check the output: Logs for the date will be saved in output/output_YYYY-MM-DD.txt.
