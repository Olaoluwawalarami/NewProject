from tkinter import *

class Table:
    def __init__(self,root):

        #code for creating table
        for i in range(total_rows):
            for j in range(total_columns):

                self.e = Entry(root, width=20, fg="blue", font=("Arial",16,"bold"))

                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])

# take data
lst = with sqlite3.connect("Project.db") as new:
        cursor = new.cursor()

    cursor.execute("SELECT * FROM columns")
    rows = cursor.fetchall()

    new.commit()

# find total number of rows and colums in list
total_rows = len(lst)
total_columns = len(lst[0])

# creat root window
root = Tk()
t = Table(root)
root.mainloop()





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