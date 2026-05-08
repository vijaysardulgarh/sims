const ConfirmModal = ({
    isOpen,
    title,
    message,
    onConfirm,
    onCancel,
  }) => {
  
    if (!isOpen) return null;
  
    return (
  
      <div className="fixed inset-0 bg-black/40 flex items-center justify-center z-50">
  
        <div className="bg-white rounded-2xl shadow-xl w-full max-w-md p-6">
  
          {/* TITLE */}
          <h2 className="text-2xl font-bold text-gray-800">
            {title}
          </h2>
  
          {/* MESSAGE */}
          <p className="text-gray-500 mt-3">
            {message}
          </p>
  
          {/* ACTIONS */}
          <div className="flex justify-end gap-3 mt-6">
  
            <button
              onClick={onCancel}
              className="px-5 py-2 rounded-xl border border-gray-300 hover:bg-gray-100"
            >
              Cancel
            </button>
  
            <button
              onClick={onConfirm}
              className="px-5 py-2 rounded-xl bg-red-600 hover:bg-red-700 text-white"
            >
              Delete
            </button>
  
          </div>
  
        </div>
  
      </div>
  
    );
  
  };
  
  export default ConfirmModal;