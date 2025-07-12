// Project     :   Todo app
// Package     :   todolist.js
// Description :   controls the list and shows the tasks
// Modification History:
// *********************************************************
// Date            Author          Modification
// 11-07-2025      jdmunoz         Creation
// *********************************************************
function TodoList({ todos, onToggleComplete, loading }) {
  // Function to format the date nicely
  const formatDate = (dateString) => {
    if (!dateString) return '';
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };
  
  
  
  return (
    <div className="todo-list">
      {todos.length === 0 ? (
        <p>Your new tasks will appear here...</p>
      ) : (
        <div>
          <h3>Your Tasks:</h3>
          {todos.map(todo => (
            <div key={todo.id} className={`todo-item ${todo.finished === 'Y' ? 'completed' : ''}`}>
              <div className="todo-content">
                <div className="todo-checkbox">
                  <input
                    type="checkbox"
                    checked={todo.finished === 'Y'}
                    onChange={() => onToggleComplete(todo.id, todo.finished)}
                    disabled={loading}
                    className="checkbox-input"
                  />
                </div>
                <div className="todo-text">
                  <h4>{todo.task}</h4>
                  {todo.description && <p>{todo.description}</p>}
                  <div className="todo-date">
                    📅 Created: {formatDate(todo.created_date)}
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
      <p>Tasks: {todos.length}</p>
    </div>
  );
}

export default TodoList;
