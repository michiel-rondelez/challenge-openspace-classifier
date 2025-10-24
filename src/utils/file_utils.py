import os
import csv
from typing import List

def get_names_from_csv(file_name: str) -> List[str]:
    """
    Reads a CSV file containing one name per row and returns a list of names.

    Args:
        file_name (str): Name of the CSV file in the '../data/' folder.

    Returns:
        List[str]: List of names from the CSV.
    """ 
    folder_path = "../data"
    file_path = os.path.join(folder_path, file_name)

    if not os.path.isdir(folder_path):
        print(f"Folder does not exist: {folder_path}")
        return []

    if not os.path.isfile(file_path):
        print(f"File not found: '{file_name}'")
        return []

    names = []
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row:
                    names.append(row[0].strip())
        return names
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return []
