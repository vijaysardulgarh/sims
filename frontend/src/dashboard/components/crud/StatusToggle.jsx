const StatusToggle = ({
  status,
  onToggle,
}) => {

  return (

    <button
      onClick={onToggle}
      className={`px-3 py-1 rounded-full text-sm font-medium transition

        ${
          status === "Active"
            ? "bg-green-100 text-green-700 hover:bg-green-200"
            : "bg-red-100 text-red-700 hover:bg-red-200"
        }
      `}
    >

      {status}

    </button>

  );

};

export default StatusToggle;