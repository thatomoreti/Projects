import sqlite3

# Connect to the DB
conn = sqlite3.connect('task_manager.db')
cursor = conn.cursor()

def print_table(table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    
    if rows:
        print(f"\n--- {table_name.upper()} ---")
        for row in rows:
            print(row)
    else:
        print(f"\n--- {table_name.upper()} is empty ---")

# List of tables to check
tables = ['user', 'admin', 'worker', 'task']

for table in tables:
    print_table(table)

# Close connection
conn.close()
