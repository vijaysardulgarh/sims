const BulkActions = ({
    selectedCount,
    onDelete,
    onSelectAll,
  }) => {
  
    if (selectedCount === 0)
      return null;
  
    return (
  
      <div className="bg-blue-50 border border-blue-200 rounded-xl p-4 flex flex-col md:flex-row items-center justify-between gap-4">
  
        {/* LEFT */}
        <p className="font-medium text-blue-700">
  
          {selectedCount} item(s) selected
  
        </p>
  
        {/* RIGHT */}
        <div className="flex gap-3">
  
          {/* SELECT ALL RECORDS */}
          <button
            onClick={onSelectAll}
            className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg"
          >
            Select All Records
          </button>
  
          {/* DELETE */}
          <button
            onClick={onDelete}
            className="bg-red-600 hover:bg-red-700 text-white px-4 py-2 rounded-lg"
          >
            Delete Selected
          </button>
  
        </div>
  
      </div>
  
    );
  
  };
  
  export default BulkActions;