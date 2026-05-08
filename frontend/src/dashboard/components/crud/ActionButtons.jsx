const ActionButtons = ({
  onView,
  onEdit,
  onDelete,
}) => {

  return (

    <div className="flex gap-2">

      {/* VIEW */}
      <button
        onClick={onView}
        className="bg-blue-600 hover:bg-blue-700 text-white px-3 py-1 rounded-lg text-sm"
      >
        View
      </button>

      {/* EDIT */}
      <button
        onClick={onEdit}
        className="bg-yellow-500 hover:bg-yellow-600 text-white px-3 py-1 rounded-lg text-sm"
      >
        Edit
      </button>

      {/* DELETE */}
      <button
        onClick={onDelete}
        className="bg-red-600 hover:bg-red-700 text-white px-3 py-1 rounded-lg text-sm"
      >
        Delete
      </button>

    </div>

  );

};

export default ActionButtons;