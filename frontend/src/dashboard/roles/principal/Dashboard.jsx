const Dashboard = () => {
  const stats = [
    {
      title: "Total Students",
      value: "1,248",
      icon: "🎓",
    },
    {
      title: "Teaching Staff",
      value: "86",
      icon: "👨‍🏫",
    },
    {
      title: "Attendance",
      value: "94%",
      icon: "📊",
    },
    {
      title: "Classes Running",
      value: "42",
      icon: "🏫",
    },
  ];

  const notices = [
    "PTM scheduled on Saturday at 10:00 AM",
    "Board practical exams begin next week",
    "Submit monthly academic reports before Friday",
    "Staff meeting tomorrow at 1:30 PM",
  ];

  return (
    <div className="space-y-8">
      {/* Header */}
      <div className="bg-gradient-to-r from-blue-900 to-blue-700 rounded-3xl p-8 text-white shadow-lg">
        <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-6">
          <div>
            <h1 className="text-4xl font-bold mb-3">
              Principal Dashboard
            </h1>

            <p className="text-blue-100 text-lg">
              Welcome back! Here’s the latest overview of your school.
            </p>
          </div>

          <div className="bg-white/10 backdrop-blur-md rounded-2xl px-6 py-4">
            <p className="text-sm text-blue-100">Current Session</p>
            <h2 className="text-2xl font-bold">2025–2026</h2>
          </div>
        </div>
      </div>

      {/* Statistics */}
      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">
        {stats.map((item, index) => (
          <div
            key={index}
            className="bg-white rounded-2xl shadow-md p-6 border border-gray-100 hover:shadow-xl transition"
          >
            <div className="flex items-center justify-between">
              <div>
                <p className="text-gray-500 text-sm mb-2">
                  {item.title}
                </p>

                <h3 className="text-3xl font-bold text-gray-800">
                  {item.value}
                </h3>
              </div>

              <div className="text-4xl">
                {item.icon}
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* Main Content */}
      <div className="grid grid-cols-1 xl:grid-cols-3 gap-6">
        {/* Academic Overview */}
        <div className="xl:col-span-2 bg-white rounded-2xl shadow-md p-6">
          <div className="flex items-center justify-between mb-6">
            <h2 className="text-2xl font-bold text-gray-800">
              Academic Overview
            </h2>

            <button className="bg-blue-900 hover:bg-blue-800 text-white px-4 py-2 rounded-xl transition">
              View Reports
            </button>
          </div>

          <div className="space-y-5">
            <div className="border border-gray-100 rounded-xl p-5">
              <div className="flex items-center justify-between mb-3">
                <h3 className="font-semibold text-gray-700">
                  Board Classes Performance
                </h3>

                <span className="text-green-600 font-semibold">
                  +8%
                </span>
              </div>

              <div className="w-full bg-gray-200 rounded-full h-3">
                <div className="bg-blue-900 h-3 rounded-full w-[82%]"></div>
              </div>

              <p className="text-sm text-gray-500 mt-2">
                Overall performance improvement this month.
              </p>
            </div>

            <div className="border border-gray-100 rounded-xl p-5">
              <div className="flex items-center justify-between mb-3">
                <h3 className="font-semibold text-gray-700">
                  Student Attendance
                </h3>

                <span className="text-blue-700 font-semibold">
                  94%
                </span>
              </div>

              <div className="w-full bg-gray-200 rounded-full h-3">
                <div className="bg-green-500 h-3 rounded-full w-[94%]"></div>
              </div>

              <p className="text-sm text-gray-500 mt-2">
                Excellent attendance maintained this week.
              </p>
            </div>

            <div className="border border-gray-100 rounded-xl p-5">
              <div className="flex items-center justify-between mb-3">
                <h3 className="font-semibold text-gray-700">
                  Staff Completion Reports
                </h3>

                <span className="text-orange-500 font-semibold">
                  76%
                </span>
              </div>

              <div className="w-full bg-gray-200 rounded-full h-3">
                <div className="bg-orange-400 h-3 rounded-full w-[76%]"></div>
              </div>

              <p className="text-sm text-gray-500 mt-2">
                Pending reports need review before Friday.
              </p>
            </div>
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

      {/* Bottom Quick Actions */}
      <div className="bg-white rounded-2xl shadow-md p-6">
        <h2 className="text-2xl font-bold text-gray-800 mb-6">
          Quick Actions
        </h2>

        <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-5">
          <button className="bg-blue-900 hover:bg-blue-800 text-white rounded-2xl p-5 text-left transition">
            <h3 className="font-bold text-lg mb-2">
              Student Reports
            </h3>

            <p className="text-sm text-blue-100">
              View and download academic reports.
            </p>
          </button>

          <button className="bg-green-600 hover:bg-green-500 text-white rounded-2xl p-5 text-left transition">
            <h3 className="font-bold text-lg mb-2">
              Attendance Review
            </h3>

            <p className="text-sm text-green-100">
              Monitor attendance statistics quickly.
            </p>
          </button>

          <button className="bg-orange-500 hover:bg-orange-400 text-white rounded-2xl p-5 text-left transition">
            <h3 className="font-bold text-lg mb-2">
              Staff Management
            </h3>

            <p className="text-sm text-orange-100">
              Manage staff workload and schedules.
            </p>
          </button>

          <button className="bg-purple-700 hover:bg-purple-600 text-white rounded-2xl p-5 text-left transition">
            <h3 className="font-bold text-lg mb-2">
              Timetable
            </h3>

            <p className="text-sm text-purple-100">
              Check and manage class schedules.
            </p>
          </button>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;