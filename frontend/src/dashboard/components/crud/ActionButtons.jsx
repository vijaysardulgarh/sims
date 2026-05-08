const ActionButtons = () => {

  return (

    <div className="flex gap-2">

      <button className="bg-blue-600 text-white px-3 py-1 rounded-lg">
        View
      </button>

      <button className="bg-yellow-500 text-white px-3 py-1 rounded-lg">
        Edit
      </button>

      <button className="bg-red-600 text-white px-3 py-1 rounded-lg">
        Delete
      </button>

    </div>

  );

};

export default ActionButtons;