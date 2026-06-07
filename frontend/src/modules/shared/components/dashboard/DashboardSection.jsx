const DashboardSection = ({
    title,
    subtitle,
    action,
    children,
  }) => {
  
    return (
      <div
        className="
          bg-white
          rounded-2xl
          border
          border-slate-100
          shadow-sm
          p-6
        "
      >
  
        {/* HEADER */}
  
        {(title || action) && (
  
          <div className="flex items-start justify-between mb-6">
  
            <div>
  
              {title && (
                <h2 className="text-xl font-bold text-slate-800">
                  {title}
                </h2>
              )}
  
              {subtitle && (
                <p className="text-sm text-slate-500 mt-1">
                  {subtitle}
                </p>
              )}
  
            </div>
  
            {action && (
              <div>
                {action}
              </div>
            )}
  
          </div>
  
        )}
  
        {/* BODY */}
  
        <div>
          {children}
        </div>
  
      </div>
    );
  };
  
  export default DashboardSection;