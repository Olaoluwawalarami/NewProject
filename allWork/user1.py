import sqlite3

with sqlite3.connect("user1.db") as db:
    cursor = db.cursor()

cursor.execute('''
                    CREATE TABLE IF NOT EXISTS user1(
                    userID INT PRIMARY KEY,
                    username CHAR(50) NOT NULL,
                    password CHAR(50) NOT NULL);
                ''')

db.commit()

#db.commit
