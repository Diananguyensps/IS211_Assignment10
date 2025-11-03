import sqlite3

DB_NAME = "music.db"  # Make sure both scripts use this same name

# Connect to the database
conn = sqlite3.connect(DB_NAME)
c = conn.cursor()

# Create person table
c.execute('''
CREATE TABLE IF NOT EXISTS person (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER
)
''')

# Create pet table
c.execute('''
CREATE TABLE IF NOT EXISTS pet (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    species TEXT NOT NULL,
    person_id INTEGER,
    FOREIGN KEY (person_id) REFERENCES person(id)
)
''')

# Clear tables to avoid duplicates
c.execute("DELETE FROM pet")
c.execute("DELETE FROM person")

# Sample data for persons
persons = [
    ("John", "Doe", 28),
    ("Jane", "Smith", 34),
    ("Alice", "Johnson", 22),
    ("Bob", "Lee", 40)
]

# Insert persons
c.executemany("INSERT INTO person (first_name, last_name, age) VALUES (?, ?, ?)", persons)

# Get the actual IDs assigned by SQLite
c.execute("SELECT id FROM person")
person_ids = [row[0] for row in c.fetchall()]

# Sample data for pets, using correct person IDs
pets = [
    ("Fluffy", "Cat", person_ids[0]),
    ("Rex", "Dog", person_ids[1]),
    ("Whiskers", "Cat", person_ids[2]),
    ("Spot", "Dog", person_ids[3])
]

# Insert pets
c.executemany("INSERT INTO pet (name, species, person_id) VALUES (?, ?, ?)", pets)

conn.commit()
conn.close()

print("Tables created and data loaded successfully!")
