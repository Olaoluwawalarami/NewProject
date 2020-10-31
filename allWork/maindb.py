import sqlite3
import datetime

with sqlite3.connect("Project.db") as db:
    cursor = db.cursor()

cursor.execute('''
                    CREATE TABLE IF NOT EXISTS columns(
                    Timestamp datetime default current_timestamp,
                    posted_strength INT NOT NULL,
                    on_parade INT NOT NULL,
                    on_duty INT NOT NULL,
                    off_duty INT NOT NULL,
                    sick INT NOT NULL,
                    ops INT NOT NULL,
                    course INT NOT NULL,
                    naicc INT NOT NULL,
                    leave INT NOT NULL,
                    hosp_admin INT NOT NULL);
                ''')

db.commit()

