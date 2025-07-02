# analyze_data.py
import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('video_games.db')
cursor = conn.cursor()

print("--- Running SQL Queries for Analysis ---")

# --- Query 1: Top 10 Games by Global Sales ---
print("\n1. Top 10 Games by Global Sales:")
query_top_sales = """
SELECT title, global_sales
FROM merged_games
ORDER BY global_sales DESC
LIMIT 10;
"""
cursor.execute(query_top_sales)
top_sales_games = cursor.fetchall()
for rank, (title, sales) in enumerate(top_sales_games):
    print(f"{rank+1}. {title}: {sales:.2f}M")

# --- Query 2: Average Rating per Genre ---
print("\n2. Average Rating per Genre:")
query_avg_rating_genre = """
SELECT genre, AVG(rating) AS avg_rating
FROM merged_games
WHERE genre IS NOT NULL AND rating IS NOT NULL
GROUP BY genre
ORDER BY avg_rating DESC
LIMIT 10;
"""
cursor.execute(query_avg_rating_genre)
avg_rating_genre = cursor.fetchall()
for genre, avg_rating in avg_rating_genre:
    print(f"   {genre}: {avg_rating:.2f}")

# --- Query 3: Total Global Sales by Platform ---
print("\n3. Total Global Sales by Platform:")
query_sales_by_platform = """
SELECT platform, SUM(global_sales) AS total_sales
FROM merged_games
WHERE platform IS NOT NULL
GROUP BY platform
ORDER BY total_sales DESC
LIMIT 10;
"""
cursor.execute(query_sales_by_platform)
sales_by_platform = cursor.fetchall()
for platform, total_sales in sales_by_platform:
    print(f"   {platform}: {total_sales:.2f}M")

# --- Query 4: Number of Games Released Per Year ---
print("\n4. Number of Games Released Per Year (Top 10 years by game count):")
query_games_per_year = """
SELECT year, COUNT(DISTINCT title) AS game_count
FROM merged_games
WHERE year IS NOT NULL
GROUP BY year
ORDER BY game_count DESC
LIMIT 10;
"""
cursor.execute(query_games_per_year)
games_per_year = cursor.fetchall()
for year, count in games_per_year:
    print(f"   {int(year)}: {count} games") # Convert year to int for cleaner output

# Convert query results to DataFrames and save as CSV files
pd.DataFrame(top_sales_games, columns=["title", "global_sales"]).to_csv("top_10_sales.csv", index=False)
pd.DataFrame(avg_rating_genre, columns=["genre", "avg_rating"]).to_csv("avg_rating_per_genre.csv", index=False)
pd.DataFrame(sales_by_platform, columns=["platform", "total_sales"]).to_csv("sales_by_platform.csv", index=False)
pd.DataFrame(games_per_year, columns=["year", "game_count"]).to_csv("games_per_year.csv", index=False)

# Close the database connection
conn.close()
print("\n✅ CSV files saved in your project folder.")
print("\n--- Analysis Complete ---")