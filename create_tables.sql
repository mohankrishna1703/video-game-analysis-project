-- Table 1: Games metadata
CREATE TABLE IF NOT EXISTS games (
    title TEXT,
    rating REAL,
    genres TEXT,
    plays INTEGER,
    backlogs INTEGER,
    wishlist INTEGER,
    release_date TEXT,
    platform TEXT,
    team TEXT
);

-- Table 2: Sales info
CREATE TABLE IF NOT EXISTS sales (
    name TEXT,
    platform TEXT,
    year INTEGER,
    genre TEXT,
    publisher TEXT,
    na_sales REAL,
    eu_sales REAL,
    jp_sales REAL,
    other_sales REAL,
    global_sales REAL
);

-- Table 3: Merged Dataset
CREATE TABLE IF NOT EXISTS merged_games (
    title TEXT,
    rating REAL,
    genres TEXT,
    plays INTEGER,
    backlogs INTEGER,
    wishlist INTEGER,
    release_date TEXT,
    platform TEXT,
    team TEXT,
    year INTEGER,
    genre TEXT,
    publisher TEXT,
    na_sales REAL,
    eu_sales REAL,
    jp_sales REAL,
    other_sales REAL,
    global_sales REAL
);