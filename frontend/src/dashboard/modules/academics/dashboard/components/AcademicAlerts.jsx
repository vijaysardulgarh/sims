const AcademicAlerts = () => {

    const alerts = [
      "2 timetable conflicts detected",
      "5 subjects not assigned",
      "3 sections missing class teacher",
      "1 teacher overload found",
    ];
  
    return (
      <div className="bg-white rounded-2xl shadow-sm border border-red-100 p-6">
  
        <h2 className="text-xl font-bold text-red-600 mb-5">
          Academic Alerts
        </h2>
  
        <div className="space-y-4">
  
          {alerts.map((item, index) => (
            <div
              key={index}
              className="
                bg-red-50
                border
                border-red-100
                rounded-xl
                p-4
                text-red-700
              "
            >
              ⚠ {item}
            </div>
          ))}
  
        </div>
  
      </div>
    );
  };
  
  export default AcademicAlerts;