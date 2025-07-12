// Project     :   Todo app
// Package     :   todolist.js
// Description :   controls the list and shows the tasks
// Modification History:
// *********************************************************
// Date            Author          Modification
// 11-07-2025      jdmunoz         Creation
// *********************************************************
function TodoList({ todos }) {
  return (
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
  );
}

export default TodoList;
