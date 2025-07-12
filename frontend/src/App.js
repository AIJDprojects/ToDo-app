// Project     :   Todo List
// Package     :   App.js
// Description :   Main component of the application
// Modification History:
// *********************************************************
// Date            Author          Modification
// 05-07-2025      jdmunoz         Creation
// *********************************************************

import { useState, useEffect } from 'react';
import './App.css';
import TodoForm from './components/todoform';
import TodoList from './components/todolist';
import { todoAPI } from './services/api';

function App() {
  // State to hold the todos
  const [todos, setTodos] = useState([]);
  const [loading, setLoading] = useState(false);
  const [aiInsights, setAiInsights] = useState('');

  // Load todos when component mounts
  useEffect(() => {
    loadTodos();
  }, []);

  // Auto-update AI insights whenever todos change
  useEffect(() => {
    if (todos.length > 0) {
      updateAIInsights();
    }
  }, [todos]);

  // Function to convert array format to object format
  const convertArrayToTodo = (todoArray) => {
    return {
      id: todoArray[0],
      task: todoArray[1],
      description: todoArray[2],
      created_date: todoArray[3],
      updated_date: todoArray[4],
      finished: todoArray[5]
    };
  };

  // Function to load todos from API
  const loadTodos = async () => {
    try {
      setLoading(true);
      const todosData = await todoAPI.getAllTasks();
      // Convert array format to object format
      const convertedTodos = todosData.map(convertArrayToTodo);
      setTodos(convertedTodos);
    } catch (error) {
      console.error('Failed to load todos:', error);
      alert('Failed to load todos. Make sure your backend is running!');
    } finally {
      setLoading(false);
    }
  };

  // Function to add a new todo (using API)
  const handleAddTodo = async (newTodo) => {
    try {
      setLoading(true);
      const createdTodo = await todoAPI.createTask(newTodo);
      // Convert the response and add to todos
      const convertedTodo = Array.isArray(createdTodo) ? convertArrayToTodo(createdTodo) : createdTodo;
      setTodos([...todos, convertedTodo]);
    } catch (error) {
      console.error('Failed to create todo:', error);
      alert('Failed to create todo. Please try again!');
    } finally {
      setLoading(false);
    }
  };

  // Function to update AI insights automatically
  const updateAIInsights = async () => {
    try {
      const insights = await todoAPI.getAIInsights();
      setAiInsights(insights.response);
    } catch (error) {
      console.error('Failed to get AI insights:', error);
      // Don't show alert for automatic updates, just log the error
    }
  };

  return (
    <div className="App">
      <header className="todo-header">
        <h1>📝 Todo AI</h1>
        <p>AI Driven Todo List application 🤖 </p>
      </header>
      
      <main className="todo-main">
        
        
        {/* AI Insights Section - Auto-updated */}
        {aiInsights && (
          <div className="ai-section">
            <div className="ai-insights">
              <h3>🤖 AI Assistant:</h3>
              <p>{aiInsights}</p>
            </div>
          </div>
        )}

        <TodoForm onAddTodo={handleAddTodo} />

        <TodoList todos={todos} />
      </main>
    </div>
  );
}

export default App;

