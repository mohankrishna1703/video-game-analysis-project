import sqlite3
import pandas as pd

# Connect to DB
conn = sqlite3.connect('video_games.db')

# Load CSVs
games = pd.read_csv('cleaned_games.csv')
sales = pd.read_csv('cleaned_vgsales.csv')
merged = pd.read_csv('merged_games.csv')

# Drop any index or unnamed columns
games = games.loc[:, ~games.columns.str.contains('^Unnamed')]
sales = sales.loc[:, ~sales.columns.str.contains('^Unnamed')]
merged = merged.loc[:, ~merged.columns.str.contains('^Unnamed')]

# Define allowed columns (exactly as in SQL tables)
games_columns = ['title', 'rating', 'genres', 'plays', 'backlogs', 'wishlist', 'release_date', 'platform', 'team']
sales_columns = ['name', 'platform', 'year', 'genre', 'publisher', 'na_sales', 'eu_sales', 'jp_sales', 'other_sales', 'global_sales']
merged_columns = ['title', 'rating', 'genres', 'plays', 'backlogs', 'wishlist', 'release_date', 'platform', 'team',
                  'year', 'genre', 'publisher', 'na_sales', 'eu_sales', 'jp_sales', 'other_sales', 'global_sales']

# Keep only the columns needed
games = games[[col for col in games_columns if col in games.columns]]
sales = sales[[col for col in sales_columns if col in sales.columns]]
merged = merged[[col for col in merged_columns if col in merged.columns]]

# Insert into DB
games.to_sql('games', conn, if_exists='append', index=False)
sales.to_sql('sales', conn, if_exists='append', index=False)
merged.to_sql('merged_games', conn, if_exists='append', index=False)

conn.close()
print("✅ Data successfully inserted into the database.")