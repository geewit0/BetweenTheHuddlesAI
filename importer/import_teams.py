import sqlite3

DB = "../database/bth.db"

teams = [
    ("Arizona Cardinals", "Arizona", "ARI", "NFC", "West"),
    ("Atlanta Falcons", "Atlanta", "ATL", "NFC", "South"),
    ("Baltimore Ravens", "Baltimore", "BAL", "AFC", "North"),
    ("Buffalo Bills", "Buffalo", "BUF", "AFC", "East"),
    ("Carolina Panthers", "Carolina", "CAR", "NFC", "South"),
    ("Chicago Bears", "Chicago", "CHI", "NFC", "North"),
    ("Cincinnati Bengals", "Cincinnati", "CIN", "AFC", "North"),
    ("Cleveland Browns", "Cleveland", "CLE", "AFC", "North"),
    ("Dallas Cowboys", "Dallas", "DAL", "NFC", "East"),
    ("Denver Broncos", "Denver", "DEN", "AFC", "West"),
    ("Detroit Lions", "Detroit", "DET", "NFC", "North"),
    ("Green Bay Packers", "Green Bay", "GB", "NFC", "North"),
    ("Houston Texans", "Houston", "HOU", "AFC", "South"),
    ("Indianapolis Colts", "Indianapolis", "IND", "AFC", "South"),
    ("Jacksonville Jaguars", "Jacksonville", "JAX", "AFC", "South"),
    ("Kansas City Chiefs", "Kansas City", "KC", "AFC", "West"),
    ("Las Vegas Raiders", "Las Vegas", "LV", "AFC", "West"),
    ("Los Angeles Chargers", "Los Angeles", "LAC", "AFC", "West"),
    ("Los Angeles Rams", "Los Angeles", "LAR", "NFC", "West"),
    ("Miami Dolphins", "Miami", "MIA", "AFC", "East"),
    ("Minnesota Vikings", "Minnesota", "MIN", "NFC", "North"),
    ("New England Patriots", "New England", "NE", "AFC", "East"),
    ("New Orleans Saints", "New Orleans", "NO", "NFC", "South"),
    ("New York Giants", "New York", "NYG", "NFC", "East"),
    ("New York Jets", "New York", "NYJ", "AFC", "East"),
    ("Philadelphia Eagles", "Philadelphia", "PHI", "NFC", "East"),
    ("Pittsburgh Steelers", "Pittsburgh", "PIT", "AFC", "North"),
    ("San Francisco 49ers", "San Francisco", "SF", "NFC", "West"),
    ("Seattle Seahawks", "Seattle", "SEA", "NFC", "West"),
    ("Tampa Bay Buccaneers", "Tampa Bay", "TB", "NFC", "South"),
    ("Tennessee Titans", "Tennessee", "TEN", "AFC", "South"),
    ("Washington Commanders", "Washington", "WAS", "NFC", "East"),
]

conn = sqlite3.connect(DB)
cur = conn.cursor()

for team in teams:
    cur.execute(
        """
        INSERT OR IGNORE INTO teams
        (name, city, abbreviation, conference, division)
        VALUES (?, ?, ?, ?, ?)
        """,
        team,
    )

conn.commit()
conn.close()

print("32 NFL teams imported successfully!")
