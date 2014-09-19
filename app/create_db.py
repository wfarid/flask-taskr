'''
 Creating the 'flasktaskr.db' and creating the table 'tasks'
'''
import sqlite3
from config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:

    c = connection.cursor()
    c.execute('''CREATE TABLE tasks (task_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                     name TEXT NOT NULL, 
                                     due_date TEXT NOT NULL,
                                     priority INTEGER NOT NULL, 
                                     status INTEGER NOT NULL)''')

    c.execute('INSERT INTO tasks (name,due_date,priority,status) VALUES("Finish this tutorial","01/04/2015",10,1)')
    c.execute('INSERT INTO tasks (name,due_date,priority,status) VALUES("Finish 2nd course in Real-Python","01/11/2014",7,1)')