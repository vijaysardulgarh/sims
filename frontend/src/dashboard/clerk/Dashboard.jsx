const Dashboard = () => {
    return (
      <div className="space-y-6">
  
        <div>
          <h1 className="text-3xl font-bold text-gray-800">
            Clerk Dashboard
          </h1>
  
          <p className="text-gray-500 mt-2">
            Administrative and office operations.
          </p>
        </div>
  
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
  
          <div className="bg-white rounded-2xl shadow p-6">
            <p className="text-gray-500">Admissions</p>
            <h2 className="text-3xl font-bold text-blue-700 mt-2">58</h2>
          </div>
  
          <div className="bg-white rounded-2xl shadow p-6">
            <p className="text-gray-500">Certificates</p>
            <h2 className="text-3xl font-bold text-green-600 mt-2">32</h2>
          </div>
  
          <div className="bg-white rounded-2xl shadow p-6">
            <p className="text-gray-500">Records Updated</p>
            <h2 className="text-3xl font-bold text-orange-500 mt-2">120</h2>
          </div>
  
          <div className="bg-white rounded-2xl shadow p-6">
            <p className="text-gray-500">Reports</p>
            <h2 className="text-3xl font-bold text-purple-700 mt-2">16</h2>
          </div>
  
        </div>
  
      </div>
    );
  };
  
  export default Dashboard;