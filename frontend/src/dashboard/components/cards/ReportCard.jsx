const ReportCard = ({
    title,
    description,
    icon,
    onClick,
  }) => {
  
    return (
      <div
        className="
          bg-white
          rounded-2xl
          border
          border-slate-100
          shadow-sm
          p-5
          hover:shadow-md
          transition-all
        "
      >
  
        <div className="flex items-start justify-between">
  
          <div>
  
            <h3 className="text-lg font-bold text-slate-800">
              {title}
            </h3>
  
            <p className="text-sm text-slate-500 mt-2">
              {description}
            </p>
  
          </div>
  
          {icon && (
            <div className="text-blue-600">
              {icon}
            </div>
          )}
  
        </div>
  
        <button
          onClick={onClick}
          className="
            mt-5
            text-blue-600
            font-semibold
          "
        >
          Open Report
        </button>
  
      </div>
    );
  };
  
  export default ReportCard;