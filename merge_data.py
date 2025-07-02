import pandas as pd

# Load cleaned datasets
games = pd.read_csv('cleaned_games.csv')
sales = pd.read_csv('cleaned_vgsales.csv')

# Drop any unnamed columns
games = games.loc[:, ~games.columns.str.contains('^Unnamed')]
sales = sales.loc[:, ~sales.columns.str.contains('^Unnamed')]

# Merge on title and name
merged = pd.merge(games, sales, left_on='title', right_on='name', how='inner')

# Drop duplicate 'name' column
merged.drop(columns=['name'], inplace=True)

# Save the merged dataset
merged.to_csv('merged_games.csv', index=False)
print("✅ Merged dataset saved as 'merged_games.csv'")