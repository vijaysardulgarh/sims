const Dashboard = () => {
  const subjects = [
    "English",
    "Mathematics",
    "Science",
    "Social Science",
    "Punjabi",
  ];

  const assignments = [
    {
      title: "Math Assignment",
      due: "Tomorrow",
    },
    {
      title: "Science Project",
      due: "Friday",
    },
    {
      title: "English Essay",
      due: "Next Week",
    },
  ];

  const notices = [
    "Unit tests will begin from Monday.",
    "Submit science project files before Friday.",
    "Sports meet registration is open.",
  ];

  return (
    <div className="space-y-8">
      {/* Header */}
      <div className="bg-gradient-to-r from-indigo-900 to-blue-700 rounded-3xl p-8 text-white shadow-lg">
        <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-6">
          <div>
            <h1 className="text-4xl font-bold mb-3">
              Student Dashboard
            </h1>

            <p className="text-blue-100 text-lg">
              Welcome back! Stay updated with your academics and activities.
            </p>
          </div>

          <div className="bg-white/10 backdrop-blur-md rounded-2xl px-6 py-4">
            <p className="text-sm text-blue-100">
              Current Class
            </p>

            <h2 className="text-2xl font-bold">
              Class 10 - A
            </h2>
          </div>
        </div>
      </div>

      {/* Statistics */}
      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">
        <div className="bg-white rounded-2xl shadow-md p-6 border border-gray-100">
          <p className="text-gray-500 text-sm mb-2">
            Attendance
          </p>

          <h2 className="text-3xl font-bold text-blue-900">
            94%
          </h2>
        </div>

        <div className="bg-white rounded-2xl shadow-md p-6 border border-gray-100">
          <p className="text-gray-500 text-sm mb-2">
            Subjects
          </p>

          <h2 className="text-3xl font-bold text-green-600">
            5
          </h2>
        </div>

        <div className="bg-white rounded-2xl shadow-md p-6 border border-gray-100">
          <p className="text-gray-500 text-sm mb-2">
            Assignments
          </p>

          <h2 className="text-3xl font-bold text-orange-500">
            3
          </h2>
        </div>

        <div className="bg-white rounded-2xl shadow-md p-6 border border-gray-100">
          <p className="text-gray-500 text-sm mb-2">
            Overall Grade
          </p>

          <h2 className="text-3xl font-bold text-purple-700">
            A+
          </h2>
        </div>
      </div>

      {/* Main Section */}
      <div className="grid grid-cols-1 xl:grid-cols-3 gap-6">
        {/* Subjects */}
        <div className="bg-white rounded-2xl shadow-md p-6">
          <div className="flex items-center justify-between mb-6">
            <h2 className="text-2xl font-bold text-gray-800">
              My Subjects
            </h2>

            <button className="text-blue-900 font-medium hover:underline">
              View All
            </button>
          </div>

          <div className="space-y-4">
            {subjects.map((subject, index) => (
              <div
                key={index}
                className="border border-gray-100 rounded-xl p-4 flex items-center justify-between hover:bg-gray-50 transition"
              >
                <span className="font-medium text-gray-700">
                  {subject}
                </span>

                <span className="bg-blue-100 text-blue-900 px-3 py-1 rounded-full text-sm">
                  Active
                </span>
              </div>
            ))}
          </div>
        </div>

        {/* Assignments */}
        <div className="bg-white rounded-2xl shadow-md p-6">
          <div className="flex items-center justify-between mb-6">
            <h2 className="text-2xl font-bold text-gray-800">
              Assignments
            </h2>

            <button className="text-blue-900 font-medium hover:underline">
              View All
            </button>
          </div>

          <div className="space-y-4">
            {assignments.map((assignment, index) => (
              <div
                key={index}
                className="border border-gray-100 rounded-xl p-4 hover:bg-gray-50 transition"
              >
                <h3 className="font-semibold text-gray-700 mb-2">
                  {assignment.title}
                </h3>

                <p className="text-sm text-gray-500">
                  Due: {assignment.due}
                </p>
              </div>
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

      {/* Attendance + Performance */}
      <div className="grid grid-cols-1 xl:grid-cols-2 gap-6">
        {/* Attendance */}
        <div className="bg-white rounded-2xl shadow-md p-6">
          <h2 className="text-2xl font-bold text-gray-800 mb-6">
            Attendance Overview
          </h2>

          <div className="space-y-5">
            <div>
              <div className="flex justify-between mb-2">
                <span className="text-gray-700 font-medium">
                  Monthly Attendance
                </span>

                <span className="text-blue-900 font-semibold">
                  94%
                </span>
              </div>

              <div className="w-full bg-gray-200 rounded-full h-3">
                <div className="bg-blue-900 h-3 rounded-full w-[94%]"></div>
              </div>
            </div>

            <div>
              <div className="flex justify-between mb-2">
                <span className="text-gray-700 font-medium">
                  Assignment Completion
                </span>

                <span className="text-green-600 font-semibold">
                  88%
                </span>
              </div>

              <div className="w-full bg-gray-200 rounded-full h-3">
                <div className="bg-green-500 h-3 rounded-full w-[88%]"></div>
              </div>
            </div>
          </div>
        </div>

        {/* Performance */}
        <div className="bg-white rounded-2xl shadow-md p-6">
          <h2 className="text-2xl font-bold text-gray-800 mb-6">
            Performance Overview
          </h2>

          <div className="space-y-5">
            <div className="border border-gray-100 rounded-xl p-5">
              <div className="flex justify-between mb-3">
                <span className="font-medium text-gray-700">
                  Mathematics
                </span>

                <span className="text-green-600 font-semibold">
                  92%
                </span>
              </div>

              <div className="w-full bg-gray-200 rounded-full h-3">
                <div className="bg-green-500 h-3 rounded-full w-[92%]"></div>
              </div>
            </div>

            <div className="border border-gray-100 rounded-xl p-5">
              <div className="flex justify-between mb-3">
                <span className="font-medium text-gray-700">
                  Science
                </span>

                <span className="text-blue-900 font-semibold">
                  89%
                </span>
              </div>

              <div className="w-full bg-gray-200 rounded-full h-3">
                <div className="bg-blue-900 h-3 rounded-full w-[89%]"></div>
              </div>
            </div>

            <div className="border border-gray-100 rounded-xl p-5">
              <div className="flex justify-between mb-3">
                <span className="font-medium text-gray-700">
                  English
                </span>

                <span className="text-orange-500 font-semibold">
                  84%
                </span>
              </div>

              <div className="w-full bg-gray-200 rounded-full h-3">
                <div className="bg-orange-400 h-3 rounded-full w-[84%]"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;