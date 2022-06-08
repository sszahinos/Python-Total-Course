import os
import re
from pathlib import Path

MAIN_PATH = Path(".\\Mi_Gran_Directorio")
PATTERN = r"N\D{3}-\d{5}"  # example: Nryu-12365


def start():
    serial_nums = find_serial_nums(MAIN_PATH, PATTERN)
    print_serial_nums(serial_nums)


def find_pattern(file_path, pattern: str) -> re.Match:
    opened_file = open(file_path, "r")
    text = opened_file.read()
    code = re.search(pattern, text)
    opened_file.close()
    return code


def find_serial_nums(path: Path, pattern: str) -> dict:
    serial_nums = dict()
    for folder, subfolder, files in os.walk(path):
        for file in files:
            code = find_pattern(Path(folder, file), pattern)
            if code is not None:
                serial_nums[file] = code.group()
    return serial_nums


def print_serial_nums(serials: dict):
    print("""FILE\tSERIAL NUMBER\n-------\t-------""")
    for item in serials:
        print(f"{item}\t{serials[item]}")


start()
