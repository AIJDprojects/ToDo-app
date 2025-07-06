# Project     :   ToDo List
# Package     :   database.py
# Description :   This package contains the database creation and connection for the ToDo List application.
# Modification History:
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# *********************************************************

import sqlite3
import os


# paths contants
DB_FOLDER = "database"
DB_NAME = "todo.db"
DB_PATH = os.path.join(DB_FOLDER, DB_NAME)



# Project     :   ToDo List
# Method      :   Val_Create_folder
# Description :   This method creates the database folder if it does not exist.
# Modification History:
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# *********************************************************
def Val_Create_folder():
     
    if not os.path.exists(DB_FOLDER):
        os.makedirs(DB_FOLDER)




# Project     :   ToDo List
# Method      :   get_db_connection
# Description :   This method establishes a connection to the SQLite database.
# Modification History:
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# *********************************************************
def get_db_connection():
    # Returns a connection to the SQLite database.
    return sqlite3.connect(DB_PATH)


# Project     :   ToDo List
# Method      :   init_db
# Description :   This method initializes the database by creating the tasks table
#                 if it does not exist.  
# Modification History:
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# *********************************************************
def init_db():
    # Creates the folder if it does not exist
    Val_Create_folder()

    # Establish a connection to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create the tasks table if it does not exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        description TEXT,
        creation_time TEXT DEFAULT CURRENT_TIMESTAMP,
        end_time TEXT,
        finished TEXT CHECK(finished IN ('Y', 'N')) DEFAULT 'N'
    )
    ''')

    conn.commit()  # Commit the changes
    conn.close()  # Close the connection


# start init_db as soon as this file is imported
init_db()
