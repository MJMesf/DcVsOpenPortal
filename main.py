from colorama import Fore , Style , init

from Catalogue_Driver import fetch_catalogue
from catalogue_ids import get_catalogue_ids
from davids_code import get_davids_ids  # assumes file returns list of ids

init()

def main():
    # download current csv from open data portal https://search.open.canada.ca/opendata/  (Agriculture and Agri-Food Canada organization only)
    fetch_catalogue()

    # Get IDs from the downloaded CSV file.
    catalogue_ids = get_catalogue_ids()
    
    # Get another list of IDs from data catalogue.
    davids_ids = get_davids_ids()
    
    # Find the common IDs.
    duplicate_ids = list(set(catalogue_ids) & set(davids_ids))
    

    print(Fore.GREEN + "Number of IDs in common:", len(duplicate_ids) + Style.RESET_ALL)
    print("Duplicate IDs list:", duplicate_ids)

if __name__ == "__main__":
    main()
