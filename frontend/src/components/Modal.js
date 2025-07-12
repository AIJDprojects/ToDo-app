// Project     :   Todo List
// Package     :   Modal.js
// Description :   Modal component for the pop ups 
// Modification History:
// *********************************************************
// Date            Author          Modification
// 12-07-2025      jdmunoz         Creation
// *********************************************************

function Modal({ isOpen, onClose, onConfirm, title, message, type = 'confirm' }) {
  if (!isOpen) return null;

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        <div className="modal-header">
          <h3>{title}</h3>
        </div>
        <div className="modal-body">
          <p>{message}</p>
        </div>
        <div className="modal-actions">
          {type === 'confirm' ? (
            <>
              <button onClick={onConfirm} className="modal-btn confirm-btn">
                Yes, Delete
              </button>
              <button onClick={onClose} className="modal-btn cancel-btn">
                Cancel
              </button>
            </>
          ) : (
            <button onClick={onClose} className="modal-btn ok-btn">
              OK
            </button>
          )}
        </div>
      </div>
    </div>
  );
}

export default Modal;
