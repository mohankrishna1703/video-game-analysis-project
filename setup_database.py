import sqlite3

# Connect to SQLite DB (or create it)
conn = sqlite3.connect('video_games.db')
cursor = conn.cursor()

# Read and execute the SQL schema
with open('create_tables.sql', 'r') as f:
    sql_script = f.read()

cursor.executescript(sql_script)
conn.commit()
conn.close()

print("✅ SQLite database and tables created successfully.")