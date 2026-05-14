import { NavLink } from "react-router-dom";

import { responsibilityMenus } from "../config/responsibilityMenus";

const Sidebar = () => {

  /*
    TEMPORARY AUTH SYSTEM
  */

  const role = localStorage.getItem("role");

  /*
    RESPONSIBILITIES
    Example:
    [
      "class-incharge",
      "exam-coordinator",
      "timetable-incharge"
    ]
  */

  const responsibilities =
    JSON.parse(
      localStorage.getItem("responsibilities")
    ) || [];

  // =========================
  // SUPER ADMIN MENU
  // =========================

  const superAdminMenu = [
    { name: "Dashboard", path: "/dashboard/super-admin" },
    { name: "Clusters", path: "/dashboard/clusters" },
    { name: "Schools", path: "/dashboard/schools" },
    { name: "Subscriptions", path: "/dashboard/subscriptions" },
    { name: "School Admins", path: "/dashboard/school-admins" },
    { name: "Cluster Admins", path: "/dashboard/cluster-admins" },
    { name: "Users", path: "/dashboard/users" },
    { name: "Global Reports", path: "/dashboard/global-reports" },
    { name: "Settings", path: "/dashboard/settings" },
  ];

  // =========================
  // CLUSTER ADMIN MENU
  // =========================

  const clusterAdminMenu = [
    { name: "Dashboard", path: "/dashboard/cluster-admin" },
    { name: "Cluster Schools", path: "/dashboard/cluster-schools" },
    { name: "Analytics", path: "/dashboard/analytics" },
    { name: "Attendance Reports", path: "/dashboard/attendance-reports" },
    { name: "Academic Reports", path: "/dashboard/academic-reports" },
    { name: "Staff Monitoring", path: "/dashboard/staff-monitoring" },
    { name: "Meetings", path: "/dashboard/meetings" },
    { name: "Notices", path: "/dashboard/notices" },
  ];

  // =========================
  // SCHOOL ADMIN MENU
  // =========================

  const adminMenu = [
    { name: "Dashboard", path: "/dashboard/admin" },
    { name: "Students", path: "/dashboard/students" },
    { name: "Staff", path: "/dashboard/staff" },
    { name: "Admissions", path: "/dashboard/admissions" },
    { name: "Academics", path: "/dashboard/academics" },
    { name: "Attendance", path: "/dashboard/attendance" },
    { name: "Examinations", path: "/dashboard/examinations" },
    { name: "Fees", path: "/dashboard/fees" },
    { name: "Timetable", path: "/dashboard/timetable" },
    { name: "Library", path: "/dashboard/library" },
    { name: "Transport", path: "/dashboard/transport" },
    { name: "Hostel", path: "/dashboard/hostel" },
    { name: "Inventory", path: "/dashboard/inventory" },
    { name: "Reports", path: "/dashboard/reports" },
    { name: "Settings", path: "/dashboard/settings" },
  ];

  // =========================
  // PRINCIPAL MENU
  // =========================

  const principalMenu = [
    { name: "Dashboard", path: "/dashboard/principal" },
    { name: "Academic Reports", path: "/dashboard/academic-reports" },
    { name: "Attendance", path: "/dashboard/attendance" },
    { name: "Staff Monitoring", path: "/dashboard/staff" },
    { name: "Examinations", path: "/dashboard/examinations" },
    { name: "Meetings", path: "/dashboard/meetings" },
    { name: "Analytics", path: "/dashboard/analytics" },
    { name: "Discipline", path: "/dashboard/discipline" },
  ];

  // =========================
  // VICE PRINCIPAL MENU
  // =========================

  const vicePrincipalMenu = [
    { name: "Dashboard", path: "/dashboard/vice-principal" },
    { name: "Attendance", path: "/dashboard/attendance" },
    { name: "Discipline", path: "/dashboard/discipline" },
    { name: "Teacher Monitoring", path: "/dashboard/staff" },
    { name: "Meetings", path: "/dashboard/meetings" },
    { name: "Reports", path: "/dashboard/reports" },
  ];

  // =========================
  // TEACHER MENU
  // =========================

  const teacherMenu = [
    { name: "Dashboard", path: "/dashboard/teacher" },
    { name: "My Classes", path: "/dashboard/my-classes" },
    { name: "Attendance", path: "/dashboard/attendance" },
    { name: "Homework", path: "/dashboard/homework" },
    { name: "Assignments", path: "/dashboard/assignments" },
    { name: "Marks Entry", path: "/dashboard/marks" },
    { name: "Timetable", path: "/dashboard/timetable" },
  ];

  // =========================
  // ACCOUNTANT MENU
  // =========================

  const accountantMenu = [
    { name: "Dashboard", path: "/dashboard/accountant" },
    { name: "Fees", path: "/dashboard/fees" },
    { name: "Receipts", path: "/dashboard/receipts" },
    { name: "Concessions", path: "/dashboard/concessions" },
    { name: "Scholarships", path: "/dashboard/scholarships" },
    { name: "Fee Reports", path: "/dashboard/fee-reports" },
  ];

  // =========================
  // CLERK MENU
  // =========================

  const clerkMenu = [
    { name: "Dashboard", path: "/dashboard/clerk" },
    { name: "Admissions", path: "/dashboard/admissions" },
    { name: "Certificates", path: "/dashboard/certificates" },
    { name: "Student Records", path: "/dashboard/student-records" },
    { name: "Reports", path: "/dashboard/reports" },
  ];

  // =========================
  // RECEPTIONIST MENU
  // =========================

  const receptionistMenu = [
    { name: "Dashboard", path: "/dashboard/receptionist" },
    { name: "Visitors", path: "/dashboard/visitors" },
    { name: "Inquiries", path: "/dashboard/inquiries" },
    { name: "Appointments", path: "/dashboard/appointments" },
    { name: "Calls", path: "/dashboard/calls" },
  ];

  // =========================
  // LIBRARIAN MENU
  // =========================

  const librarianMenu = [
    { name: "Dashboard", path: "/dashboard/librarian" },
    { name: "Books", path: "/dashboard/books" },
    { name: "Issue Books", path: "/dashboard/issue-books" },
    { name: "Returns", path: "/dashboard/returns" },
    { name: "Fine Management", path: "/dashboard/fines" },
    { name: "Library Reports", path: "/dashboard/library-reports" },
  ];

  // =========================
  // HOSTEL WARDEN MENU
  // =========================

  const hostelWardenMenu = [
    { name: "Dashboard", path: "/dashboard/hostel-warden" },
    { name: "Rooms", path: "/dashboard/rooms" },
    { name: "Hostel Students", path: "/dashboard/hostel-students" },
    { name: "Hostel Attendance", path: "/dashboard/hostel-attendance" },
    { name: "Discipline", path: "/dashboard/discipline" },
    { name: "Hostel Reports", path: "/dashboard/hostel-reports" },
  ];

  // =========================
  // SECURITY SUPERVISOR MENU
  // =========================

  const securitySupervisorMenu = [
    { name: "Dashboard", path: "/dashboard/security-supervisor" },
    { name: "Visitor Logs", path: "/dashboard/visitor-logs" },
    { name: "Gate Entries", path: "/dashboard/gate-entries" },
    { name: "Incidents", path: "/dashboard/incidents" },
    { name: "Vehicles", path: "/dashboard/vehicles" },
  ];

  // =========================
  // STUDENT MENU
  // =========================

  const studentMenu = [
    { name: "Dashboard", path: "/dashboard/student" },
    { name: "Subjects", path: "/dashboard/subjects" },
    { name: "Homework", path: "/dashboard/homework" },
    { name: "Assignments", path: "/dashboard/assignments" },
    { name: "Results", path: "/dashboard/results" },
    { name: "Attendance", path: "/dashboard/attendance" },
    { name: "Timetable", path: "/dashboard/timetable" },
  ];

  // =========================
  // PARENT MENU
  // =========================

  const parentMenu = [
    { name: "Dashboard", path: "/dashboard/parent" },
    { name: "Attendance", path: "/dashboard/attendance" },
    { name: "Homework", path: "/dashboard/homework" },
    { name: "Results", path: "/dashboard/results" },
    { name: "Fees", path: "/dashboard/fees" },
    { name: "Messages", path: "/dashboard/messages" },
  ];

  // =========================
  // ROLE BASED MENU
  // =========================

  let menuItems = [];

  if (role === "super-admin") menuItems = superAdminMenu;
  if (role === "cluster-admin") menuItems = clusterAdminMenu;
  if (role === "admin") menuItems = adminMenu;
  if (role === "principal") menuItems = principalMenu;
  if (role === "vice-principal") menuItems = vicePrincipalMenu;
  if (role === "teacher") menuItems = teacherMenu;
  if (role === "accountant") menuItems = accountantMenu;
  if (role === "clerk") menuItems = clerkMenu;
  if (role === "receptionist") menuItems = receptionistMenu;
  if (role === "librarian") menuItems = librarianMenu;
  if (role === "hostel-warden") menuItems = hostelWardenMenu;
  if (role === "security-supervisor") menuItems = securitySupervisorMenu;
  if (role === "student") menuItems = studentMenu;
  if (role === "parent") menuItems = parentMenu;

  // =========================
  // RESPONSIBILITY BASED MENUS
  // =========================

  responsibilities.forEach((responsibility) => {

    const extraMenus =
      responsibilityMenus[responsibility];

    if (extraMenus) {

      menuItems.push(...extraMenus);

    }

  });

  return (

    <aside
      className="
        w-64
        h-screen
        overflow-hidden
        bg-gradient-to-b
        from-blue-950
        to-blue-900
        text-white
        shadow-2xl
        flex
        flex-col
      "
    >

      {/* ===================================== */}
      {/* LOGO */}
      {/* ===================================== */}

      <div className="p-6 border-b border-blue-800">

        <h1 className="text-3xl font-bold tracking-wide">
          SIMS
        </h1>

        <p className="text-blue-200 text-sm mt-1">
          School ERP System
        </p>

        <div
          className="
            mt-4
            inline-block
            bg-white/10
            px-3
            py-1
            rounded-full
            text-xs
            uppercase
            tracking-wider
            text-blue-100
          "
        >
          {role}
        </div>

      </div>

      {/* ===================================== */}
      {/* NAVIGATION */}
      {/* ===================================== */}

      <nav
        className="
          flex-1
          p-4
          space-y-2
          overflow-y-auto
          scroll-smooth
          custom-scrollbar
        "
      >

        {menuItems.map((item) => (

          <NavLink
            key={item.name}
            to={item.path}
            className={({ isActive }) =>
              `
                block
                px-4
                py-3
                rounded-xl
                transition-all
                duration-200
                ${
                  isActive
                    ? "bg-white text-blue-900 font-semibold shadow-md"
                    : "hover:bg-blue-800 text-blue-100"
                }
              `
            }
          >
            {item.name}
          </NavLink>

        ))}

      </nav>

    </aside>

  );
};

export default Sidebar;