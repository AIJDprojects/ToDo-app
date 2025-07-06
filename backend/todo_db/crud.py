# Project     :   ToDo List
# Package     :   CRUD.py
# Description :   This package contains the CRUD operations 
#                 for the ToDo List application.
# Modification History:
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# *********************************************************


# Libraries
from datetime import datetime
from database import get_db_connection


# Project     :   ToDo List
# Method      :   Insert_task
# Description :   This method inserts a new task in the database.
# Modification History:
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# *********************************************************
def Insert_task(task: str, description: str = None) -> int: 

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        'INSERT INTO tasks (task, description) VALUES (?, ?)',
        (task, description)
    )

    conn.commit()
    task_id = cursor.lastrowid
    conn.close()

    return task_id


# Project     :   ToDo List
# Method      :   get_task
# Description :   This method retrieves a task by its ID from the database.
# Modification History:
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# *********************************************************
def get_task(task_id: int):
     
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    task = cursor.fetchone()

    conn.close()

    if task is None:
        return None 
    
    return task


# Project     :   ToDo List
# Method      :   get_all_tasks
# Description :   This method retrieves all tasks from the database.
# Modification History:
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# *********************************************************
def get_all_tasks():

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()

    conn.close()

    return tasks



# Project     :   ToDo List
# Method      :   update_task
# Description :   This method updates an existing task in the database 
#                 by a dinamic query.
# Modification History:
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# *********************************************************
def update_task(task_id: int, task_data: dict) -> bool:
    
    conn = get_db_connection()
    cursor = conn.cursor()

    updates = []
    params = []

    # Prepare the update query dynamically based on provided task_data
    for key, value in task_data.items():
        if value is not None:
            # Special handling for 'finished' key to set end_time
            if key == "finished" and value == 'Y':
                updates.append("end_time = ?")
                params.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            else:
                updates.append(f"{key} = ?")
                params.append(value)
                

    if not updates:
        conn.close()
        return False

    # append the task_id to the parameters for the WHERE clause
    params.append(task_id)      

    # Create the update query
    update_query = f"UPDATE tasks SET {', '.join(updates)} WHERE id = ?"

    # Execute the update query
    cursor.execute(update_query, params)

    conn.commit()
    conn.close()

    return True    


# Project     :   ToDo List
# Method      :   delete_task
# Description :   This method deletes a task from the database by its ID.
# Modification History:
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# *********************************************************
def delete_task(task_id: int) -> bool:

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id))
    conn.commit()

    rows_afected = cursor.rowcount
    conn.close()

    return rows_afected > 0





