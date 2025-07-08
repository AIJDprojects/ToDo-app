# Project     :   ToDo List
# Package     :   CRUD.py
# Description :   This package contains the CRUD operations 
#                 for the ToDo List application.
# Modification History:
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# 06-07-2025      jdmunoz         Refactor the connection to the database
#                                 for better error handling and avoid
#                                 connection blockage.
#                                 Methods:
#                                 - Insert_task
#                                 - get_task
#                                 - get_all_tasks
#                                 - update_task
#                                 - delete_task
# 08-07-2025      jdmunoz         Add validation and sanitization
#                                 Methods:
#                                 - Insert_task
#                                 - get_task
#                                 - update_task
#                                 - delete_task
# *********************************************************


# Libraries
import sqlite3
from datetime import datetime
from todo_db.database import get_db_connection
from todo_db.validation import InputValidator, ValidationError


# Project     :   ToDo List
# Method      :   Insert_task
# Description :   This method inserts a new task in the database.
# Modification History:
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# 06-07-2025      jdmunoz         Refactor the connection to the database
#                                 for better error handling and avoid
#                                 connection blockage.
# 08-07-2025      jdmunoz         Add validation and sanitization 
# *********************************************************
def Insert_task(task: str, description: str = None) -> int: 

    try:
        # validate and snitize the task input in the insert method    
        validated_data = InputValidator.validate_task_creation(task, description)

        with get_db_connection() as conn:
            cursor = conn.cursor()

            cursor.execute(
                'INSERT INTO tasks (task, description) VALUES (?, ?)',
                (validated_data['task'], validated_data['description'])
            )

            conn.commit()
            task_id = cursor.lastrowid

            return task_id
    except ValidationError as e:   
        print(f"Validation error in Insert_task: {e}")
        return False        
    except sqlite3.OperationalError as e:
        print(f"Database error in Insert_task: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error in Insert_task: {e}")
        return False    


# Project     :   ToDo List
# Method      :   get_task
# Description :   This method retrieves a task by its ID from the database.
# Modification History:
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# 06-07-2025      jdmunoz         Refactor the connection to the database
#                                 for better error handling and avoid
#                                 connection blockage.
# 08-07-2025      jdmunoz         Add validation and sanitization 
# *********************************************************
def get_task(task_id: int):

    try: 
        
        # validate task_id 
        validated_data = InputValidator.validate_task_id(task_id)

        with get_db_connection() as conn:
            cursor = conn.cursor()

            cursor.execute('SELECT * FROM tasks WHERE id = ?', (validated_data,))
            task = cursor.fetchone()

            #conn.close()

            if task is None:
                return None 
            
            return task
    except ValidationError as e:
        print(f"Validation error in get_task: {e}")
        return False         
    except sqlite3.OperationalError as e:
        print(f"Database error in get_task: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error in get_task: {e}")
        return False         


# Project     :   ToDo List
# Method      :   get_all_tasks
# Description :   This method retrieves all tasks from the database.
# Modification History:
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# 06-07-2025      jdmunoz         Refactor the connection to the database
#                                 for better error handling and avoid
#                                 connection blockage.
# *********************************************************
def get_all_tasks() -> list:
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()

            cursor.execute('SELECT * FROM tasks')
            tasks = cursor.fetchall()

            #conn.close()

            return tasks
        
    except sqlite3.OperationalError as e:
        print(f"Database error in get_all_tasks: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error in get_all_tasks: {e}")
        return False        



# Project     :   ToDo List
# Method      :   update_task
# Description :   This method updates an existing task in the database 
#                 by a dinamic query.
# Modification History:
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# 06-07-2025      jdmunoz         Refactor the connection to the database
#                                 for better error handling and avoid
#                                 connection blockage.
# 08-07-2025      jdmunoz         Add validation and sanitization 
# *********************************************************
def update_task(task_id: int, task_data: dict) -> bool:
    
    try:
        
        # validate and snitize the task input
        validated_id, validated_data = InputValidator.validate_task_update(task_id, task_data)
        

        with get_db_connection() as conn:
            
            cursor = conn.cursor()

            updates = []
            params = []

            # Prepare the update query dynamically based on provided task_data
            for key, value in validated_data.items():
                if value is not None:
                    # Special handling for 'finished' key to set end_time
                    if key == "finished" and value == 'Y':
                        updates.append("end_time = ?")
                        params.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                        updates.append(f"{key} = ?")
                        params.append(value)
                    elif key == "finished" and value == 'N':    
                        updates.append("end_time = ?")
                        params.append(None)
                        updates.append(f"{key} = ?")
                        params.append(value)
                    else:
                        updates.append(f"{key} = ?")
                        params.append(value)
                        

            if not updates:
                conn.close()
                return False

            # append the task_id to the parameters for the WHERE clause
            params.append(validated_id)      

            # Create the update query
            update_query = f"UPDATE tasks SET {', '.join(updates)} WHERE id = ?"

            # Execute the update query
            cursor.execute(update_query, params)

            conn.commit()

            return True    
    except ValidationError as e:
        print(f"Validation error in update_task: {e}")
        return False
    except sqlite3.OperationalError as e:
        print(f"Database error in update_task: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error in update_task: {e}")
        return False


# Project     :   ToDo List
# Method      :   delete_task
# Description :   This method deletes a task from the database by its ID.
# Modification History:
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# 06-07-2025      jdmunoz         Refactor the connection to the database
#                                 for better error handling and avoid
#                                 connection blockage.
# 08-07-2025      jdmunoz         Add validation and sanitization 
# *********************************************************
def delete_task(task_id: int) -> bool:

    try:

        # validate task_id 
        validated_data = InputValidator.validate_task_id(task_id)

        with get_db_connection() as conn:
            cursor = conn.cursor()

            cursor.execute('DELETE FROM tasks WHERE id = ?', (validated_data,))
            conn.commit()

            rows_afected = cursor.rowcount
            #conn.close()

            return rows_afected > 0
    except ValidationError as e:
        print(f"Validation error in delete_task: {e}")
        return False    
    except sqlite3.OperationalError as e:
        print(f"Database error in delete_task: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error in delete_task: {e}")
        return False        





