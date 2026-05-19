const Dashboard = () => {
  const classes = [
    {
      className: "10-A",
      subject: "Mathematics",
      period: "1st Period",
    },
    {
      className: "9-B",
      subject: "Science",
      period: "3rd Period",
    },
    {
      className: "8-A",
      subject: "Mathematics",
      period: "5th Period",
    },
  ];

  const assignments = [
    "Check Class 10 Mathematics notebooks",
    "Prepare unit test question paper",
    "Upload attendance report",
    "Complete internal assessment marks",
  ];

  const notices = [
    "Staff meeting tomorrow at 1:30 PM",
    "Submit lesson plans before Friday",
    "Practical examination duty list uploaded",
  ];

  return (
    <div className="space-y-8">
      {/* Header */}
      <div className="bg-gradient-to-r from-green-700 to-emerald-600 rounded-3xl p-8 text-white shadow-lg">
        <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-6">
          <div>
            <h1 className="text-4xl font-bold mb-3">
              Teacher Dashboard
            </h1>

            <p className="text-green-100 text-lg">
              Welcome back! Manage your classes, attendance, and assignments efficiently.
            </p>
          </div>

          <div className="bg-white/10 backdrop-blur-md rounded-2xl px-6 py-4">
            <p className="text-sm text-green-100">
              Today’s Classes
            </p>

            <h2 className="text-3xl font-bold">
              6
            </h2>
          </div>
        </div>
      </div>

      {/* Stats */}
      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">
        <div className="bg-white rounded-2xl shadow-md p-6 border border-gray-100">
          <p className="text-gray-500 text-sm mb-2">
            Total Classes
          </p>

          <h2 className="text-3xl font-bold text-green-700">
            18
          </h2>
        </div>

        <div className="bg-white rounded-2xl shadow-md p-6 border border-gray-100">
          <p className="text-gray-500 text-sm mb-2">
            Students
          </p>

          <h2 className="text-3xl font-bold text-blue-900">
            420
          </h2>
        </div>

        <div className="bg-white rounded-2xl shadow-md p-6 border border-gray-100">
          <p className="text-gray-500 text-sm mb-2">
            Attendance Submitted
          </p>

          <h2 className="text-3xl font-bold text-orange-500">
            92%
          </h2>
        </div>

        <div className="bg-white rounded-2xl shadow-md p-6 border border-gray-100">
          <p className="text-gray-500 text-sm mb-2">
            Pending Tasks
          </p>

          <h2 className="text-3xl font-bold text-red-500">
            4
          </h2>
        </div>
      </div>

      {/* Main Grid */}
      <div className="grid grid-cols-1 xl:grid-cols-3 gap-6">
        {/* Today's Schedule */}
        <div className="xl:col-span-2 bg-white rounded-2xl shadow-md p-6">
          <div className="flex items-center justify-between mb-6">
            <h2 className="text-2xl font-bold text-gray-800">
              Today’s Schedule
            </h2>

            <button className="text-green-700 font-medium hover:underline">
              View Full Timetable
            </button>
          </div>

          <div className="space-y-4">
            {classes.map((item, index) => (
              <div
                key={index}
                className="border border-gray-100 rounded-2xl p-5 hover:bg-gray-50 transition"
              >
                <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
                  <div>
                    <h3 className="text-xl font-semibold text-gray-800">
                      {item.className}
                    </h3>

                    <p className="text-gray-500">
                      Subject: {item.subject}
                    </p>
                  </div>

                  <div className="bg-green-100 text-green-800 px-4 py-2 rounded-full font-medium">
                    {item.period}
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Notices */}
        <div className="bg-white rounded-2xl shadow-md p-6">
          <div className="flex items-center justify-between mb-6">
            <h2 className="text-2xl font-bold text-gray-800">
              Notices
            </h2>

            <button className="text-green-700 font-medium hover:underline">
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
                  <div className="w-3 h-3 bg-green-700 rounded-full mt-2"></div>

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
        {/* Tasks */}
        <div className="bg-white rounded-2xl shadow-md p-6">
          <div className="flex items-center justify-between mb-6">
            <h2 className="text-2xl font-bold text-gray-800">
              Pending Tasks
            </h2>

            <button className="text-green-700 font-medium hover:underline">
              Manage Tasks
            </button>
          </div>

          <div className="space-y-4">
            {assignments.map((task, index) => (
              <div
                key={index}
                className="flex items-center justify-between border border-gray-100 rounded-xl p-4 hover:bg-gray-50 transition"
              >
                <div className="flex items-center gap-3">
                  <div className="w-4 h-4 border-2 border-green-700 rounded"></div>

                  <p className="text-gray-700">
                    {task}
                  </p>
                </div>

                <button className="text-sm bg-green-700 hover:bg-green-600 text-white px-3 py-1 rounded-lg transition">
                  Done
                </button>
              </div>
            ))}
          </div>
        </div>

        {/* Attendance Overview */}
        <div className="bg-white rounded-2xl shadow-md p-6">
          <h2 className="text-2xl font-bold text-gray-800 mb-6">
            Attendance Overview
          </h2>

          <div className="space-y-5">
            <div>
              <div className="flex justify-between mb-2">
                <span className="font-medium text-gray-700">
                  Class 10-A
                </span>

                <span className="font-semibold text-green-700">
                  96%
                </span>
              </div>

              <div className="w-full bg-gray-200 rounded-full h-3">
                <div className="bg-green-600 h-3 rounded-full w-[96%]"></div>
              </div>
            </div>

            <div>
              <div className="flex justify-between mb-2">
                <span className="font-medium text-gray-700">
                  Class 9-B
                </span>

                <span className="font-semibold text-blue-900">
                  91%
                </span>
              </div>

              <div className="w-full bg-gray-200 rounded-full h-3">
                <div className="bg-blue-900 h-3 rounded-full w-[91%]"></div>
              </div>
            </div>

            <div>
              <div className="flex justify-between mb-2">
                <span className="font-medium text-gray-700">
                  Class 8-A
                </span>

                <span className="font-semibold text-orange-500">
                  87%
                </span>
              </div>

              <div className="w-full bg-gray-200 rounded-full h-3">
                <div className="bg-orange-400 h-3 rounded-full w-[87%]"></div>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Quick Actions */}
      <div className="bg-white rounded-2xl shadow-md p-6">
        <h2 className="text-2xl font-bold text-gray-800 mb-6">
          Quick Actions
        </h2>

        <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-5">
          <button className="bg-green-700 hover:bg-green-600 text-white rounded-2xl p-5 text-left transition">
            <h3 className="font-bold text-lg mb-2">
              Take Attendance
            </h3>

            <p className="text-sm text-green-100">
              Mark student attendance quickly.
            </p>
          </button>

          <button className="bg-blue-900 hover:bg-blue-800 text-white rounded-2xl p-5 text-left transition">
            <h3 className="font-bold text-lg mb-2">
              Upload Marks
            </h3>

            <p className="text-sm text-blue-100">
              Submit examination marks and grades.
            </p>
          </button>

          <button className="bg-orange-500 hover:bg-orange-400 text-white rounded-2xl p-5 text-left transition">
            <h3 className="font-bold text-lg mb-2">
              Assign Homework
            </h3>

            <p className="text-sm text-orange-100">
              Share assignments with students.
            </p>
          </button>

          <button className="bg-purple-700 hover:bg-purple-600 text-white rounded-2xl p-5 text-left transition">
            <h3 className="font-bold text-lg mb-2">
              View Timetable
            </h3>

            <p className="text-sm text-purple-100">
              Access your daily class schedule.
            </p>
          </button>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;