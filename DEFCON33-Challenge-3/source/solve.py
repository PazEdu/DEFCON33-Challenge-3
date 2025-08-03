import csv
import re
from pathlib import Path

def extract_flag_from_csv(csv_file_path):
    """
    Parses the crash dump CSV file, reads sensor values row-wise,
    converts them to ASCII characters, and extracts the CTF flag.
    """
    ascii_stream = []

    with csv_file_path.open("r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                ascii_stream.extend([
                    int(row["thruster_cmd"]),
                    int(row["gyro_raw"]),
                    int(row["diag_code"])
                ])
            except ValueError:
                continue  # Skip rows with malformed data

    # Convert numeric values to ASCII
    decoded_text = ''.join(chr(val) for val in ascii_stream if 32 <= val <= 126)

    # Search for the flag in decoded string
    match = re.search(r"aeroCTF\{.*?\}", decoded_text)
    return match.group(0) if match else "Flag not found."

if __name__ == '__main__':
    # Get path to crash_dump.csv 
    csv_path = Path(__file__).resolve().parent / "crash_dump.csv"
    print(extract_flag_from_csv(csv_path))
