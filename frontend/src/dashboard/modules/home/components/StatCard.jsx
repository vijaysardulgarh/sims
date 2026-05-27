const StatCard = ({

    title,
  
    value,
  
  }) => {
  
    return (
  
      <div
        className="
          bg-white
          rounded-2xl
          shadow-sm
          p-6
        "
      >
  
        <p className="text-gray-500 text-sm">
  
          {title}
  
        </p>
  
        <h2
          className="
            text-3xl
            font-bold
            text-gray-800
            mt-2
          "
        >
  
          {value}
  
        </h2>
  
      </div>
    );
  };
  
  export default StatCard;