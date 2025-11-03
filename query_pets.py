import sqlite3

DB_NAME = "music.db"

conn = sqlite3.connect(DB_NAME)
c = conn.cursor()

# List all persons
print("Persons:")
c.execute("SELECT * FROM person")
for row in c.fetchall():
    print(row)

# List all pets with their owners
print("\nPets with owners:")
c.execute('''
SELECT pet.name, pet.species, person.first_name, person.last_name
FROM pet
JOIN person ON pet.person_id = person.id
''')
for row in c.fetchall():
    print(row)

conn.close()

