from colorama import Fore , Style , init

from Catalogue_Driver import fetch_catalogue
from catalogue_ids import get_catalogue_ids
from davids_code import get_davids_ids  # assumes file returns list of ids

init()

def main():
    # download current csv from open data portal https://search.open.canada.ca/opendata/  (Agriculture and Agri-Food Canada organization only)
    print(Fore.BLUE + "Downloading Open Data Portal ID'S\n" + Style.RESET_ALL)
    fetch_catalogue()

    # get IDs from the downloaded CSV file
    catalogue_ids = get_catalogue_ids()
    
    # get another list of IDs from data catalogue
    davids_ids = get_davids_ids()
    
    # find common IDs
    duplicate_ids = list(set(catalogue_ids) & set(davids_ids))
    
    print("Duplicate IDs list:", duplicate_ids)
    print(Fore.GREEN + "\n\nAbove is list of Duplicate Id's\n\nNumber of IDs in common: " + str(len(duplicate_ids)) + Style.RESET_ALL)

if __name__ == "__main__":
    main()

