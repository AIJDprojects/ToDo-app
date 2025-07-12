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
import TodoForm from './components/todoform.jsx';
import TodoList from './components/todolist.jsx';
import Modal from './components/Modal.jsx';
import TaskModal from './components/TaskModal.jsx';
import { todoAPI } from './services/api.jsx';

function App() {
  // State to hold the todos
  const [todos, setTodos] = useState([]);
  const [loading, setLoading] = useState(false);
  const [aiInsights, setAiInsights] = useState('');

  // Load todos when component mounts
  useEffect(() => {
    loadTodos();
  }, []);

    // Add modal state
  const [modal, setModal] = useState({
    isOpen: false,
    type: 'confirm', // 'confirm' or 'alert'
    title: '',
    message: '',
    onConfirm: null
  });

  const [taskModal, setTaskModal] = useState({
    isOpen: false,
    task: null
  });
  

  // Auto-update AI insights whenever todos change
  useEffect(() => {
    if (todos.length > 0) {
      //updateAIInsights();
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
      showAlert('Failed to load todos. Make sure your backend is running!');
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
      //showAlert('✅ Success', 'Task created successfully!');
    } catch (error) {
      console.error('Failed to create todo:', error);
      showAlert('❌ Error', 'Failed to create task. Please try again!');
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


  // Function to handle checkbox toggle
  const handleToggleComplete = async (taskId, currentStatus) => {
    try {
      setLoading(true);
      const newStatus = currentStatus === 'Y' ? 'N' : 'Y';
      await todoAPI.updateTaskStatus(taskId, newStatus);
      setTodos(todos.map(todo => 
        todo.id === taskId 
          ? { ...todo, finished: newStatus }
          : todo
      ));
      // updateAIInsights();
    } catch (error) {
      console.error('Failed to update task status:', error);
      showAlert('❌ Error', 'Failed to update task. Please try again!');
    } finally {
      setLoading(false);
    }
  };

    // Function to show custom alerts
  const showAlert = (title, message) => {
    setModal({
      isOpen: true,
      type: 'alert',
      title: title,
      message: message,
      onConfirm: null
    });
  };


  // Function to handle task deletion
  const handleDeleteTask = async (taskId, taskTitle) => {
     setModal({
      isOpen: true,
      type: 'confirm',
      title: '🗑️ Delete Task',
      message: `Are you sure you want to delete "${taskTitle}"?\n\nThis action cannot be undone.`,
      onConfirm: () => confirmDeleteTask(taskId)
    });
  };

  const confirmDeleteTask = async (taskId) => {
    setModal({ ...modal, isOpen: false });
    
    try {
      setLoading(true);
      await todoAPI.deleteTask(taskId);
      setTodos(todos.filter(todo => todo.id !== taskId));
      // updateAIInsights();
      
      // Show success message
      showAlert('✅ Success', 'Task deleted successfully!');
      
    } catch (error) {
      console.error('Failed to delete task:', error);
      showAlert('❌ Error', 'Failed to delete task. Please try again!');
    } finally {
      setLoading(false);
    }
  };

  // Function to handle task editing (for now, just show alert - we'll implement later)
  const handleEditTask = (taskId, currentTask) => {
      setTaskModal({
      isOpen: true,
      task: currentTask
    });
  };

  // handling both add and edit:
  const handleSaveTask = async (taskIdOrData, taskData = null) => {
    try {
      setLoading(true);
      
      if (taskData) {
        // Editing existing task
        await todoAPI.updateTask(taskIdOrData, taskData);
        setTodos(todos.map(todo => 
          todo.id === taskIdOrData 
            ? { ...todo, ...taskData }
            : todo
        ));
        showAlert('✅ Success', 'Task updated successfully!');
      } else {
        // Adding new task (use your existing logic)
        const createdTodo = await todoAPI.createTask(taskIdOrData);
        const convertedTodo = Array.isArray(createdTodo) ? convertArrayToTodo(createdTodo) : createdTodo;
        setTodos([...todos, convertedTodo]);
        showAlert('✅ Success', 'Task created successfully!');
      }
      
      setTaskModal({ isOpen: false, task: null });
      // updateAIInsights();
      
    } catch (error) {
      console.error('Failed to save task:', error);
      showAlert('❌ Error', 'Failed to save task. Please try again!');
    } finally {
      setLoading(false);
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

        <TodoList 
          todos={todos} 
          onToggleComplete={handleToggleComplete}
          onEditTask={handleEditTask}
          onDeleteTask={handleDeleteTask}
          loading={loading}
        />
      </main>

      {/* Custom Modal */}
      <Modal
        isOpen={modal.isOpen}
        onClose={() => setModal({ ...modal, isOpen: false })}
        onConfirm={modal.onConfirm}
        title={modal.title}
        message={modal.message}
        type={modal.type}
      />

      <TaskModal
        isOpen={taskModal.isOpen}
        onClose={() => setTaskModal({ isOpen: false, task: null })}
        onSave={handleSaveTask}
        task={taskModal.task}
        loading={loading}
      />
    </div>
  );
}

export default App;
