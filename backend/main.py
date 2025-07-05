# Project     :   ToDo List
# Package     :   main 
# Description :   This Package has the objective to start the web server using uvicorn
# Modification History: 
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# *********************************************************

# Libraries 
import uvicorn # web server
import os
# ----


# Running uvicorn server with the api app
if __name__ == "__main__":
    # run the method to star the API
    uvicorn.run(
        "api:app", 
        host="0.0.0.0",
        reload=True, 
        port=int(os.environ.get("PORT",8070))
    )

