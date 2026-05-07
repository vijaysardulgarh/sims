const Dashboard = () => {
    return (
      <div className="space-y-6">
  
        <div>
  
          <h1 className="text-3xl font-bold text-gray-800">
            Parent Dashboard
          </h1>
  
          <p className="text-gray-500 mt-2">
            Monitor your child academic performance and activities.
          </p>
  
        </div>
  
        <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">
  
          <div className="bg-white rounded-2xl shadow p-6">
  
            <p className="text-gray-500">
              Attendance
            </p>
  
            <h2 className="text-3xl font-bold text-blue-700 mt-2">
              94%
            </h2>
  
          </div>
  
          <div className="bg-white rounded-2xl shadow p-6">
  
            <p className="text-gray-500">
              Homework
            </p>
  
            <h2 className="text-3xl font-bold text-green-600 mt-2">
              12
            </h2>
  
          </div>
  
          <div className="bg-white rounded-2xl shadow p-6">
  
            <p className="text-gray-500">
              Fees Due
            </p>
  
            <h2 className="text-3xl font-bold text-orange-500 mt-2">
              ₹5,000
            </h2>
  
          </div>
  
          <div className="bg-white rounded-2xl shadow p-6">
  
            <p className="text-gray-500">
              Messages
            </p>
  
            <h2 className="text-3xl font-bold text-purple-700 mt-2">
              3
            </h2>
  
          </div>
  
        </div>
  
      </div>
    );
  };
  
  export default Dashboard;