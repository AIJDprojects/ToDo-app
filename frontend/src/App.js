// Project     :   Todo List
// Package     :   App.js
// Description :   Main component of the application
// Modification History:
// *********************************************************
// Date            Author          Modification
// 05-07-2025      jdmunoz         Creation
// *********************************************************

import { useState } from 'react';
import './App.css';
import TodoForm from './components/todoform';
import TodoList from './components/todolist';

function App() {

  // State to holde the todos
  const [todos, setTodos] = useState([]);

  // add a new Task (using TodoForm)
  const handleAddTodo = (newTodo) => {
    const todoWithId = {
      ...newTodo,
      id: Date.now(),
      finished: 'N'
    };

    setTodos([...todos, todoWithId]);
  };

  return (
    <div className="App">
      <header className="todo-header">
        <h1>TodoAP</h1>
        <p>My Personal Todo Application</p>
      </header>
      
      <main className="todo-main">
        <TodoForm onAddTodo={handleAddTodo} />
        <TodoList todos={todos} />
      </main>
    </div>
  );
}

export default App;
