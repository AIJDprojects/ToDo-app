// Project     :   Todo app
// Package     :   todoform.js 
// Description :   Todo from add task button
// Modification History:
// *********************************************************
// Date            Author          Modification
// 11-07-2025      jdmunoz         Creation
// *********************************************************

import { useState } from 'react';

function TodoForm({ onAddTodo }) {

  // State for the input values
  const [taskInput, setTaskInput] = useState('');
  const [descriptionInput, setDescriptionInput] = useState('');
  
  // State to control if we show the form
  const [showForm, setShowForm] = useState(false);

  // Function to handle "Add Task!" button click
  const handleAddTaskClick = () => {
    setShowForm(true);
  };

  // Function to handle form submission
  const handleSubmit = () => {
    if (taskInput.trim()) {
      // Create new todo object matching your backend structure
      const newTodo = {
        task: taskInput,
        description: descriptionInput || null,
      };
      
      // Call the parent function to add the todo
      onAddTodo(newTodo);
      
      // Reset form
      setTaskInput('');
      setDescriptionInput('');
      setShowForm(false);
    }
  };

  // Function to cancel form
  const handleCancel = () => {
    setTaskInput('');
    setDescriptionInput('');
    setShowForm(false);
  };

  return (
    <div className="add-todo">
      {!showForm ? (
        // Initial state - just the "Add Task!" button
        <button onClick={handleAddTaskClick}>Add Task!</button>
      ) : (
        // Form state - show input fields
        <div className="todo-form"> 
        <h2>Add a new task</h2>
        <div className="input-section">
            <div className="input-fields">
            <input 
                type="text" 
                placeholder="Task title (required)" 
                value={taskInput}
                onChange={(e) => setTaskInput(e.target.value)}
            />
            <input 
                type="text" 
                placeholder="Description (optional)" 
                value={descriptionInput}
                onChange={(e) => setDescriptionInput(e.target.value)}
            />
            </div>
            <div className="button-section">
            <button onClick={handleSubmit} className="save-btn">Save Task</button>
            <button onClick={handleCancel} className="cancel-btn">Cancel</button>
            </div>
        </div>
        

          
        </div>
      )}
    </div>
  );
}

export default TodoForm;
