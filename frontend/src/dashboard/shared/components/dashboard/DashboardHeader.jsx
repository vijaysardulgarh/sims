const DashboardHeader = ({
    title,
    subtitle,
    actionButton,
  }) => {
  
    return (
      <div
        className="
          flex
          flex-col
          xl:flex-row
          xl:items-center
          justify-between
          gap-4
        "
      >
  
        <div>
  
          <h1 className="text-3xl font-bold text-slate-800">
            {title}
          </h1>
  
          {subtitle && (
            <p className="text-slate-500 mt-1">
              {subtitle}
            </p>
          )}
  
        </div>
  
        {actionButton && (
          <div>
            {actionButton}
          </div>
        )}
  
      </div>
    );
  };
  
  export default DashboardHeader;