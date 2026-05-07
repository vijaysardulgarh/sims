const Dashboard = () => {
    const stats = [
      {
        title: "Total Schools",
        value: "48",
        color: "text-blue-700",
        bg: "bg-blue-100",
        icon: "🏫",
      },
      {
        title: "Clusters",
        value: "6",
        color: "text-green-600",
        bg: "bg-green-100",
        icon: "🌐",
      },
      {
        title: "Total Students",
        value: "52,480",
        color: "text-orange-500",
        bg: "bg-orange-100",
        icon: "🎓",
      },
      {
        title: "Revenue",
        value: "₹24L",
        color: "text-purple-700",
        bg: "bg-purple-100",
        icon: "💰",
      },
    ];
  
    return (
      <div className="space-y-8">
  
        {/* Header */}
        <div className="bg-gradient-to-r from-indigo-900 to-blue-800 rounded-3xl p-8 text-white shadow-lg">
  
          <div className="flex items-center justify-between flex-wrap gap-6">
  
            <div>
  
              <h1 className="text-4xl font-bold mb-3">
                Super Admin Dashboard
              </h1>
  
              <p className="text-blue-100 text-lg">
                Manage all schools, clusters, subscriptions, and platform analytics.
              </p>
  
            </div>
  
            <div className="bg-white/10 px-6 py-4 rounded-2xl backdrop-blur-md">
  
              <p className="text-sm text-blue-100">
                Platform Status
              </p>
  
              <h2 className="text-2xl font-bold">
                Active
              </h2>
  
            </div>
  
          </div>
  
        </div>
  
        {/* Stats */}
        <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">
  
          {stats.map((item, index) => (
            <div
              key={index}
              className="bg-white rounded-2xl shadow-md p-6 border border-gray-100"
            >
  
              <div className="flex items-center justify-between">
  
                <div>
  
                  <p className="text-gray-500 text-sm mb-2">
                    {item.title}
                  </p>
  
                  <h2 className={`text-3xl font-bold ${item.color}`}>
                    {item.value}
                  </h2>
  
                </div>
  
                <div
                  className={`w-16 h-16 rounded-2xl flex items-center justify-center text-3xl ${item.bg}`}
                >
                  {item.icon}
                </div>
  
              </div>
  
            </div>
          ))}
  
        </div>
  
        {/* Main Section */}
        <div className="grid grid-cols-1 xl:grid-cols-3 gap-6">
  
          {/* Quick Actions */}
          <div className="xl:col-span-2 bg-white rounded-2xl shadow-md p-6">
  
            <h2 className="text-2xl font-bold text-gray-800 mb-6">
              Quick Actions
            </h2>
  
            <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
  
              <button className="bg-indigo-900 text-white rounded-2xl p-6 text-left hover:scale-[1.02] transition">
                <h3 className="text-xl font-semibold mb-2">
                  Create School
                </h3>
  
                <p className="text-blue-100 text-sm">
                  Add a new school to the ERP platform.
                </p>
              </button>
  
              <button className="bg-green-600 text-white rounded-2xl p-6 text-left hover:scale-[1.02] transition">
                <h3 className="text-xl font-semibold mb-2">
                  Manage Clusters
                </h3>
  
                <p className="text-green-100 text-sm">
                  Configure school clusters and regions.
                </p>
              </button>
  
              <button className="bg-orange-500 text-white rounded-2xl p-6 text-left hover:scale-[1.02] transition">
                <h3 className="text-xl font-semibold mb-2">
                  Subscriptions
                </h3>
  
                <p className="text-orange-100 text-sm">
                  Manage plans and renewals.
                </p>
              </button>
  
              <button className="bg-purple-700 text-white rounded-2xl p-6 text-left hover:scale-[1.02] transition">
                <h3 className="text-xl font-semibold mb-2">
                  Global Reports
                </h3>
  
                <p className="text-purple-100 text-sm">
                  Access platform-wide analytics.
                </p>
              </button>
  
            </div>
  
          </div>
  
          {/* Notices */}
          <div className="bg-white rounded-2xl shadow-md p-6">
  
            <h2 className="text-2xl font-bold text-gray-800 mb-6">
              Platform Notices
            </h2>
  
            <div className="space-y-4">
  
              <div className="border rounded-xl p-4">
                Server maintenance scheduled tonight.
              </div>
  
              <div className="border rounded-xl p-4">
                3 school subscriptions expiring this week.
              </div>
  
              <div className="border rounded-xl p-4">
                New cluster added successfully.
              </div>
  
            </div>
  
          </div>
  
        </div>
  
      </div>
    );
  };
  
  export default Dashboard;