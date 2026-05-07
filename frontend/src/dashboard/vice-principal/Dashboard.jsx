const Dashboard = () => {
    return (
      <div className="space-y-6">
  
        <div>
          <h1 className="text-3xl font-bold text-gray-800">
            Vice Principal Dashboard
          </h1>
  
          <p className="text-gray-500 mt-2">
            School operations and discipline monitoring.
          </p>
        </div>
  
        <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">
  
          <div className="bg-white p-6 rounded-2xl shadow">
            <p className="text-gray-500">
              Attendance
            </p>
  
            <h2 className="text-3xl font-bold text-blue-700 mt-2">
              94%
            </h2>
          </div>
  
          <div className="bg-white p-6 rounded-2xl shadow">
            <p className="text-gray-500">
              Discipline Cases
            </p>
  
            <h2 className="text-3xl font-bold text-red-600 mt-2">
              12
            </h2>
          </div>
  
          <div className="bg-white p-6 rounded-2xl shadow">
            <p className="text-gray-500">
              Meetings
            </p>
  
            <h2 className="text-3xl font-bold text-green-600 mt-2">
              5
            </h2>
          </div>
  
          <div className="bg-white p-6 rounded-2xl shadow">
            <p className="text-gray-500">
              Reports
            </p>
  
            <h2 className="text-3xl font-bold text-purple-700 mt-2">
              18
            </h2>
          </div>
  
        </div>
  
      </div>
    );
  };
  
  export default Dashboard;