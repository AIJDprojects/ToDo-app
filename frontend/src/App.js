import { useState } from 'react';
import './App.css';

function App() {

  // State to holde the todos
  const [todos, setTodos] = useState([]);

  // State to hold the input
  const [taskInput, setInput] = useState('');
  const [descriptionInput, setDescriptionInput] = useState('');

  // state to control the input fields 
  const [showForm, setShowForm] = useState(false);

  // function for the button
  const handleAddTask = () => {
    setShowForm(true);
  };

  // function to handle the submission
  const handleSubmit = () => {
    if (taskInput.trim()) {

      // task object
      const newTodo = {
        id: Date.now(),
        text: taskInput,
        description: descriptionInput || null,
      };
    

    setTodos([...todos, newTodo]);

    // reset 
    setInput('');
    setDescriptionInput('');
    setShowForm(false);
    }  

  };

  // function to cancel form
  const handleCancel = () => {
    setInput('');
    setDescriptionInput('');
    setShowForm(false);
  };
  

  return (
    <div className="App">
      <header className="todo-header">
        <h1>TodoAP</h1>
        <p>My Personal Todo Application</p>
      </header>
      
      <main className="todo-main">
        <div className="add-todo">
          {!showForm ? (
            // Initial state - just the "Add Task!" button
            <button onClick={handleAddTask}>Add Task!</button>
          ) : (
            // Form state - show input fields
            <div className="todo-form">
              <input 
                type="text" 
                placeholder="Task title*" 
                value={taskInput}
                onChange={(e) => setInput(e.target.value)}
              />
              <input 
                type="text" 
                placeholder="Description" 
                value={descriptionInput}
                onChange={(e) => setDescriptionInput(e.target.value)}
              />
              <div className="form-buttons">
                <button onClick={handleSubmit}>Save Task</button>
                <button onClick={handleCancel} className="cancel-btn">Cancel</button>
              </div>
            </div>
          )}
        </div>

        
        <div className="todo-list">
          {todos.length === 0 ? (
            <p>Your tasks will appear here...</p>
          ) : (
            <div>
              <h3>Your Tasks:</h3>
              {todos.map(todo => (
                <div key={todo.id} className="todo-item">
                  <h4>{todo.task}</h4>
                  {todo.description && <p>{todo.description}</p>}
                </div>
              ))}
            </div>
          )}
          <p>Number of todos: {todos.length}</p>
        </div>
      </main>
    </div>
  );
}

export default App;
