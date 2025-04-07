import csv
import os
import glob

def get_catalogue_ids():
    """
    Searches for a CSV file in the same directory 
    and returns a list of IDs found in the file.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    pattern = os.path.join(script_dir, 'search_opencanada_*.csv')
    matching_files = glob.glob(pattern)

    if not matching_files:
        print("No matching CSV file found.")
        return []

    csv_file_path = matching_files[0]

    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        id_list = [row['id'] for row in reader]

    return id_list

