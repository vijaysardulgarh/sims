const Dashboard = () => {
    return (
      <div className="space-y-6">
  
        <div>
          <h1 className="text-3xl font-bold text-gray-800">
            Accountant Dashboard
          </h1>
  
          <p className="text-gray-500 mt-2">
            School finance and fee management.
          </p>
        </div>
  
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
  
          <div className="bg-white rounded-2xl shadow p-6">
            <p className="text-gray-500">Fee Collection</p>
            <h2 className="text-3xl font-bold text-blue-700 mt-2">₹4.5L</h2>
          </div>
  
          <div className="bg-white rounded-2xl shadow p-6">
            <p className="text-gray-500">Pending Fees</p>
            <h2 className="text-3xl font-bold text-red-600 mt-2">₹1.2L</h2>
          </div>
  
          <div className="bg-white rounded-2xl shadow p-6">
            <p className="text-gray-500">Receipts</p>
            <h2 className="text-3xl font-bold text-green-600 mt-2">620</h2>
          </div>
  
          <div className="bg-white rounded-2xl shadow p-6">
            <p className="text-gray-500">Concessions</p>
            <h2 className="text-3xl font-bold text-purple-700 mt-2">18</h2>
          </div>
  
        </div>
  
      </div>
    );
  };
  
  export default Dashboard;