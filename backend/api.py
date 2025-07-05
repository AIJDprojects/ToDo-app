# Project     :   ToDo List
# Package     :   api 
# Description :   API package for the ToDo List application
#                This package contains the FastAPI application and its routes.
#                It serves as the entry point for the web server.
# Modification History: 
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# *********************************************************


from fastapi import FastAPI

# Create dummy api
app = FastAPI()

@app.get("/hi")
def hi():
    return {"message": "Hello, World!"}