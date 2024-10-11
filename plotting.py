import pandas as pd
import matplotlib.pyplot as plt
import time
import os

file_path = 'data/rick_n_morty.csv'
while not os.path.isfile(file_path):
    print(f"Waiting for {file_path} to be created...")
    time.sleep(5)

data = pd.read_csv('data/rick_n_morty.csv')

species_counts = data['species'].value_counts()


colors = ['blue' if i == 0 else 'grey' for i in range(len(species_counts))]
ax = species_counts.plot.bar(color=colors)

plt.title('Species Breakdown from Rick and Morty')
plt.xticks(rotation=45)

plt.savefig('data/plot.png', bbox_inches='tight')
