// Project     :   Todo App
// Package     :   api.js
// Description :   services to connect to the backend
// Modification History:
// *********************************************************
// Date            Author          Modification
// 11-07-2025      jdmunoz         Creation
// *********************************************************

// API base URL
const API_BASE_URL = 'http://localhost:8070';



// API functions
export const todoAPI = {

 // LLM/AI Functions
  getAIInsights: async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/llm/query`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
      });
      
      if (!response.ok) {
        throw new Error('Failed to get AI insights');
      }
      return await response.json();
    } catch (error) {
      console.error('Error getting AI insights:', error);
      throw error;
    }
  },

    // Get all tasks
  getAllTasks: async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/crud/getall`, {
        method: 'GET'
        }
      );

      if (!response.ok) {
        throw new Error('Failed to fetch todos');
      }
      return await response.json();
    } catch (error) {
      console.error('Error fetching todos:', error);
      throw error;
    }
  },

  // Create a new Task
  createTask: async (todoData) => {
    try {
      const response = await fetch(`${API_BASE_URL}/crud/create`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(todoData),
      });
      
      if (!response.ok) {
        throw new Error('Failed to create todo');
      }
      return await response.json();
    } catch (error) {
      console.error('Error creating todo:', error);
      throw error;
    }
  },

  // Update a task
  updateTask: async (taskId, todoData) => {
    try {
      const response = await fetch(`${API_BASE_URL}/crud/update/${taskId}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(todoData),
      });
      
      if (!response.ok) {
        throw new Error('Failed to update todo');
      }
      return await response.json();
    } catch (error) {
      console.error('Error updating todo:', error);
      throw error;
    }
  },

  // Add this function to your existing todoAPI object
  updateTaskStatus: async (taskId, finished) => {
    try {
      const response = await fetch(`${API_BASE_URL}/crud/update/${taskId}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ finished: finished }),
      });
      
      if (!response.ok) {
        throw new Error('Failed to update task status');
      }
      return await response.json();
    } catch (error) {
      console.error('Error updating task status:', error);
      throw error;
    }
  },


  // Delete a Task
  deleteTask: async (taskId) => {
    try {
      const response = await fetch(`${API_BASE_URL}/crud/delete/${taskId}`, {
        method: 'DELETE',
      });
      
      if (!response.ok) {
        throw new Error('Failed to delete todo');
      }
      return await response.json();
    } catch (error) {
      console.error('Error deleting todo:', error);
      throw error;
    }
  }

}