import { NavLink } from "react-router-dom";

const Sidebar = () => {

  /*
    TEMPORARY ROLE
    Later this will come from backend/auth context
  */

  const role = localStorage.getItem("role");

  // Admin Menu
  const adminMenu = [
    {
      name: "Dashboard",
      path: "/dashboard/admin",
    },
    {
      name: "Students",
      path: "/dashboard/students",
    },
    {
      name: "Staff",
      path: "/dashboard/staff",
    },
    {
      name: "Reports",
      path: "/dashboard/reports",
    },
    {
      name: "Settings",
      path: "/dashboard/settings",
    },
  ];

  // Teacher Menu
  const teacherMenu = [
    {
      name: "Dashboard",
      path: "/dashboard/teacher",
    },
    {
      name: "Attendance",
      path: "/dashboard/attendance",
    },
    {
      name: "Assignments",
      path: "/dashboard/assignments",
    },
    {
      name: "Timetable",
      path: "/dashboard/timetable",
    },
  ];

  // Student Menu
  const studentMenu = [
    {
      name: "Dashboard",
      path: "/dashboard/student",
    },
    {
      name: "Subjects",
      path: "/dashboard/subjects",
    },
    {
      name: "Results",
      path: "/dashboard/results",
    },
    {
      name: "Attendance",
      path: "/dashboard/attendance",
    },
  ];

  // Principal Menu
  const principalMenu = [
    {
      name: "Dashboard",
      path: "/dashboard/principal",
    },
    {
      name: "Analytics",
      path: "/dashboard/analytics",
    },
    {
      name: "Reports",
      path: "/dashboard/reports",
    },
    {
      name: "Staff",
      path: "/dashboard/staff",
    },
  ];

  // Role-based menu selection
  let menuItems = [];

  if (role === "admin") {
    menuItems = adminMenu;
  }

  if (role === "teacher") {
    menuItems = teacherMenu;
  }

  if (role === "student") {
    menuItems = studentMenu;
  }

  if (role === "principal") {
    menuItems = principalMenu;
  }

  return (
    <aside className="w-64 min-h-screen bg-blue-900 text-white">

      {/* Logo */}
      <div className="p-6 border-b border-blue-800">

        <h1 className="text-3xl font-bold">
          SIMS
        </h1>

        <p className="text-blue-200 text-sm mt-1">
          School ERP System
        </p>

      </div>

      {/* Navigation */}
      <nav className="p-4 space-y-2">

        {menuItems.map((item) => (
          <NavLink
            key={item.name}
            to={item.path}
            className={({ isActive }) =>
              `block px-4 py-3 rounded-xl transition ${
                isActive
                  ? "bg-white text-blue-900 font-semibold"
                  : "hover:bg-blue-800"
              }`
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