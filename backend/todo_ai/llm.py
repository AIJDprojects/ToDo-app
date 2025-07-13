# Project     :   ToDo List
# Package     :   llm.py
# Description :   This package contains the LLM (Large Language Model) 
#                 integration
# Modification History:
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# 13-07-2025      jdmunoz         Modification to alternate between 
#                                 models in the API with .env file
# *********************************************************

# Libraries
import os
from dotenv import load_dotenv
import requests
from typing import Any, Iterator, Optional
from llama_index.core.llms import CustomLLM, LLMMetadata
from llama_index.core.base.llms.types import CompletionResponse
from sqlalchemy import create_engine, MetaData, Table
from llama_index.core import SQLDatabase
from llama_index.core.query_engine import NLSQLTableQueryEngine
from google import genai
# **********************************************************


# Constants
DB_FOLDER = "database"
DB_NAME = "todo.db"
DB_ENTITY = "tasks"
# *********************************************************

# Load .env variables
load_dotenv()

# Model to be used in the App 
model = os.getenv("API_MODEL")



# Project     :   toDo List
# Method      :   CodeGPTLLM
# Description :   Class that integrates with the CodeGPT API 
#                 to generate completions. it creates the prompt 
#                 and sends it to the API.  
# Modification History:
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# *********************************************************
class CodeGPTLLM(CustomLLM):
    api_key: Optional[str] = None
    api_base: Optional[str] = None
    agent_id: Optional[str] = None
    organization_id: Optional[str] = None

    def __init__(self):                
        api_key = os.getenv("OPENAI_API_KEY")
        api_base = os.getenv("CODEGPT_API_BASE")
        agent_id = os.getenv("AGENT_ID")
        organization_id = os.getenv("ORGANIZATION_ID")
        super().__init__(
            api_key=api_key,
            api_base=api_base,
            agent_id=agent_id,
            organization_id=organization_id)
        
        
    @property
    def metadata(self) -> LLMMetadata:
        return LLMMetadata(
            context_window=4096,
            num_output=256,
            model_name="codegpt-custom",
            is_chat_model=True, 
            is_function_calling_model=False
        )   

    def complete(self, prompt: str, **kwargs:Any) -> CompletionResponse:
        try: 
            payload = {
                "agentId": f"{self.agent_id}",                      
                "messages": [{
                        "content":  f"{prompt}" ,
                        "role": "user"
                        }]
                }
            
            headers = {
                "accept": "application/json",
                "CodeGPT-Org-Id": f"{self.organization_id}",
                "content-type": "application/json",
                "authorization": f"Bearer {self.api_key}"
            }


            response = requests.post(
                f"{self.api_base}",
                json=payload,
                headers=headers
            )
            
            return CompletionResponse(text=response.text)
        except Exception as e:
            print(f"Error in CodeGPTLLM call: {e}")
            return CompletionResponse(text="Error in generating response")
        
    def stream_complete(self, prompt: str, **kwargs: Any) -> Iterator[CompletionResponse]:
        # For non-streaming implementation, just yield the complete response
        response = self.complete(prompt, **kwargs)
        yield response  


# Project     :   ToDo Lsit
# Method      :   GeminiLLM
# Description :   Class that integrates with the Gemini API 
#                 to generate completions. it creates the prompt 
#                 and sends it to the API.
# Modification History:
# *********************************************************
# Date            Author          Modification
# 13-07-2025      jdmunoz         Creation
# *********************************************************
class GeminiLLM(CustomLLM):
        
    @property
    def metadata(self) -> LLMMetadata:
        return LLMMetadata(
            context_window=4096,
            num_output=256,
            model_name="gemini-custom",
            is_chat_model=True,  # Set to True if your model supports chat format
            is_function_calling_model=False
        )   

    def complete(self, prompt: str, **kwargs:Any) -> CompletionResponse:
        try: 
            client = genai.Client()
            response = client.models.generate_content(
                    model="gemini-2.5-flash", contents=f"{prompt}"
                    )
            
            return CompletionResponse(text=response.text)
        except Exception as e:
            print(f"Error in GeminiLLM call: {e}")
            return CompletionResponse(text="Error in generating response")
        
    def stream_complete(self, prompt: str, **kwargs: Any) -> Iterator[CompletionResponse]:
        # For non-streaming implementation, just yield the complete response
        response = self.complete(prompt, **kwargs)
        yield response         



# Project     :   ToDo List
# Method      :   query_llm
# Description :   This method initializes the LLM, connects to the database
#                 and creates a query engine for the tasks table. 
# Modification History:
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# 13-07-2025      jdmunoz         Modification in order to be able to use 
#                                 gemini or codegpt APIs
# *********************************************************
def query_llm(model: str):

    if model == 'gemini':
        llm = GeminiLLM()
        print(f"conected to {model}")
    elif model == 'codegpt':
        # Initialize LLM
        print(f"conected to {model}")
        llm = CodeGPTLLM()

    # Connect to the database
    db_path = os.path.join(DB_FOLDER, DB_NAME)
    print(f"Connecting to database at: {db_path}")
    engine = create_engine(f"sqlite:///{db_path}")

    # Create a SQLDatabase instance
    sql_database = SQLDatabase(engine, include_tables=[f"{DB_ENTITY}"])

    # create a Query Engine
    query_engine = NLSQLTableQueryEngine(
    sql_database=sql_database,
    tables=["tasks"],
    llm=llm,
    synthesize_response=True
    )

    return query_engine



# Project     :   ToDo List
# Method      :   query_tasks
# Description :   Private method to query the LLM with a PROMPT.
# Modification History:
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# 08-07-2025      jdmunoz         The method query_tasks was moved to the
#                                 todo_ai.llm module. AS the Routers
#                                 are ment to had only the endpoints
#                                 and not the logic.
#                                 added llm_query_engine that is 
#                                 query engine initialized 
# *********************************************************
def query_tasks(question: str) -> str:
    query_engine = llm_query_engine
    response = query_engine.query(question)
    return str(response)




# Initialize the LLM query engine as soon as the module is imported default gemini
llm_query_engine = query_llm(model)

