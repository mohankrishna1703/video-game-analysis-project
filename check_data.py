import sqlite3

conn = sqlite3.connect('video_games.db')
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM games")
print("🎮 Games table rows:", cursor.fetchone()[0])

cursor.execute("SELECT COUNT(*) FROM sales")
print("💰 Sales table rows:", cursor.fetchone()[0])

cursor.execute("SELECT COUNT(*) FROM merged_games")
print("🧩 Merged table rows:", cursor.fetchone()[0])

conn.close()