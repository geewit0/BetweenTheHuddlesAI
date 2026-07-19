CREATE TABLE teams (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    city TEXT,
    abbreviation TEXT UNIQUE,
    conference TEXT,
    division TEXT
);

CREATE TABLE players (
    id INTEGER PRIMARY KEY,
    team_id INTEGER,
    name TEXT NOT NULL,
    position TEXT,
    jersey_number INTEGER
);

CREATE TABLE games (
    id INTEGER PRIMARY KEY,
    week INTEGER,
    game_date TEXT,
    home_team_id INTEGER,
    away_team_id INTEGER,
    home_score INTEGER,
    away_score INTEGER,
    status TEXT
);

CREATE TABLE news (
    id INTEGER PRIMARY KEY,
    title TEXT,
    summary TEXT,
    source TEXT,
    url TEXT,
    published_at TEXT
);

CREATE TABLE injuries (
    id INTEGER PRIMARY KEY,
    player_id INTEGER,
    status TEXT,
    injury TEXT,
    updated_at TEXT
);
