import sqlite3

# Create/connect to the DB
conn = sqlite3.connect('task_manager.db')

cursor = conn.cursor()

task_tbl= '''
CREATE TABLE IF NOT EXISTS task (
    task_id INTEGER PRIMARY KEY AUTOINCREMENT,
    heading VARCHAR(200) NOT NULL,
    description VARCHAR(200),
    status VARCHAR DEFAULT 'Incomplete' CHECK(status IN('Incomplete', 'In progress', 'Complete')),
    type VARCHAR(100) NOT NULL,
    worker_name VARCHAR(100)
)
'''
cursor.execute(task_tbl)
user_tbl= '''
CREATE TABLE IF NOT EXISTS user (
    u_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(200) NOT NULL,
    s_name VARCHAR(200) NOT NULL,
    type VARCHAR CHECK(type IN('Admin','Worker'))
)
'''
cursor.execute(user_tbl)
admin_tbl= '''
CREATE TABLE IF NOT EXISTS admin (
    u_id INTEGER PRIMARY KEY ,
    FOREIGN KEY(u_id) REFERENCES user(u_id)
)
'''
cursor.execute(admin_tbl)
worker_tbl= '''
CREATE TABLE IF NOT EXISTS worker (
    u_id INTEGER PRIMARY KEY ,
    FOREIGN KEY(u_id) REFERENCES user(u_id)
)
'''
cursor.execute(worker_tbl)

# Close the connection (we’ll add tables later)
conn.close()
