const DashboardGrid = ({
    children,
    cols = "grid-cols-1 md:grid-cols-2 xl:grid-cols-4",
    gap = "gap-6",
  }) => {
  
    return (
      <div
        className={`
          grid
          ${cols}
          ${gap}
        `}
      >
        {children}
      </div>
    );
  };
  
  export default DashboardGrid;