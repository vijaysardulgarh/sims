const Dashboard = () => {
    return (
      <div className="space-y-6">
  
        <div>
          <h1 className="text-3xl font-bold text-gray-800">
            Receptionist Dashboard
          </h1>
  
          <p className="text-gray-500 mt-2">
            Front desk and visitor management.
          </p>
        </div>
  
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
  
          <div className="bg-white rounded-2xl shadow p-6">
            <p className="text-gray-500">Visitors</p>
            <h2 className="text-3xl font-bold text-blue-700 mt-2">85</h2>
          </div>
  
          <div className="bg-white rounded-2xl shadow p-6">
            <p className="text-gray-500">Calls</p>
            <h2 className="text-3xl font-bold text-green-600 mt-2">43</h2>
          </div>
  
          <div className="bg-white rounded-2xl shadow p-6">
            <p className="text-gray-500">Appointments</p>
            <h2 className="text-3xl font-bold text-orange-500 mt-2">12</h2>
          </div>
  
          <div className="bg-white rounded-2xl shadow p-6">
            <p className="text-gray-500">Inquiries</p>
            <h2 className="text-3xl font-bold text-purple-700 mt-2">20</h2>
          </div>
  
        </div>
  
      </div>
    );
  };
  
  export default Dashboard;