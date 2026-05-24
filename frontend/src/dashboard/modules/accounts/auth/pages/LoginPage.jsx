import { Link, useNavigate } from "react-router-dom";

export default function Login() {

  const navigate = useNavigate();

  // =========================
  // COMMON LOGIN FUNCTION
  // =========================

  const loginUser = (
    role,
    path,
    responsibilities = []
  ) => {

    localStorage.setItem("role", role);

    localStorage.setItem(
      "responsibilities",
      JSON.stringify(responsibilities)
    );

    navigate(path);

  };

  // =========================
  // HANDLE LOGIN
  // =========================

  const handleLogin = (e) => {

    e.preventDefault();

    const email = e.target.email.value;
    const password = e.target.password.value;

    // =========================
    // CLEAR OLD SESSION
    // =========================

    localStorage.removeItem("role");
    localStorage.removeItem("responsibilities");

    // =========================
    // SUPER ADMIN LOGIN
    // =========================

    if (
      email === "superadmin" &&
      password === "superadmin"
    ) {

      loginUser(
        "super-admin",
        "/dashboard/super-admin"
      );

      return;
    }

    // =========================
    // CLUSTER ADMIN LOGIN
    // =========================

    if (
      email === "clusteradmin" &&
      password === "clusteradmin"
    ) {

      loginUser(
        "cluster-admin",
        "/dashboard/cluster-admin"
      );

      return;
    }

    // =========================
    // SCHOOL ADMIN LOGIN
    // =========================

    if (
      email === "admin" &&
      password === "admin"
    ) {

      loginUser(
        "admin",
        "/dashboard/admin"
      );

      return;
    }

    // =========================
    // PRINCIPAL LOGIN
    // =========================

    if (
      email === "principal" &&
      password === "principal"
    ) {

      loginUser(
        "principal",
        "/dashboard/principal"
      );

      return;
    }

    // =========================
    // VICE PRINCIPAL LOGIN
    // =========================

    if (
      email === "viceprincipal" &&
      password === "viceprincipal"
    ) {

      loginUser(
        "vice-principal",
        "/dashboard/vice-principal"
      );

      return;
    }

    // =========================
    // TEACHER LOGIN
    // =========================

    if (
      email === "teacher" &&
      password === "teacher"
    ) {

      loginUser(
        "teacher",
        "/dashboard/teacher"
      );

      return;
    }

    // =========================
    // CLASS INCHARGE LOGIN
    // =========================

    if (
      email === "classincharge" &&
      password === "classincharge"
    ) {

      loginUser(
        "teacher",
        "/dashboard/teacher",
        [
          "class-incharge"
        ]
      );

      return;
    }

    // =========================
    // EXAM COORDINATOR LOGIN
    // =========================

    if (
      email === "examcoordinator" &&
      password === "examcoordinator"
    ) {

      loginUser(
        "teacher",
        "/dashboard/teacher",
        [
          "exam-coordinator"
        ]
      );

      return;
    }

    // =========================
    // TIMETABLE INCHARGE LOGIN
    // =========================

    if (
      email === "timetableincharge" &&
      password === "timetableincharge"
    ) {

      loginUser(
        "teacher",
        "/dashboard/teacher",
        [
          "timetable-incharge"
        ]
      );

      return;
    }

    // =========================
    // TRANSPORT INCHARGE LOGIN
    // =========================

    if (
      email === "transportincharge" &&
      password === "transportincharge"
    ) {

      loginUser(
        "teacher",
        "/dashboard/teacher",
        [
          "transport-incharge"
        ]
      );

      return;
    }

    // =========================
    // SPORTS COORDINATOR LOGIN
    // =========================

    if (
      email === "sportscoordinator" &&
      password === "sportscoordinator"
    ) {

      loginUser(
        "teacher",
        "/dashboard/teacher",
        [
          "sports-coordinator"
        ]
      );

      return;
    }

    // =========================
    // SENIOR TEACHER LOGIN
    // =========================

    if (
      email === "seniorteacher" &&
      password === "seniorteacher"
    ) {

      loginUser(
        "teacher",
        "/dashboard/teacher",
        [
          "class-incharge",
          "exam-coordinator",
          "timetable-incharge",
          "sports-coordinator"
        ]
      );

      return;
    }

    // =========================
    // ACCOUNTANT LOGIN
    // =========================

    if (
      email === "accountant" &&
      password === "accountant"
    ) {

      loginUser(
        "accountant",
        "/dashboard/accountant"
      );

      return;
    }

    // =========================
    // CLERK LOGIN
    // =========================

    if (
      email === "clerk" &&
      password === "clerk"
    ) {

      loginUser(
        "clerk",
        "/dashboard/clerk"
      );

      return;
    }

    // =========================
    // RECEPTIONIST LOGIN
    // =========================

    if (
      email === "receptionist" &&
      password === "receptionist"
    ) {

      loginUser(
        "receptionist",
        "/dashboard/receptionist"
      );

      return;
    }

    // =========================
    // LIBRARIAN LOGIN
    // =========================

    if (
      email === "librarian" &&
      password === "librarian"
    ) {

      loginUser(
        "librarian",
        "/dashboard/librarian"
      );

      return;
    }

    // =========================
    // HOSTEL WARDEN LOGIN
    // =========================

    if (
      email === "hostelwarden" &&
      password === "hostelwarden"
    ) {

      loginUser(
        "hostel-warden",
        "/dashboard/hostel-warden"
      );

      return;
    }

    // =========================
    // SECURITY SUPERVISOR LOGIN
    // =========================

    if (
      email === "security" &&
      password === "security"
    ) {

      loginUser(
        "security-supervisor",
        "/dashboard/security-supervisor"
      );

      return;
    }

    // =========================
    // STUDENT LOGIN
    // =========================

    if (
      email === "student" &&
      password === "student"
    ) {

      loginUser(
        "student",
        "/dashboard/student"
      );

      return;
    }

    // =========================
    // PARENT LOGIN
    // =========================

    if (
      email === "parent" &&
      password === "parent"
    ) {

      loginUser(
        "parent",
        "/dashboard/parent"
      );

      return;
    }

    // =========================
    // INVALID LOGIN
    // =========================

    alert("Invalid User ID or Password");

  };

  return (

    <div className="min-h-screen bg-gray-100 flex items-center justify-center px-4 py-10">

      <div className="w-full max-w-6xl bg-white rounded-[40px] overflow-hidden shadow-2xl">

        <div className="grid lg:grid-cols-2">

          {/* LEFT SIDE */}
          <div className="bg-blue-700 text-white p-12 lg:p-16 flex flex-col justify-center relative overflow-hidden">

            <div className="absolute inset-0 opacity-10">
              <div className="w-full h-full bg-[radial-gradient(circle_at_top_right,_white,_transparent_40%)]"></div>
            </div>

            <div className="relative z-10">

              <p className="uppercase tracking-widest text-blue-200 font-semibold mb-5">
                Welcome Back
              </p>

              <h1 className="text-5xl lg:text-6xl font-bold leading-tight mb-8">
                SIMS
                <span className="block text-blue-200">
                  Portal Login
                </span>
              </h1>

              <p className="text-lg leading-9 text-blue-100 mb-10">
                Access the School Information Management System
                for schools, teachers, students, parents,
                principals, and administrators.
              </p>

              {/* DEMO CREDENTIALS */}
              <div className="bg-white/10 rounded-2xl p-6 space-y-2 mb-10 max-h-[420px] overflow-y-auto">

                <h3 className="text-xl font-semibold mb-4">
                  Demo Login Credentials
                </h3>

                <p><b>Super Admin:</b> superadmin / superadmin</p>
                <p><b>Cluster Admin:</b> clusteradmin / clusteradmin</p>
                <p><b>School Admin:</b> admin / admin</p>
                <p><b>Principal:</b> principal / principal</p>
                <p><b>Vice Principal:</b> viceprincipal / viceprincipal</p>

                <hr className="border-white/20 my-4" />

                <p><b>Teacher:</b> teacher / teacher</p>
                <p><b>Class Incharge:</b> classincharge / classincharge</p>
                <p><b>Exam Coordinator:</b> examcoordinator / examcoordinator</p>
                <p><b>Timetable Incharge:</b> timetableincharge / timetableincharge</p>
                <p><b>Transport Incharge:</b> transportincharge / transportincharge</p>
                <p><b>Sports Coordinator:</b> sportscoordinator / sportscoordinator</p>
                <p><b>Senior Teacher:</b> seniorteacher / seniorteacher</p>

                <hr className="border-white/20 my-4" />

                <p><b>Accountant:</b> accountant / accountant</p>
                <p><b>Clerk:</b> clerk / clerk</p>
                <p><b>Receptionist:</b> receptionist / receptionist</p>
                <p><b>Librarian:</b> librarian / librarian</p>
                <p><b>Hostel Warden:</b> hostelwarden / hostelwarden</p>
                <p><b>Security Supervisor:</b> security / security</p>

                <hr className="border-white/20 my-4" />

                <p><b>Student:</b> student / student</p>
                <p><b>Parent:</b> parent / parent</p>

              </div>

            </div>

          </div>

          {/* RIGHT SIDE */}
          <div className="p-12 lg:p-16 flex items-center">

            <div className="w-full">

              <div className="mb-10">

                <p className="uppercase tracking-widest text-blue-600 font-semibold mb-3">
                  Account Access
                </p>

                <h2 className="text-4xl font-bold text-gray-800 mb-4">
                  Login To Continue
                </h2>

              </div>

              <form onSubmit={handleLogin} className="space-y-7">

                <div>

                  <label className="block text-gray-700 font-medium mb-3">
                    User ID
                  </label>

                  <input
                    type="text"
                    name="email"
                    placeholder="Enter your user ID"
                    className="w-full border border-gray-300 rounded-2xl px-5 py-4 focus:outline-none focus:ring-2 focus:ring-blue-600"
                  />

                </div>

                <div>

                  <div className="flex items-center justify-between mb-3">

                    <label className="text-gray-700 font-medium">
                      Password
                    </label>

                    <Link
                      to="/forgot-password"
                      className="text-blue-600 hover:underline text-sm font-medium"
                    >
                      Forgot Password?
                    </Link>

                  </div>

                  <input
                    type="password"
                    name="password"
                    placeholder="Enter your password"
                    className="w-full border border-gray-300 rounded-2xl px-5 py-4 focus:outline-none focus:ring-2 focus:ring-blue-600"
                  />

                </div>

                <button
                  type="submit"
                  className="w-full bg-blue-600 hover:bg-blue-700 text-white py-4 rounded-2xl font-semibold text-lg transition"
                >
                  Login
                </button>

              </form>

            </div>

          </div>

        </div>

      </div>

    </div>

  );
}