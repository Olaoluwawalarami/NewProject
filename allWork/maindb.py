import sqlite3

with sqlite3.connect("Project.db") as db:
    cursor = db.cursor()

cursor.execute('''
                    CREATE TABLE IF NOT EXISTS columns(
                    date CHAR(50),
                    posted_strength INT NOT NULL,
                    on_parade INT NOT NULL,
                    on_duty INT NOT NULL,
                    off_duty INT NOT NULL,
                    sick INT NOT NULL,
                    ops INT NOT NULL,
                    course INT NOT NULL,
                    naicc INT NOT NULL,
                    nafc INT NOT NULL,
                    leave INT NOT NULL,
                    hosp_admin INT NOT NULL);
                ''')

db.commit()

#db.commit
