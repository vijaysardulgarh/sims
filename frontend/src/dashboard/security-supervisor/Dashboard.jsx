const Dashboard = () => {
    return (
      <div className="space-y-6">
  
        <div>
          <h1 className="text-3xl font-bold text-gray-800">
            Security Supervisor Dashboard
          </h1>
  
          <p className="text-gray-500 mt-2">
            Campus security and visitor monitoring.
          </p>
        </div>
  
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
  
          <div className="bg-white rounded-2xl shadow p-6">
            <p className="text-gray-500">Visitors Today</p>
            <h2 className="text-3xl font-bold text-blue-700 mt-2">48</h2>
          </div>
  
          <div className="bg-white rounded-2xl shadow p-6">
            <p className="text-gray-500">Gate Entries</p>
            <h2 className="text-3xl font-bold text-green-600 mt-2">320</h2>
          </div>
  
          <div className="bg-white rounded-2xl shadow p-6">
            <p className="text-gray-500">Incidents</p>
            <h2 className="text-3xl font-bold text-orange-500 mt-2">2</h2>
          </div>
  
          <div className="bg-white rounded-2xl shadow p-6">
            <p className="text-gray-500">Vehicles</p>
            <h2 className="text-3xl font-bold text-purple-700 mt-2">56</h2>
          </div>
  
        </div>
  
      </div>
    );
  };
  
  export default Dashboard;