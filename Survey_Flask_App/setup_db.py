import sqlite3

def setup_db():
    conn = sqlite3.connect('questions.db')  # Connects to the database
    cursor = conn.cursor()
    
    # Create the quiz table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS quiz (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL
        )
    ''')

    # Insert sample questions if needed
    cursor.execute("INSERT INTO quiz (question, answer) VALUES ('Translate: Hello', 'Hola')")
    cursor.execute("INSERT INTO quiz (question, answer) VALUES ('Translate: Goodbye', 'Adiós')")
    cursor.execute("INSERT INTO quiz (question, answer) VALUES ('Translate: Thank you', 'Gracias')")
    
    conn.commit()  # Save changes
    conn.close()   # Close the connection

setup_db()  # Run the setup
