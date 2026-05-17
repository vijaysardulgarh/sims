const StatCard = ({
    title,
    value,
    icon,
    color = "bg-blue-500",
    subtitle,
    onClick,
  }) => {
  
    return (
      <div
        onClick={onClick}
        className="
          bg-white
          rounded-2xl
          shadow-sm
          border
          border-slate-100
          p-6
          hover:shadow-lg
          transition-all
          cursor-pointer
        "
      >
  
        <div className="flex items-center justify-between">
  
          <div>
  
            <h3 className="text-sm text-slate-500 mb-2">
              {title}
            </h3>
  
            <p className="text-3xl font-bold text-slate-800">
              {value}
            </p>
  
            {subtitle && (
              <p className="text-xs text-slate-400 mt-2">
                {subtitle}
              </p>
            )}
  
          </div>
  
          {icon && (
            <div
              className={`
                w-14
                h-14
                rounded-2xl
                ${color}
                text-white
                flex
                items-center
                justify-center
              `}
            >
              {icon}
            </div>
          )}
  
        </div>
  
      </div>
    );
  };
  
  export default StatCard;