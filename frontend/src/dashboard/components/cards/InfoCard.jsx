const InfoCard = ({
    title,
    value,
    description,
    icon,
    color = "bg-blue-500",
    footer,
    onClick,
  }) => {
  
    return (
      <div
        onClick={onClick}
        className="
          bg-white
          rounded-2xl
          border
          border-slate-100
          shadow-sm
          p-6
          hover:shadow-lg
          transition-all
          cursor-pointer
        "
      >
  
        {/* HEADER */}
  
        <div className="flex items-start justify-between">
  
          <div>
  
            <p className="text-sm text-slate-500">
              {title}
            </p>
  
            {value && (
              <h2 className="text-3xl font-bold mt-2 text-slate-800">
                {value}
              </h2>
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
  
        {/* DESCRIPTION */}
  
        {description && (
          <p className="text-sm text-slate-500 mt-4">
            {description}
          </p>
        )}
  
        {/* FOOTER */}
  
        {footer && (
          <div className="mt-5 pt-4 border-t border-slate-100">
  
            {footer}
  
          </div>
        )}
  
      </div>
    );
  };
  
  export default InfoCard;