import './App.css';

function App() {
  return (
    <div className="App">
      <header className="todo-header">
        <h1>TodoAP</h1>
        <p>My Personal Todo Application</p>
      </header>
      
      <main className="todo-main">
        <div className="add-todo">
          <input 
            type="text" 
            placeholder="What needs to be done?" 
          />
          <button>Add Todo</button>
        </div>
        
        <div className="todo-list">
          <p>Your todos will appear here...</p>
        </div>
      </main>
    </div>
  );
}

export default App;
