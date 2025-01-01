import sqlite3
class Database:
    def __init__(self, db_name):
        self.conn= sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        finance_query= """CREATE TABLE IF NOT EXISTS finance(
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         type TEXT NOT NULL,
         amount REAL NOT NULL,
         source TEXT NOT NULL,
         date TEXT NOT NULL
         )"""
        goals_query = """CREATE TABLE IF NOT EXISTS goals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        target REAL NOT NULL,
        saved REAL DEFAULT 0
        )"""
        self.conn.execute(finance_query)
        self.conn.execute(goals_query)
        self.conn.commit()

    def some_data(self):
        # data fallco
        query = "SELECT COUNT(*) FROM finance"
        cursor = self.conn.execute(query)
        count = cursor.fetchone()[0]
        if count == 0:
            sample_data = [
                ("Income", 3000.0, "Salary", "2024-01-01"),
                ("Expense", 500.0, "Groceries", "2024-01-03"),
                ("Expense", 200.0, "Utilities", "2024-01-05"),
                ("Income", 150.0, "Freelance", "2024-01-10"),
                ("Expense", 100.0, "Transport", "2024-01-15"),
            ]
            self.conn.executemany(
                "INSERT INTO finance (type, amount, source, date) VALUES (?, ?, ?, ?)",
                sample_data,
            )
            self.conn.commit()
    def add_entry(self, entry_type, amount, source, date):
        query="INSERT INTO finance (type, amount, source, date) VALUES (?,?,?,?)"
        self.conn.execute(query, (entry_type, amount, source,date))
        self.conn.commit()
    def get_all_entries(self):
        query=" SELECT * FROM finance"
        cursor= self.conn.execute(query)
        return cursor.fetchall()
    def add_goal(self, name, target):
        query= "INSERT INTO goals(name, target) VALUES (?,?)"
        self.conn.execute(query,(name, target))
        self.conn.commit()
    def update_goal(self, goal_id, amount):
        query= ("UPDATE goals SET saved= saved + ? WHERE id=?")
        self.conn.execute(query, (amount, goal_id))
        self.conn.commit()
    def get_goals(self):
        query= "SELECT * FROM goals"
        cursor= self.conn.execute(query)
        return cursor.fetchall()


