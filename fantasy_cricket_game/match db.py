#Creates the match data database
import sqlite3
conn = sqlite3.connect("cricket.db")
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS match")

cursor.execute("""
CREATE TABLE match (
    player TEXT,
    runs INTEGER,
    wickets INTEGER,
    catches INTEGER
)
""")

match_data = [
    ("Virat Kohli", 75, 0, 0),
    ("Rohit Sharma", 40, 0, 1),
    ("Bhuvneshwar Kumar", 5, 3, 0),
    ("Jasprit Bumrah", 2, 2, 0),
    ("Ravindra Jadeja", 30, 2, 1),
    ("Hardik Pandya", 45, 1, 1),
    ("MS Dhoni", 60, 0, 2),
    ("Rishabh Pant", 50, 0, 1)
]

cursor.executemany("INSERT INTO match VALUES (?, ?, ?, ?)", match_data)

conn.commit()
conn.close()
print("Match database (match table) created.")
