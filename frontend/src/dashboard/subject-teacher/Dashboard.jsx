const Dashboard = () => {
    return (
      <div className="space-y-6">
  
        <div>
          <h1 className="text-3xl font-bold text-gray-800">
            Subject Teacher Dashboard
          </h1>
  
          <p className="text-gray-500 mt-2">
            Subject teaching and assessments.
          </p>
        </div>
  
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
  
          <div className="bg-white rounded-2xl shadow p-6">
            <p className="text-gray-500">Subjects</p>
            <h2 className="text-3xl font-bold text-blue-700 mt-2">5</h2>
          </div>
  
          <div className="bg-white rounded-2xl shadow p-6">
            <p className="text-gray-500">Assignments</p>
            <h2 className="text-3xl font-bold text-green-600 mt-2">14</h2>
          </div>
  
          <div className="bg-white rounded-2xl shadow p-6">
            <p className="text-gray-500">Tests</p>
            <h2 className="text-3xl font-bold text-purple-700 mt-2">9</h2>
          </div>
  
        </div>
  
      </div>
    );
  };
  
  export default Dashboard;