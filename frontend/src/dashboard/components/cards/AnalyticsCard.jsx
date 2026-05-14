const AnalyticsCard = ({
    title,
    value,
    percentage,
    trend = "up",
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
  
        <div className="flex items-center justify-between">
  
          <div>
  
            <p className="text-sm text-slate-500">
              {title}
            </p>
  
            <h2 className="text-3xl font-bold mt-2 text-slate-800">
              {value}
            </h2>
  
          </div>
  
          <div
            className={`
              px-3
              py-1
              rounded-full
              text-sm
              font-semibold
              ${
                trend === "up"
                  ? "bg-green-100 text-green-700"
                  : "bg-red-100 text-red-700"
              }
            `}
          >
            {percentage}
          </div>
  
        </div>
  
      </div>
    );
  };
  
  export default AnalyticsCard;