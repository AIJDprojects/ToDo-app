# Project     :   ToDo List
# Package     :   api.py
# Description :   API package for the ToDo List application
#                 This package contains the FastAPI application and its routes.
#                 It serves as the entry point for the web server.
# Modification History: 
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# *********************************************************


from fastapi import FastAPI
from todo_db.crud_router import router as crud_router
from todo_ai.llm_router import router as llm_router

# Create the API
app = FastAPI()

# Include the CRUD router
app.include_router(crud_router, prefix="/crud")

# Include the llm router
app.include_router(llm_router, prefix="/llm")



@app.get("/hi")
def hi():
    return {"message": "Hello, World!"}