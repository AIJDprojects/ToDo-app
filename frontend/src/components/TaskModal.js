// Project     :   Todo List
// Package     :   TaskModals
// Description :   Modals to pop up when adding or editing tasks
// Modification History:
// *********************************************************
// Date            Author          Modification
// 12-07-2025      jdmunoz         Creation
// *********************************************************
import { useState, useEffect } from 'react';

function TaskModal({ isOpen, onClose, onSave, task = null, loading = false }) {
  const [taskInput, setTaskInput] = useState('');
  const [descriptionInput, setDescriptionInput] = useState('');
  
  const isEditing = task !== null;

  // Populate form when editing
  useEffect(() => {
    if (isEditing && task) {
      setTaskInput(task.task || '');
      setDescriptionInput(task.description || '');
    } else {
      setTaskInput('');
      setDescriptionInput('');
    }
  }, [isEditing, task]);

  const handleSubmit = () => {
    if (taskInput.trim()) {
      const taskData = {
        task: taskInput.trim(),
        description: descriptionInput.trim() || null,
      };
      
      if (isEditing) {
        onSave(task.id, taskData);
      } else {
        onSave(taskData);
      }
    }
  };

  const handleClose = () => {
    setTaskInput('');
    setDescriptionInput('');
    onClose();
  };

  if (!isOpen) return null;

  return (
    <div className="modal-overlay" onClick={handleClose}>
      <div className="modal-content task-modal" onClick={(e) => e.stopPropagation()}>
        <div className="modal-header">
          <h3>{isEditing ? '✏️ Edit Task' : '➕ Add New Task'}</h3>
        </div>
        <div className="modal-body">
          <div className="task-form-fields">
            <div className="form-field">
              <label htmlFor="task-title">Task Title *</label>
              <input
                id="task-title"
                type="text"
                placeholder="What needs to be done?"
                value={taskInput}
                onChange={(e) => setTaskInput(e.target.value)}
                disabled={loading}
                className="task-input"
              />
            </div>
            <div className="form-field">
              <label htmlFor="task-description">Description</label>
              <textarea
                id="task-description"
                placeholder="Add more details (optional)"
                value={descriptionInput}
                onChange={(e) => setDescriptionInput(e.target.value)}
                disabled={loading}
                className="task-textarea"
                rows="3"
              />
            </div>
          </div>
        </div>
        <div className="modal-actions">
          <button 
            onClick={handleSubmit} 
            disabled={loading || !taskInput.trim()}
            className="modal-btn save-task-btn"
          >
            {loading ? '⏳ Saving...' : (isEditing ? '💾 Update Task' : '➕ Create Task')}
          </button>
          <button 
            onClick={handleClose} 
            disabled={loading}
            className="modal-btn cancel-btn"
          >
            Cancel
          </button>
        </div>
      </div>
    </div>
  );
}

export default TaskModal;
