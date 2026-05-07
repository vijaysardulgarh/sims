const Dashboard = () => {
    const stats = [
      {
        title: "Schools",
        value: "8",
        color: "text-blue-700",
        bg: "bg-blue-100",
        icon: "🏫",
      },
      {
        title: "Students",
        value: "12,450",
        color: "text-green-600",
        bg: "bg-green-100",
        icon: "🎓",
      },
      {
        title: "Teachers",
        value: "520",
        color: "text-orange-500",
        bg: "bg-orange-100",
        icon: "👨‍🏫",
      },
      {
        title: "Attendance",
        value: "93%",
        color: "text-purple-700",
        bg: "bg-purple-100",
        icon: "📊",
      },
    ];
  
    return (
      <div className="space-y-8">
  
        {/* Header */}
        <div className="bg-gradient-to-r from-green-700 to-emerald-600 rounded-3xl p-8 text-white shadow-lg">
  
          <div className="flex items-center justify-between flex-wrap gap-6">
  
            <div>
  
              <h1 className="text-4xl font-bold mb-3">
                Cluster Admin Dashboard
              </h1>
  
              <p className="text-green-100 text-lg">
                Monitor cluster schools, academics, attendance, and performance.
              </p>
  
            </div>
  
            <div className="bg-white/10 px-6 py-4 rounded-2xl backdrop-blur-md">
  
              <p className="text-sm text-green-100">
                Active Cluster
              </p>
  
              <h2 className="text-2xl font-bold">
                Punjab Cluster
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
  
        {/* Main Grid */}
        <div className="grid grid-cols-1 xl:grid-cols-3 gap-6">
  
          {/* Schools */}
          <div className="xl:col-span-2 bg-white rounded-2xl shadow-md p-6">
  
            <h2 className="text-2xl font-bold text-gray-800 mb-6">
              Cluster Schools
            </h2>
  
            <div className="space-y-4">
  
              <div className="border rounded-xl p-5 flex justify-between items-center">
                <div>
                  <h3 className="font-semibold text-lg">
                    ABC Public School
                  </h3>
  
                  <p className="text-gray-500 text-sm">
                    2,450 Students
                  </p>
                </div>
  
                <span className="bg-green-100 text-green-700 px-4 py-2 rounded-full text-sm">
                  Active
                </span>
              </div>
  
              <div className="border rounded-xl p-5 flex justify-between items-center">
                <div>
                  <h3 className="font-semibold text-lg">
                    XYZ Senior Secondary School
                  </h3>
  
                  <p className="text-gray-500 text-sm">
                    1,980 Students
                  </p>
                </div>
  
                <span className="bg-green-100 text-green-700 px-4 py-2 rounded-full text-sm">
                  Active
                </span>
              </div>
  
            </div>
  
          </div>
  
          {/* Notices */}
          <div className="bg-white rounded-2xl shadow-md p-6">
  
            <h2 className="text-2xl font-bold text-gray-800 mb-6">
              Notices
            </h2>
  
            <div className="space-y-4">
  
              <div className="border rounded-xl p-4">
                Cluster-level meeting on Friday.
              </div>
  
              <div className="border rounded-xl p-4">
                Attendance performance improved by 4%.
              </div>
  
              <div className="border rounded-xl p-4">
                Annual inspections begin next month.
              </div>
  
            </div>
  
          </div>
  
        </div>
  
      </div>
    );
  };
  
  export default Dashboard;