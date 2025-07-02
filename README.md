# 🎮 Video Game Sales and Engagement Analysis

This project analyzes trends in video game performance using user engagement metrics (ratings, wishlists) and global sales across platforms and genres.

## 📦 Contents

- `games.csv`, `vgsales.csv` — Raw datasets
- `clean_data.py`, `merge_data.py` — Python scripts for data prep
- `create_tables.sql`, `setup_database.py` — SQLite schema & setup
- `insert_data.py` — Inserts cleaned data into SQLite
- `analyze_data.py` — Runs SQL queries to generate insights
- `video_games.db` — Final database
- `top_10_sales.csv`, `avg_rating_per_genre.csv`, etc. — CSV output
- `video_game_project_report.docx` — 📄 Final report
- `screenshots/` — Dashboard screenshots from Power BI (optional)

## 📊 Tools Used

- Python (pandas, sqlite3)
- SQLite
- Power BI
- Visual Studio Code

## 📈 Key Insights

- 🏆 Top Game by Sales: **Wii Sports**
- ⭐ Best-Rated Genres: **Role-Playing**, **Puzzle**
- 🎮 Top Platforms: **DS**, **PS2**, **Wii**
- 🗓️ Peak Release Year: 2008–2011

## ✅ How to Run

```bash
python clean_data.py
python merge_data.py
python setup_database.py
python insert_data.py
python analyze_data.py
