# Project     :   ToDo List
# Package     :   llm_router.py
# Description :   This package contains the LLM router for 
#                 the ToDo List application.
# Modification History:
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# 08-07-2025      jdmunoz         the method query_tasks was moved to the
#                                 todo_ai.llm module.
#                                 Change in the prompt 
# *********************************************************


# Libraries
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from todo_ai.llm import query_tasks
# *********************************************************


# Constants
#PROMPT = "Give me a summary of the taks Where you specified percentage of completion, " \
#        "percentage of not complete. add an insight (add emojis throughout the response, at lest 3 emojis)" \
# *********************************************************

PROMPT ="Give me a summary of the taks Where you specified percentage of completion, " \
        "percentage of not complete. add a short insight (add emojis throughout the response, at lest 3 emojis)" \
        "Count the tasks in the table and take into account the field finised in order to know how many were finiched,"\
        "it is given by the Y or N also be very precise in the answer and the counting of information"\
        "Also make it a short paragraph answer do not make a list nor separation between the summary and the insigt"



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
