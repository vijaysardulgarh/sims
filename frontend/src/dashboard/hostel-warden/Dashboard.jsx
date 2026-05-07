const Dashboard = () => {
    return (
      <div className="space-y-6">
  
        <div>
          <h1 className="text-3xl font-bold text-gray-800">
            Hostel Warden Dashboard
          </h1>
  
          <p className="text-gray-500 mt-2">
            Hostel management and student monitoring.
          </p>
        </div>
  
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
  
          <div className="bg-white rounded-2xl shadow p-6">
            <p className="text-gray-500">Hostel Rooms</p>
            <h2 className="text-3xl font-bold text-blue-700 mt-2">120</h2>
          </div>
  
          <div className="bg-white rounded-2xl shadow p-6">
            <p className="text-gray-500">Students</p>
            <h2 className="text-3xl font-bold text-green-600 mt-2">340</h2>
          </div>
  
          <div className="bg-white rounded-2xl shadow p-6">
            <p className="text-gray-500">Attendance</p>
            <h2 className="text-3xl font-bold text-orange-500 mt-2">97%</h2>
          </div>
  
          <div className="bg-white rounded-2xl shadow p-6">
            <p className="text-gray-500">Discipline Cases</p>
            <h2 className="text-3xl font-bold text-purple-700 mt-2">5</h2>
          </div>
  
        </div>
  
      </div>
    );
  };
  
  export default Dashboard;