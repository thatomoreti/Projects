import sqlite3

def get_connection():
    return sqlite3.connect('task_manager.db')


#Admin function
def create_user(name,s_name,u_type):
    connection =get_connection()
    cursor = connection.cursor()
    
    user_insertion = '''INSERT INTO user (name, s_name, type)
    VALUES (?,?,?);'''

    cursor.execute(user_insertion,(name, s_name, u_type))
    connection.commit()
    # if u_type == 'Admin':
    #     admin_insertion = '''INSERT INTO admin (name, s_name)'''
    #     cursor.execute(admin_insertion,(name,s_name))

    #     connection.commit()
    #     connection.close()
    # elif u_type == 'Worker':
    #     worker_insertion = '''INSERT INTO worker (name, s_name)'''
    #     cursor.execute(worker_insertion,(name,s_name))

    #     connection.commit()
    #     connection.close()
    
def create_task(name,heading,description,status, type,creator_id,worker_id):
    connection = get_connection()
    cursor = connection.cursor()
    
    name_query = ('''SELECT * FROM user WHERE name = ? ;''')
    
    cursor.execute(name_query,(name,))
    name_r=cursor.fetchone()
    
    if name_r is None:
        print("You're not in the db")
        connection.close()
        
        
    else:
        if name_r[3] == 'Admin':
                task_insertion = '''INSERT INTO task (heading, description, status,type,creator_id,worker_id)
                                VALUES (?,?,?,?,?,?);'''

                cursor.execute(task_insertion,(heading, description, status,type,creator_id,worker_id))

                connection.commit()
                connection.close()
        else:
                print("Only Admins can create tasks")
                connection.close()
                
def delete_task(name,heading,worker_id):
    connection = get_connection()
    cursor = connection.cursor()
    
    name_query = ('''SELECT * FROM user WHERE name = ? ;''')
    
    cursor.execute(name_query,(name,))
    name_r=cursor.fetchone()
    
    if name_r is None:
        print("You're not in the db")
        connection.close()
        
        
    else:
        if name_r[3] == 'Admin':
            task_query = ('''SELECT * FROM task WHERE heading = ? AND  worker_id = ?;''')
            
            cursor.execute(task_query,(heading,worker_id))
            task_r=cursor.fetchone()
            
            if task_r is None:
                print("Task doesn't exist")
                connection.close()
                
            else:
                task_deletion = '''DELETE FROM task WHERE heading =? AND worker_id = ?;'''

                cursor.execute(task_deletion,(heading,worker_id))

                connection.commit()
                connection.close()
        else:
            print("Only Admins can delete Tasks")
            connection.close()
        
def edit_task(u_id,heading, description):
    connection = get_connection()
    cursor = connection.cursor()
    
    name_query = ('''SELECT * FROM user WHERE u_id = ? ;''')
    
    cursor.execute(name_query,(u_id,))
    name_r=cursor.fetchone()
    
    if name_r is None:
        print("You're not in the db")
        connection.close()
        
        
    else:
        if name_r[3] == 'Admin':
    
            heading_query = ('''SELECT * FROM task WHERE heading = ?;''')
            
            cursor.execute(heading_query,(heading,))
            task_r=cursor.fetchone()
            
            if task_r is None:
                print("Task doesn't exist")
                connection.close()
                
            else:
                task_update = '''UPDATE task set description = ? WHERE heading = ?;'''
                
                cursor.execute(task_update,(description,heading))

                connection.commit()
                connection.close()
        else:
            print("Only Admins can edit Tasks")
            connection.close()
            
def view_tasks():
    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM task")
    rows = cursor.fetchall()
    
    if rows:
        print("\n--- Tasks: ---")
        for row in rows:
            print(row)
        connection.close()
    else:
        print("\n--- There are no tasks to view ---")
        connection.close()
    return rows
            
#Worker Functions
def complete_task(name,worker_id):
    connection = get_connection()
    cursor = connection.cursor()
    
    name_query = ('''SELECT * FROM user WHERE name = ? ;''')
    
    cursor.execute(name_query,(name,))
    name_r=cursor.fetchone()
    
    if name_r is None:
        print("You're not in the db")
        connection.close()
           
    else:
        if name_r[3] == 'Worker':
                task_insertion = '''UPDATE task SET status = ? WHERE worker_id = ? ;'''

                cursor.execute(task_insertion,('Complete',worker_id))

                connection.commit()
                connection.close()
        else:
                print("Only Workers can complete tasks")
                connection.close()
