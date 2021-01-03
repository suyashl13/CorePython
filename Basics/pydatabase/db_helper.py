import sqlite3

db = 'my_todo.db'
table_name = 'tasks'
connection = sqlite3.connect(db)
c = connection.cursor()

def create_table():
    sql = 'CREATE TABLE IF NOT EXISTS ' + table_name \
    + ' (ID INTEGER PRIMARY KEY AUTOINCREMENT, TaskName ' \
        'text)'

    c.execute(sql)  

def dataEntry(task):
    c.execute("INSERT INTO " + table_name + " (TaskName) VALUES (?)",[task])
    print("Task Added in database...")
    connection.commit()


def printData():
    sql = "SELECT * FROM " + table_name
    c.execute(sql)
    for row in c.fetchall():
        print(row[0], " => ", row[1])

def deleteTask(index):
    c.execute('DELETE FROM ' + table_name + " WHERE ID=?", (index, ))
    print("Task deleted sucessfully...")


def closeCursor():
    c.close()
    connection.close()
    