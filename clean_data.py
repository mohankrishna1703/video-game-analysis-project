import pandas as pd

# Load raw CSVs
games = pd.read_csv('games.csv')
sales = pd.read_csv('vgsales.csv')

# Drop rows with missing critical values
games_cleaned = games.dropna(subset=['Rating', 'Plays'])
sales_cleaned = sales.dropna(subset=['Global_Sales'])

# Remove duplicates
games_cleaned = games_cleaned.drop_duplicates()
sales_cleaned = sales_cleaned.drop_duplicates()

# Standardize genre and publisher
games_cleaned['Genres'] = games_cleaned['Genres'].str.lower().str.strip()
sales_cleaned['Genre'] = sales_cleaned['Genre'].str.lower().str.strip()
sales_cleaned['Publisher'] = sales_cleaned['Publisher'].str.title().str.strip()

# Rename columns to match SQL schema
games_cleaned.rename(columns={
    'Title': 'title',
    'Rating': 'rating',
    'Genres': 'genres',
    'Plays': 'plays',
    'Backlogs': 'backlogs',
    'Wishlist': 'wishlist',
    'Release Date': 'release_date',
    'Platform': 'platform',
    'Team': 'team'
}, inplace=True)

sales_cleaned.rename(columns={
    'Name': 'name',
    'Platform': 'platform',
    'Year': 'year',
    'Genre': 'genre',
    'Publisher': 'publisher',
    'NA_Sales': 'na_sales',
    'EU_Sales': 'eu_sales',
    'JP_Sales': 'jp_sales',
    'Other_Sales': 'other_sales',
    'Global_Sales': 'global_sales'
}, inplace=True)

# Save cleaned files without index
games_cleaned.to_csv('cleaned_games.csv', index=False)
sales_cleaned.to_csv('cleaned_vgsales.csv', index=False)

print("✅ Cleaned files saved: cleaned_games.csv, cleaned_vgsales.csv")