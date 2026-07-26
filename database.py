import sqlite3

# Connect to the database
connection= sqlite3.connect("expense.db")

#Create a cursor
cursor=connection.cursor()

#Create the Expense table
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL,
    category TEXT,
    description TEXT,
    date TEXT
)
""")

# Save changes
connection.commit()

print("Database and table created successfully!")

# Close the connection
connection.close()

# Adding a helper function
def get_connection():
    return
sqlite3.connect("expense.db")