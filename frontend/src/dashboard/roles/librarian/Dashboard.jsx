const Dashboard = () => {
    return (
      <div className="space-y-6">
  
        <div>
          <h1 className="text-3xl font-bold text-gray-800">
            Librarian Dashboard
          </h1>
  
          <p className="text-gray-500 mt-2">
            Library and book management.
          </p>
        </div>
  
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
  
          <div className="bg-white rounded-2xl shadow p-6">
            <p className="text-gray-500">Books</p>
            <h2 className="text-3xl font-bold text-blue-700 mt-2">4250</h2>
          </div>
  
          <div className="bg-white rounded-2xl shadow p-6">
            <p className="text-gray-500">Issued</p>
            <h2 className="text-3xl font-bold text-green-600 mt-2">320</h2>
          </div>
  
          <div className="bg-white rounded-2xl shadow p-6">
            <p className="text-gray-500">Returns</p>
            <h2 className="text-3xl font-bold text-orange-500 mt-2">210</h2>
          </div>
  
          <div className="bg-white rounded-2xl shadow p-6">
            <p className="text-gray-500">Pending Fines</p>
            <h2 className="text-3xl font-bold text-purple-700 mt-2">₹8,500</h2>
          </div>
  
        </div>
  
      </div>
    );
  };
  
  export default Dashboard;