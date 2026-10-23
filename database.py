import sqlite3

DB_NAME = "registration.db"

def create_table():
    connection = sqlite3.connect(DB_NAME)
    try:
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS registrations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                role TEXT NOT NULL,
                aadhaar_card_no TEXT UNIQUE,
                full_name TEXT NOT NULL,
                gender TEXT,
                mobile_no TEXT NOT NULL,
                address TEXT,
                dob TEXT,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        """)

        connection.commit()
        print("Registration table created successfully!")

    finally:
        connection.close()


if __name__ == "__main__":
    create_table()