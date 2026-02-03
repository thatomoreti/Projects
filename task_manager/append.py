import sqlite3

def getConnection():
    return sqlite3.connect('task_manager.db')
    
connection = getConnection()

cursor = connection.cursor()

cursor.execute("DROP TABLE task;")

connection.commit()

cursor.execute("""
CREATE TABLE task (
    task_id INTEGER PRIMARY KEY AUTOINCREMENT,
    heading TEXT NOT NULL,
    description TEXT,
    status TEXT DEFAULT 'Incomplete'
        CHECK(status IN ('Incomplete','In progress','Complete')),
    type TEXT NOT NULL,
    creator_id INTEGER NOT NULL,
    worker_id INTEGER,
    FOREIGN KEY (creator_id) REFERENCES user(u_id),
    FOREIGN KEY (worker_id) REFERENCES user(u_id)
);
""")

connection.commit()
