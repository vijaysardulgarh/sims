const Dashboard = () => {
  const stats = [
    {
      title: "Total Students",
      value: "1,250",
      color: "text-blue-900",
      bg: "bg-blue-100",
      icon: "🎓",
    },
    {
      title: "Total Staff",
      value: "85",
      color: "text-green-600",
      bg: "bg-green-100",
      icon: "👨‍🏫",
    },
    {
      title: "Classes",
      value: "42",
      color: "text-orange-500",
      bg: "bg-orange-100",
      icon: "🏫",
    },
    {
      title: "Attendance",
      value: "94%",
      color: "text-purple-700",
      bg: "bg-purple-100",
      icon: "📊",
    },
  ];

  const quickActions = [
    "Manage Students",
    "Manage Staff",
    "View Reports",
    "Generate Timetable",
  ];

  const notices = [
    "Monthly staff meeting on Friday.",
    "Board examination forms submission begins tomorrow.",
    "Update student attendance before 4 PM.",
    "Academic performance report released.",
  ];

  return (
    <div className="space-y-8">
      {/* Hero Section */}
      <div className="bg-gradient-to-r from-blue-900 to-indigo-800 rounded-3xl p-8 text-white shadow-lg">
        <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-6">
          <div>
            <h1 className="text-4xl font-bold mb-3">
              Admin Dashboard
            </h1>

            <p className="text-blue-100 text-lg">
              Welcome back! Here’s the complete overview of your school management system.
            </p>
          </div>

          <div className="bg-white/10 backdrop-blur-md rounded-2xl px-6 py-4">
            <p className="text-sm text-blue-100">
              Current Session
            </p>

            <h2 className="text-2xl font-bold">
              2025–2026
            </h2>
          </div>
        </div>
      </div>

      {/* Statistics Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">
        {stats.map((item, index) => (
          <div
            key={index}
            className="bg-white rounded-2xl shadow-md border border-gray-100 p-6 hover:shadow-xl transition"
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
        {/* Quick Actions */}
        <div className="xl:col-span-2 bg-white rounded-2xl shadow-md p-6">
          <div className="flex items-center justify-between mb-6">
            <h2 className="text-2xl font-bold text-gray-800">
              Quick Actions
            </h2>

            <button className="text-blue-900 font-medium hover:underline">
              View All
            </button>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
            {quickActions.map((action, index) => (
              <button
                key={index}
                className="bg-gradient-to-r from-blue-900 to-indigo-700 text-white rounded-2xl p-6 text-left hover:scale-[1.02] transition"
              >
                <h3 className="text-xl font-semibold mb-2">
                  {action}
                </h3>

                <p className="text-blue-100 text-sm">
                  Access and manage {action.toLowerCase()}.
                </p>
              </button>
            ))}
          </div>
        </div>

        {/* Notices */}
        <div className="bg-white rounded-2xl shadow-md p-6">
          <div className="flex items-center justify-between mb-6">
            <h2 className="text-2xl font-bold text-gray-800">
              Latest Notices
            </h2>

            <button className="text-blue-900 font-medium hover:underline">
              View All
            </button>
          </div>

          <div className="space-y-4">
            {notices.map((notice, index) => (
              <div
                key={index}
                className="border border-gray-100 rounded-xl p-4 hover:bg-gray-50 transition"
              >
                <div className="flex gap-3">
                  <div className="w-3 h-3 bg-blue-900 rounded-full mt-2"></div>

                  <p className="text-gray-700 text-sm leading-relaxed">
                    {notice}
                  </p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Bottom Section */}
      <div className="grid grid-cols-1 xl:grid-cols-2 gap-6">
        {/* Academic Performance */}
        <div className="bg-white rounded-2xl shadow-md p-6">
          <h2 className="text-2xl font-bold text-gray-800 mb-6">
            Academic Performance
          </h2>

          <div className="space-y-5">
            <div>
              <div className="flex justify-between mb-2">
                <span className="font-medium text-gray-700">
                  Board Results
                </span>

                <span className="font-semibold text-green-600">
                  92%
                </span>
              </div>

              <div className="w-full bg-gray-200 rounded-full h-3">
                <div className="bg-green-500 h-3 rounded-full w-[92%]"></div>
              </div>
            </div>

            <div>
              <div className="flex justify-between mb-2">
                <span className="font-medium text-gray-700">
                  Student Attendance
                </span>

                <span className="font-semibold text-blue-900">
                  94%
                </span>
              </div>

              <div className="w-full bg-gray-200 rounded-full h-3">
                <div className="bg-blue-900 h-3 rounded-full w-[94%]"></div>
              </div>
            </div>

            <div>
              <div className="flex justify-between mb-2">
                <span className="font-medium text-gray-700">
                  Staff Performance
                </span>

                <span className="font-semibold text-orange-500">
                  88%
                </span>
              </div>

              <div className="w-full bg-gray-200 rounded-full h-3">
                <div className="bg-orange-400 h-3 rounded-full w-[88%]"></div>
              </div>
            </div>
          </div>
        </div>

        {/* Recent Activity */}
        <div className="bg-white rounded-2xl shadow-md p-6">
          <h2 className="text-2xl font-bold text-gray-800 mb-6">
            Recent Activity
          </h2>

          <div className="space-y-5">
            <div className="flex items-start gap-4">
              <div className="w-12 h-12 rounded-full bg-blue-100 flex items-center justify-center text-xl">
                👨‍🎓
              </div>

              <div>
                <h3 className="font-semibold text-gray-800">
                  New Student Admission
                </h3>

                <p className="text-sm text-gray-500">
                  12 new admissions completed today.
                </p>
              </div>
            </div>

            <div className="flex items-start gap-4">
              <div className="w-12 h-12 rounded-full bg-green-100 flex items-center justify-center text-xl">
                📋
              </div>

              <div>
                <h3 className="font-semibold text-gray-800">
                  Attendance Updated
                </h3>

                <p className="text-sm text-gray-500">
                  All class attendance reports submitted.
                </p>
              </div>
            </div>

            <div className="flex items-start gap-4">
              <div className="w-12 h-12 rounded-full bg-orange-100 flex items-center justify-center text-xl">
                🏫
              </div>

              <div>
                <h3 className="font-semibold text-gray-800">
                  Timetable Updated
                </h3>

                <p className="text-sm text-gray-500">
                  Weekly timetable generated successfully.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;