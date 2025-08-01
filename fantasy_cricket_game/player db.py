#Creates the player stats database 
import sqlite3
conn = sqlite3.connect("cricket.db")
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS stats")

cursor.execute("""
CREATE TABLE stats (
    player TEXT,
    matches INTEGER,
    runs INTEGER,
    "100s" INTEGER,
    "50s" INTEGER,
    value INTEGER,
    ctg TEXT
)
""")
players = [
    ("Virat Kohli", 250, 12000, 43, 62, 120, "BAT"),
    ("Rohit Sharma", 230, 9000, 29, 44, 115, "BAT"),
    ("Bhuvneshwar Kumar", 180, 400, 0, 0, 95, "BOW"),
    ("Jasprit Bumrah", 140, 150, 0, 0, 105, "BOW"),
    ("Ravindra Jadeja", 200, 2500, 1, 13, 110, "AR"),
    ("Hardik Pandya", 100, 1800, 0, 5, 100, "AR"),
    ("MS Dhoni", 350, 10500, 10, 65, 125, "WK"),
    ("Rishabh Pant", 60, 1800, 2, 10, 90, "WK")
]
cursor.executemany("INSERT INTO stats VALUES (?, ?, ?, ?, ?, ?, ?)", players)

conn.commit()
conn.close()
print("Player database created with stats table.")
