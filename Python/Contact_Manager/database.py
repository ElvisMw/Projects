import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('contacts.db')
c = conn.cursor()

# Create table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                email TEXT NOT NULL
             )''')

# Commit changes and close connection
conn.commit()
conn.close()
