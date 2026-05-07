import { useNavigate } from "react-router-dom";

const TopNavbar = () => {

  const navigate = useNavigate();

  // =========================
  // GET ROLE
  // =========================

  const role = localStorage.getItem("role");

  // =========================
  // LOGOUT
  // =========================

  const handleLogout = () => {

    localStorage.removeItem("role");
    localStorage.removeItem("responsibilities");

    navigate("/login");

  };

  // =========================
  // ROLE LABELS
  // =========================

  const roleLabels = {

    "super-admin": "Super Admin",
    "cluster-admin": "Cluster Admin",
    "admin": "School Admin",
    "principal": "Principal",
    "vice-principal": "Vice Principal",
    "teacher": "Teacher",
    "accountant": "Accountant",
    "clerk": "Clerk",
    "receptionist": "Receptionist",
    "librarian": "Librarian",
    "hostel-warden": "Hostel Warden",
    "security-supervisor": "Security Supervisor",
    "student": "Student",
    "parent": "Parent",

  };

  // =========================
  // USER NAME
  // =========================

  const userName =
    roleLabels[role] || "User";

  // =========================
  // USER INITIAL
  // =========================

  const userInitial =
    userName.charAt(0).toUpperCase();

  return (

    <header className="bg-white shadow-sm h-16 flex items-center justify-between px-6">

      {/* LEFT SIDE */}
      <div>

        <h1 className="text-xl font-semibold text-gray-700">
          School Management System
        </h1>

      </div>

      {/* RIGHT SIDE */}
      <div className="flex items-center gap-4">

        {/* USER INFO */}
        <div className="text-right">

          <p className="font-semibold text-gray-700">
            {userName}
          </p>

          <p className="text-sm text-gray-500 capitalize">
            {role}
          </p>

        </div>

        {/* AVATAR */}
        <div className="w-10 h-10 rounded-full bg-blue-900 text-white flex items-center justify-center font-bold">

          {userInitial}

        </div>

        {/* LOGOUT BUTTON */}
        <button
          onClick={handleLogout}
          className="bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded-xl text-sm font-medium transition"
        >
          Logout
        </button>

      </div>

    </header>

  );
};

export default TopNavbar;