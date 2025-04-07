import csv

# Using a raw string literal to avoid escape sequence issues
csv_file_path = r'C:\Users\mesfinmj\Downloads\search_opencanada_0bd68f5de9a6e864c7b93261c4aa15006cbb05f7_en.csv'

with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    id_list = [row['id'] for row in reader]

print("ID values:", id_list)
print("Number of IDs:", len(id_list))
