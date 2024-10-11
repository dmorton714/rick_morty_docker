import requests
import pandas as pd
import os

csv_file_path = "data/rick_n_morty.csv"

if os.path.exists(csv_file_path):
    print(f"CSV file '{csv_file_path}' found. Loading data from CSV.")
    data = pd.read_csv(csv_file_path)
else:
    print(f"CSV file '{csv_file_path}' not found. Fetching data from API.")
    
    url = 'https://rickandmortyapi.com/api/character'
    results = []
    page = 1

    while True:
        response = requests.get(f'{url}?page={page}')
        data = response.json()

        if 'results' in data and len(data['results']) > 0:
            results.extend(data['results'])
            page += 1
        else:
            break

    if not os.path.exists("data"):
        os.makedirs("data")

    data = pd.DataFrame(results)
    data.to_csv(csv_file_path, index=False)
    print(f"Data fetched and saved to '{csv_file_path}'.")
