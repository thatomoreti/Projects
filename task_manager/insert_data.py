import sqlite3

# Create/connect to the DB
conn = sqlite3.connect('task_manager.db')

cursor = conn.cursor()

user_insertion = '''INSERT INTO user (name, s_name, type)
VALUES (?,?,?);'''

cursor.execute(user_insertion,('Thabiso', 'Khumo', 'Admin'))

conn.commit()

worker_insertion = '''INSERT INTO user (name, s_name, type)
VALUES (?,?,?);'''

# try:
cursor.execute(worker_insertion,('David', 'Merlyn', 'Worker'))
conn.commit()
#     print("Gucci Mane inserted successfully!")
# except Exception as e:
#     print("Error inserting Gucci Mane:", e)

task_insertion = '''INSERT INTO task (heading, description, status,type,worker_name)
VALUES (?,?,?,?,?);'''

cursor.execute(task_insertion,('Customer Service', 'Help Mr Kuma fix her laptop','Incomplete','urgent','Gucci Mane'))

conn.commit()

conn.close()