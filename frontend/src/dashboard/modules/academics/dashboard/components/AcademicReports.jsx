const AcademicReports = () => {

    const reports = [
      {
        title: "Student Strength",
        description: "Class wise student strength report",
      },
      {
        title: "Subject Strength",
        description: "Subject enrollment analytics",
      },
      {
        title: "Teacher Workload",
        description: "Teacher period workload analysis",
      },
      {
        title: "Class Incharge",
        description: "Class teacher assignment report",
      },
    ];
  
    return (
      <div className="space-y-5">
  
        <div className="flex items-center justify-between">
  
          <h2 className="text-2xl font-bold text-slate-800">
            Academic Reports
          </h2>
  
        </div>
  
        <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">
  
          {reports.map((item, index) => (
  
            <div
              key={index}
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
  
              <h3 className="text-lg font-bold text-slate-800">
                {item.title}
              </h3>
  
              <p className="text-sm text-slate-500 mt-2">
                {item.description}
              </p>
  
              <button
                className="
                  mt-5
                  text-blue-600
                  font-semibold
                "
              >
                Open Report
              </button>
  
            </div>
  
          ))}
  
        </div>
  
      </div>
    );
  };
  
  export default AcademicReports;