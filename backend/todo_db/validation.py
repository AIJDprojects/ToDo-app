# Project     :   ToDo List
# Package     :   validation.py  
# Description :   This package contains validation and sanitization
#                 utilities for the ToDo List application.
# Modification History:
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# *********************************************************

# Libraries
import re
import html
from typing import Optional, Dict, Any, List
from datetime import datetime
from pydantic import BaseModel, field_validator
import bleach


# Project     :   ToDo List
# Method      :   ValidationError
# Description :   This class is used to represent custom 
#                 validation errors.
# Modification History:
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# *********************************************************
class ValidationError(Exception):
    pass



# Project     :   ToDo List
# Method      :   DataSanitizer
# Description :   This class is used to sanitize data.
# Modification History:
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# *********************************************************
class DataSanitizer:

    # Sanitiza string input by removing HTML tags,
    # escaping special characters, and trimming whitespace.
    @staticmethod
    def sanitize_string(text: str, max_length: int = 500) -> str:

        if not isinstance(text, str):
            raise ValidationError("Input must be a string.")
           
        # Remove whitespace 
        text = text.strip()
        # Remove HTML tags
        text = bleach.clean(text, tags=[], strip=True)

        # Escape HTML entities
        text = html.escape(text)

        # Limit length
        if len(text) > max_length:
            text = text[:max_length]

        return text
    
    # Validate and sanitize task name
    @staticmethod
    def sanitize_task_name(task: str) -> str:
        
        if not task or not task.strip():
            raise ValidationError("Task name cannot be empty.")

        sanitized = DataSanitizer.sanitize_string(task, max_length=200)

        # remove consecutive spaces
        sanitized = re.sub(r'\s+', ' ', sanitized)
        if len(sanitized) < 3:
            raise ValidationError("Task name must be at least 3 characters long.")
        
        return sanitized
    
    # Validate and sanitize task description
    @staticmethod
    def sanitize_description(description: Optional[str]) -> Optional[str]:

        if description is None or description.strip() == "":
            return None
        
        sanitized = DataSanitizer.sanitize_string(description, max_length=500)

        # remove consecutive spaces
        sanitized = re.sub(r'\s+', ' ', sanitized)

        return sanitized
    
    # validate and sanitize finished status
    @staticmethod
    def sanitixe_finished_status(status: str) -> str:

        if not isinstance(status, str):
            raise ValidationError("Finished status must be a string.")
        
        status = status.upper().strip()

        if status not in ["Y","N"]: 
            raise ValidationError("Finished status must be 'Y' or 'N'.")
        
        return status
    


# Project     :   ToDo List
# Method      :   DataValidator
# Description :   This class is for data validation in 
#                 operations CRUD.
# Modification History:
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# *********************************************************  

class DataValidator:

    # Validate task ID 
    @staticmethod
    def validate_id(task_id: Any) -> int:

        try: 
            task_id = int(task_id)
            if task_id <= 0:
                raise ValidationError("Task ID must be a positive integer.")

            return task_id
        except (ValueError, TypeError):
            raise ValidationError("Task ID must be a valid integer.")

    # Validate task data for update or creation
    @staticmethod
    def validate_task_data(data: Dict[str, Any]) -> Dict[str, Any]:

        validated_data = {}

        if 'task' in data:
            validated_data['task'] = DataSanitizer.sanitize_task_name(data['task'])

        if 'description' in data:
            validated_data['description'] = DataSanitizer.sanitize_description(data('description'))

        if 'finished' in data:
            validated_data['finished'] = DataSanitizer.sanitixe_finished_status(data['finished']) 

        return validated_data

    # Validate datetime format
    @staticmethod
    def validate_datetime_string(date_str: str) -> bool:

        try: 
            datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
            return True
        except ValueError:
            return False
        

# Project     :   ToDo List
# Method      :   SQLInjectionProtector
# Description :   This class is used to protect against SQL 
#                 injection attacks
# Modification History:
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# *********************************************************
class SQLInjectionProtector:

    # SQL injection patterns
    SQL_INJECTION_PATTERNS = [
        r"(\b(SELECT|INSERT|UPDATE|DELETE|DROP|CREATE|ALTER|EXEC|UNION)\b)",
        r"(--|#|/\*|\*/)",
        r"(\b(OR|AND)\s+\d+\s*=\s*\d+)",
        r"(\'\s*(OR|AND)\s*\'\w*\'\s*=\s*\'\w*\')",
        r"(\bUNION\s+SELECT\b)",
    ]

    # detect potential SQL injection attempts
    @staticmethod
    def detect_sql_injection(text: str) -> bool:

        if not isinstance(text, str):
            return False
        
        text_upper = text.upper()

        for pattern in SQLInjectionProtector.SQL_INJECTION_PATTERNS:
            if re.search(pattern, text_upper, re.IGNORECASE):
                return True

        return False
    

    # validate input for SQL injection
    @staticmethod
    def validate_safe_input(text: str) -> str:

        if SQLInjectionProtector.detect_sql_injection(text):
            raise ValidationError("Potential SQL injection detected in input.")

        return text
    
    
# Project     :   ToDo List
# Method      :   InputValidator
# Description :   Main validator class that combines all 
#                validation methods.
# Modification History:
# *********************************************************
# Date            Author          Modification
# 05-07-2025      jdmunoz         Creation
# *********************************************************
class InputValidator:

    # Validate data for task creation
    @staticmethod
    def validate_task_creation(task: str, description: Optional[str] = None) -> Dict[str, Any]:
        
        
        # Check for SQL injection
        SQLInjectionProtector.validate_safe_input(task)
        if description:
            SQLInjectionProtector.validate_safe_input(description)
        
        # Sanitize data
        validated_data = {
            'task': DataSanitizer.sanitize_task_name(task),
            'description': DataSanitizer.sanitize_description(description)
        }
        
        return validated_data
    

    # Validate data for task update
    @staticmethod
    def validate_task_update(task_id: Any, update_data: Dict[str, Any]) -> tuple[int, Dict[str, Any]]:
        
        # Validate ID
        validated_id = DataValidator.validate_id(task_id)
        
        # Check for SQL injection in all string fields
        for key, value in update_data.items():
            if isinstance(value, str):
                SQLInjectionProtector.validate_safe_input(value)
        
        # Validate and sanitize update data
        validated_data = DataValidator.validate_task_data(update_data)
        
        return validated_id, validated_data 
   
    # Validate data for task retrieval
    @staticmethod
    def validate_task_id(task_id: Any) -> int:

        return DataValidator.validate_id(task_id)









    




    



