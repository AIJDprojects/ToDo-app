# Project     :   ToDo List
# Package     :   models.py
# Description :   This package contains the Pydantic models 
#                 for the ToDo List application.
# Modification History:
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# *********************************************************

# Libraries
from pydantic import BaseModel
from datetime import datetime
from typing import Optional


# Project     :   ToDo List
# Method      :   TaskBase
# Description :   This class is the base model for tasks. 
# Modification History:
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# *********************************************************
class TaskBase(BaseModel):
    task: str
    description: Optional[str] = None


# Project     :   ToDo List
# Method      :   TaskCreate
# Description :   This class is used for creating new tasks.
#                 it is the same as the TaskBase model
# Modification History:
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# *********************************************************
class TaskCreate(TaskBase):
    pass


# Project     :   ToDo List
# Method      :   Task
# Description :
# Modification History:
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# *********************************************************
class Task(TaskBase):
    id: int
    creation_time: datetime
    end_time: Optional[datetime] = None
    finished: str

    class Config:
        orm_mode = True


# Project     :   ToDo List
# Method      :   TaskUpdate
# Description :   This class is used for updating existing tasks.
# Modification History:
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# *********************************************************    

class TaskUpdate(BaseModel):
    task: Optional[str] = None
    description: Optional[str] = None
    finished: Optional[str] = None

  