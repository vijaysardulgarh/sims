import { NavLink } from "react-router-dom";
import {
  FaTachometerAlt,
  FaUserGraduate,
  FaChalkboardTeacher,
  FaBook,
  FaClock,
  FaFileAlt,
  FaCog,
} from "react-icons/fa";

const Sidebar = () => {
  const menuItems = [
    {
      name: "Dashboard",
      path: "/dashboard/admin",
      icon: <FaTachometerAlt />,
    },
    {
      name: "Students",
      path: "/dashboard/students",
      icon: <FaUserGraduate />,
    },
    {
      name: "Staff",
      path: "/dashboard/staff",
      icon: <FaChalkboardTeacher />,
    },
    {
      name: "Academics",
      path: "/dashboard/academics",
      icon: <FaBook />,
    },
    {
      name: "Timetable",
      path: "/dashboard/timetable",
      icon: <FaClock />,
    },
    {
      name: "Reports",
      path: "/dashboard/reports",
      icon: <FaFileAlt />,
    },
    {
      name: "Settings",
      path: "/dashboard/settings",
      icon: <FaCog />,
    },
  ];

  return (
    <aside className="w-64 bg-blue-900 text-white min-h-screen">
      <div className="p-5 text-2xl font-bold border-b border-blue-700">
        SIMS ERP
      </div>

      <nav className="mt-5 flex flex-col gap-2 px-3">
        {menuItems.map((item) => (
          <NavLink
            key={item.name}
            to={item.path}
            className={({ isActive }) =>
              `flex items-center gap-3 px-4 py-3 rounded-lg transition ${
                isActive
                  ? "bg-white text-blue-900"
                  : "hover:bg-blue-800"
              }`
            }
          >
            {item.icon}
            <span>{item.name}</span>
          </NavLink>
        ))}
      </nav>
    </aside>
  );
};

export default Sidebar;