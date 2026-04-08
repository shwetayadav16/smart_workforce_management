import sqlite3

class DatabaseManager:
    def __init__(self):
        self.conn = sqlite3.connect("database/workforce.db")
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees(
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            department TEXT,
            salary REAL
        )
        """)
        self.conn.commit()

    def insert_employee(self, emp):
        self.cursor.execute(
            "INSERT INTO employees VALUES (?, ?, ?, ?, ?)",
            emp.to_tuple()
        )
        self.conn.commit()
    def clear_table(self):
        self.cursor.execute("DELETE FROM employees")
        self.conn.commit()

    def fetch_all(self):
        self.cursor.execute("SELECT * FROM employees")
        return self.cursor.fetchall()
    