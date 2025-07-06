# Project     :   ToDo List
# Package     :   llm_router.py
# Description :   This package contains the LLM router for 
#                 the ToDo List application.
# Modification History:
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# *********************************************************


# Libraries
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from todo_ai.llm import query_llm
# *********************************************************


# Constants
PROMPT = "Give me a summary of the taks qhere you specified percentage of completion, percentage of not complete. You can add a motivational phrase"
# *********************************************************


# Project     :   ToDo List
# Method      :   query_tasks
# Description :   Private method to query the LLM with a PROMPT.
# Modification History:
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# *********************************************************
def query_tasks(question: str) -> str:
    query_engine = query_llm()
    response = query_engine.query(question)
    return str(response)



# creating the router for the API
router = APIRouter()


# Project     :   toDo List
# Method      :   query_llm_endpoint
# Description :   Router endpoint to query the LLM with a 
#                 predefined prompt with json response.
# Modification History:
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# *********************************************************
@router.post("/query")
def query_llm_endpoint():
    try:
        response = query_tasks(PROMPT)
        return JSONResponse(content={"response": response})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error querying LLM: {str(e)}")
    

@router.get("/")
def root():
    return JSONResponse(content={"message": "Welcome to the ToDo llm API!"})    
