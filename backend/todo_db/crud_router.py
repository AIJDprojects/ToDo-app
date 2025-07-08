# Project     :   ToDo List
# Package     :   crud_router.py
# Description :   This package contains the router for the 
#                 CRUD operations
# Modification History:
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# *********************************************************

# Libraries
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from todo_db.crud import Insert_task, get_all_tasks, update_task, delete_task, get_task
from todo_db.models import Task, TaskCreate, TaskUpdate


# creating the router for the API 
router = APIRouter()


# Project     :   ToDo List
# Method      :   create_new_task
# Description :   This method creates a new task in the database.
# Modification History:
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# *********************************************************
@router.post("/create", response_model=Task)
def create_new_task(task: TaskCreate):
    
    # Insert the task into the database
    task_id = Insert_task(task.task, task.description)
    
    # validate the task creation
    created_task = get_task(task_id)

    if not created_task:
        raise HTTPException(status_code=500, detail="Error creating task")
    # Return the created task
    return JSONResponse(content=created_task)
    


# Project     :   ToDo List
# Method      :   get_all
# Description :   This method retrieves all tasks from the 
#                 database.
# Modification History:
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# *********************************************************
@router.get("/getall", response_model=list[Task])
def get_all():
    task = get_all_tasks()

    if not task:    # validate the task creation
        raise HTTPException(status_code=500, detail="No tasks found")
    
    # Return the created task
    return JSONResponse(content=task)


# Project     :   ToDo List
# Method      :   update_task_by_id
# Description :   This method updates a task by its ID in the 
#                 database.
# Modification History:
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# *********************************************************
@router.put("/update/{task_id}", response_model=Task)
def update_task_by_id(task_id: int, task_update: TaskUpdate):
    
    # validate the task ID
    existing_task = get_task(task_id)
    if not existing_task:
        raise HTTPException(status_code=500, detail="Task not found")
    

    # update the task in the database
    update_data  = task_update.model_dump(exclude_unset=True)
    updated_task = update_task(task_id, update_data)

    # validate the task update
    if not updated_task:
        raise HTTPException(status_code=500, detail="Failed to update task")
    
    # Get the updated task
    nu_task = get_task(task_id)
    
    return JSONResponse(content=nu_task)


# Project     :   ToDo List
# Method      :   delete_task_by_id
# Description :   This method deletes a task by its ID from the 
#                 database.
# Modification History:
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# *********************************************************
@router.delete("/delete/{task_id}")
def delete_task_by_id(task_id: int):

    existing_task = get_task(task_id)
    if not existing_task:
        raise HTTPException(status_code=500, detail="Task not found")

    deleted = delete_task(task_id)

    if not deleted:
        raise HTTPException(status_code=500, detail="error deleting task")
    
    return JSONResponse(content={"message": "Task deleted successfully"})


@router.get("/")
def root():
    return JSONResponse(content={"message": "Welcome to the ToDo CRUD API!"})

