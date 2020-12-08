# https://news.codecademy.com/aggregating-pokemon-data-python-pandas/

# Import the Pandas library
import pandas as pd

# Upload data into Pandas DataFrame
df = pd.read_csv('pokemon.csv')

# Count the number of Pokemon 'Name' for each Pokemon 'Type' 
print('Number of Pokemon of each type')
print(df.groupby('Type').agg('count')['Name'])

# Calculate the median of each stat for each Pokemon
print('Median stats for each type')
print(df.groupby('Type').agg('median')[['Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']])

