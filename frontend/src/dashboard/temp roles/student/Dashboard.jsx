import {
  Bell,
  BookOpen,
  Bus,
  Calendar,
  CheckCircle2,
  Clock3,
  CreditCard,
  Download,
  FileText,
  GraduationCap,
  Trophy,
  UserCircle2,
  Video,
} from "lucide-react";

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
      status: "Pending",
    },
    {
      title: "Science Project",
      due: "Friday",
      status: "Submitted",
    },
    {
      title: "English Essay",
      due: "Next Week",
      status: "Pending",
    },
  ];

  const notices = [
    {
      title: "Unit Tests",
      message: "Unit tests will begin from Monday.",
      type: "Academic",
    },
    {
      title: "Science Project",
      message: "Submit science project files before Friday.",
      type: "Important",
    },
    {
      title: "Sports Meet",
      message: "Sports meet registration is open.",
      type: "Sports",
    },
  ];

  const timetable = [
    {
      subject: "Mathematics",
      teacher: "Mr. Sharma",
      time: "09:00 - 09:45",
      room: "Room 12",
      current: true,
    },
    {
      subject: "Science",
      teacher: "Mrs. Kaur",
      time: "10:00 - 10:45",
      room: "Lab 2",
    },
    {
      subject: "English",
      teacher: "Ms. Verma",
      time: "11:00 - 11:45",
      room: "Room 5",
    },
  ];

  const onlineClasses = [
    {
      subject: "Science Live Class",
      teacher: "Mrs. Kaur",
      time: "5:00 PM",
    },
    {
      subject: "Math Doubt Session",
      teacher: "Mr. Sharma",
      time: "7:00 PM",
    },
  ];

  const resources = [
    "Mathematics Notes PDF",
    "Science Chapter Video",
    "English Grammar Worksheet",
  ];

  const tasks = [
    "Complete Math Homework",
    "Revise Science Chapter 3",
    "Bring Sports Uniform",
  ];

  const libraryBooks = [
    {
      name: "Physics Fundamentals",
      due: "25 May",
    },
    {
      name: "English Literature",
      due: "28 May",
    },
  ];

  const notifications = [
    "New assignment uploaded",
    "Fee due reminder",
    "Tomorrow is Science Test",
  ];

  return (
    <div className="space-y-8">
      {/* Header */}
      <div className="bg-gradient-to-r from-indigo-900 to-blue-700 rounded-3xl p-8 text-white shadow-lg">
        <div className="flex flex-col xl:flex-row xl:items-center xl:justify-between gap-6">
          <div>
            <h1 className="text-4xl font-bold mb-3">
              Student Dashboard
            </h1>

            <p className="text-blue-100 text-lg">
              Welcome back! Stay updated with your academics and activities.
            </p>
          </div>

          <div className="flex gap-4 flex-wrap">
            {/* Notifications */}
            <div className="bg-white/10 backdrop-blur-md rounded-2xl p-4 w-72">
              <div className="flex items-center gap-2 mb-3">
                <Bell size={18} />

                <h2 className="font-semibold">
                  Notifications
                </h2>
              </div>

              <div className="space-y-2">
                {notifications.map((item, index) => (
                  <div
                    key={index}
                    className="text-sm text-blue-100 border-b border-white/10 pb-2"
                  >
                    {item}
                  </div>
                ))}
              </div>
            </div>

            {/* Profile Card */}
            <div className="bg-white text-gray-800 rounded-2xl p-5 w-72 shadow-lg">
              <div className="flex items-center gap-4">
                <UserCircle2
                  size={60}
                  className="text-blue-900"
                />

                <div>
                  <h2 className="font-bold text-lg">
                    Aarav Kumar
                  </h2>

                  <p className="text-sm text-gray-500">
                    Class 10 - A
                  </p>

                  <p className="text-sm text-gray-500">
                    Roll No: 21
                  </p>
                </div>
              </div>

              <button className="mt-5 w-full bg-blue-900 text-white py-2 rounded-xl flex items-center justify-center gap-2 hover:bg-blue-800 transition">
                <Download size={18} />
                Download ID Card
              </button>
            </div>
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

      {/* Timetable + Fees */}
      <div className="grid grid-cols-1 xl:grid-cols-2 gap-6">
        {/* Timetable */}
        <div className="bg-white rounded-2xl shadow-md p-6">
          <div className="flex items-center gap-3 mb-6">
            <Calendar className="text-blue-900" />

            <h2 className="text-2xl font-bold text-gray-800">
              Today's Timetable
            </h2>
          </div>

          <div className="space-y-4">
            {timetable.map((item, index) => (
              <div
                key={index}
                className={`rounded-2xl p-5 border ${
                  item.current
                    ? "bg-blue-50 border-blue-200"
                    : "border-gray-100"
                }`}
              >
                <div className="flex justify-between items-start">
                  <div>
                    <h3 className="font-bold text-gray-800">
                      {item.subject}
                    </h3>

                    <p className="text-sm text-gray-500">
                      {item.teacher}
                    </p>
                  </div>

                  {item.current && (
                    <span className="bg-blue-900 text-white text-xs px-3 py-1 rounded-full">
                      Current
                    </span>
                  )}
                </div>

                <div className="mt-4 flex justify-between text-sm text-gray-600">
                  <span>{item.time}</span>

                  <span>{item.room}</span>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Fee Card */}
        <div className="bg-white rounded-2xl shadow-md p-6">
          <div className="flex items-center gap-3 mb-6">
            <CreditCard className="text-green-600" />

            <h2 className="text-2xl font-bold text-gray-800">
              Fee Status
            </h2>
          </div>

          <div className="space-y-5">
            <div>
              <div className="flex justify-between mb-2">
                <span>Total Fees</span>

                <span className="font-semibold">
                  ₹45,000
                </span>
              </div>

              <div className="flex justify-between mb-2">
                <span>Paid</span>

                <span className="text-green-600 font-semibold">
                  ₹35,000
                </span>
              </div>

              <div className="flex justify-between mb-4">
                <span>Pending</span>

                <span className="text-red-500 font-semibold">
                  ₹10,000
                </span>
              </div>

              <div className="w-full bg-gray-200 rounded-full h-3">
                <div className="bg-green-500 h-3 rounded-full w-[78%]"></div>
              </div>
            </div>

            <div className="flex gap-3">
              <button className="flex-1 bg-blue-900 text-white py-3 rounded-xl hover:bg-blue-800 transition">
                Pay Now
              </button>

              <button className="flex-1 border border-gray-300 py-3 rounded-xl hover:bg-gray-50 transition">
                Receipt
              </button>
            </div>
          </div>
        </div>
      </div>

      {/* Main Grid */}
      <div className="grid grid-cols-1 xl:grid-cols-3 gap-6">
        {/* Subjects */}
        <div className="bg-white rounded-2xl shadow-md p-6">
          <div className="flex items-center gap-3 mb-6">
            <BookOpen className="text-blue-900" />

            <h2 className="text-2xl font-bold text-gray-800">
              My Subjects
            </h2>
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
          <div className="flex items-center gap-3 mb-6">
            <FileText className="text-orange-500" />

            <h2 className="text-2xl font-bold text-gray-800">
              Assignments
            </h2>
          </div>

          <div className="space-y-4">
            {assignments.map((assignment, index) => (
              <div
                key={index}
                className="border border-gray-100 rounded-xl p-4"
              >
                <div className="flex justify-between mb-2">
                  <h3 className="font-semibold text-gray-700">
                    {assignment.title}
                  </h3>

                  <span
                    className={`text-xs px-3 py-1 rounded-full ${
                      assignment.status === "Submitted"
                        ? "bg-green-100 text-green-700"
                        : "bg-orange-100 text-orange-700"
                    }`}
                  >
                    {assignment.status}
                  </span>
                </div>

                <p className="text-sm text-gray-500">
                  Due: {assignment.due}
                </p>
              </div>
            ))}
          </div>
        </div>

        {/* Announcements */}
        <div className="bg-white rounded-2xl shadow-md p-6">
          <div className="flex items-center gap-3 mb-6">
            <Bell className="text-red-500" />

            <h2 className="text-2xl font-bold text-gray-800">
              Announcements
            </h2>
          </div>

          <div className="space-y-4">
            {notices.map((notice, index) => (
              <div
                key={index}
                className="border border-gray-100 rounded-xl p-4"
              >
                <div className="flex justify-between mb-2">
                  <h3 className="font-semibold text-gray-700">
                    {notice.title}
                  </h3>

                  <span className="bg-blue-100 text-blue-900 text-xs px-3 py-1 rounded-full">
                    {notice.type}
                  </span>
                </div>

                <p className="text-sm text-gray-600">
                  {notice.message}
                </p>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Online Classes + Resources + Tasks */}
      <div className="grid grid-cols-1 xl:grid-cols-3 gap-6">
        {/* Online Classes */}
        <div className="bg-white rounded-2xl shadow-md p-6">
          <div className="flex items-center gap-3 mb-6">
            <Video className="text-purple-700" />

            <h2 className="text-2xl font-bold text-gray-800">
              Online Classes
            </h2>
          </div>

          <div className="space-y-4">
            {onlineClasses.map((item, index) => (
              <div
                key={index}
                className="border border-gray-100 rounded-xl p-4"
              >
                <h3 className="font-semibold text-gray-700">
                  {item.subject}
                </h3>

                <p className="text-sm text-gray-500 mt-1">
                  {item.teacher}
                </p>

                <div className="flex justify-between items-center mt-4">
                  <span className="text-sm text-gray-500">
                    {item.time}
                  </span>

                  <button className="bg-blue-900 text-white px-4 py-2 rounded-lg text-sm hover:bg-blue-800">
                    Join
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Learning Resources */}
        <div className="bg-white rounded-2xl shadow-md p-6">
          <div className="flex items-center gap-3 mb-6">
            <GraduationCap className="text-green-600" />

            <h2 className="text-2xl font-bold text-gray-800">
              Learning Resources
            </h2>
          </div>

          <div className="space-y-4">
            {resources.map((resource, index) => (
              <div
                key={index}
                className="border border-gray-100 rounded-xl p-4 flex items-center justify-between"
              >
                <span className="text-gray-700 text-sm">
                  {resource}
                </span>

                <Download
                  size={18}
                  className="text-blue-900 cursor-pointer"
                />
              </div>
            ))}
          </div>
        </div>

        {/* Tasks */}
        <div className="bg-white rounded-2xl shadow-md p-6">
          <div className="flex items-center gap-3 mb-6">
            <CheckCircle2 className="text-orange-500" />

            <h2 className="text-2xl font-bold text-gray-800">
              Daily Tasks
            </h2>
          </div>

          <div className="space-y-4">
            {tasks.map((task, index) => (
              <div
                key={index}
                className="flex items-center gap-3 border border-gray-100 rounded-xl p-4"
              >
                <input
                  type="checkbox"
                  className="w-5 h-5"
                />

                <span className="text-gray-700">
                  {task}
                </span>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Bottom Section */}
      <div className="grid grid-cols-1 xl:grid-cols-4 gap-6">
        {/* Gamification */}
        <div className="bg-white rounded-2xl shadow-md p-6">
          <div className="flex items-center gap-3 mb-6">
            <Trophy className="text-yellow-500" />

            <h2 className="text-xl font-bold text-gray-800">
              Achievements
            </h2>
          </div>

          <div className="space-y-4">
            <div className="bg-yellow-50 rounded-xl p-4">
              <p className="font-semibold text-gray-700">
                🔥 15 Day Streak
              </p>
            </div>

            <div className="bg-blue-50 rounded-xl p-4">
              <p className="font-semibold text-gray-700">
                🏆 Top in Mathematics
              </p>
            </div>

            <div className="bg-green-50 rounded-xl p-4">
              <p className="font-semibold text-gray-700">
                ⭐ 1200 XP Points
              </p>
            </div>
          </div>
        </div>

        {/* Transport */}
        <div className="bg-white rounded-2xl shadow-md p-6">
          <div className="flex items-center gap-3 mb-6">
            <Bus className="text-blue-900" />

            <h2 className="text-xl font-bold text-gray-800">
              Transport
            </h2>
          </div>

          <div className="space-y-3">
            <p className="text-gray-700">
              Route: North Zone
            </p>

            <p className="text-gray-700">
              Bus No: PB10-2211
            </p>

            <p className="text-gray-700">
              Driver: Raj Singh
            </p>

            <div className="bg-green-100 text-green-700 px-4 py-2 rounded-xl text-sm inline-block">
              Bus Arriving in 10 mins
            </div>
          </div>
        </div>

        {/* Library */}
        <div className="bg-white rounded-2xl shadow-md p-6">
          <div className="flex items-center gap-3 mb-6">
            <BookOpen className="text-purple-700" />

            <h2 className="text-xl font-bold text-gray-800">
              Library
            </h2>
          </div>

          <div className="space-y-4">
            {libraryBooks.map((book, index) => (
              <div
                key={index}
                className="border border-gray-100 rounded-xl p-4"
              >
                <h3 className="font-medium text-gray-700">
                  {book.name}
                </h3>

                <p className="text-sm text-gray-500 mt-2">
                  Return By: {book.due}
                </p>
              </div>
            ))}
          </div>
        </div>

        {/* Results */}
        <div className="bg-white rounded-2xl shadow-md p-6">
          <div className="flex items-center gap-3 mb-6">
            <FileText className="text-green-600" />

            <h2 className="text-xl font-bold text-gray-800">
              Results
            </h2>
          </div>

          <div className="space-y-4">
            <div className="bg-gray-50 rounded-xl p-4">
              <p className="text-gray-500 text-sm">
                Overall GPA
              </p>

              <h2 className="text-3xl font-bold text-blue-900">
                9.2
              </h2>
            </div>

            <button className="w-full bg-blue-900 text-white py-3 rounded-xl hover:bg-blue-800 transition">
              Download Report Card
            </button>
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