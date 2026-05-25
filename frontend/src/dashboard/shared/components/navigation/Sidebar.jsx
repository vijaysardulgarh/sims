import { NavLink } from "react-router-dom";

import { useAuth } from "../../../modules/accounts/auth/context/AuthContext";

import { responsibilityMenus } from "../../../config/responsibilityMenus";



const Sidebar = () => {

  // =====================================
  // AUTH
  // =====================================


  const { user } = useAuth();

  console.log(user);


  // =====================================
  // NORMALIZED ROLES
  // =====================================

  /*
    Supports:

    ["ADMIN"]

    OR

    [
      {
        name: "ADMIN"
      }
    ]

    OR

    [
      {
        code: "ADMIN"
      }
    ]
  */

  const roles =

    user?.roles?.map((role) => {

      // STRING ROLE

      if (typeof role === "string") {

        return role.toUpperCase();
      }

      // OBJECT ROLE

      return (
        role?.code ||
        role?.name ||
        role?.role_code ||
        ""
      ).toUpperCase();

    }) || [];


  // =====================================
  // RESPONSIBILITIES
  // =====================================

  const responsibilities =

    user?.responsibilities || [];


  // =====================================
  // DEBUG
  // =====================================

  console.log("USER:", user);

  console.log("ROLES:", roles);


  // =====================================
  // SUPER ADMIN MENU
  // =====================================

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


  // =====================================
  // ADMIN MENU
  // =====================================

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

    { name: "Reports", path: "/dashboard/reports" },

    { name: "Settings", path: "/dashboard/settings" },
  ];


  // =====================================
  // TEACHER MENU
  // =====================================

  const teacherMenu = [

    { name: "Dashboard", path: "/dashboard/teacher" },

    { name: "My Classes", path: "/dashboard/my-classes" },

    { name: "Attendance", path: "/dashboard/attendance" },

    { name: "Homework", path: "/dashboard/homework" },

    { name: "Assignments", path: "/dashboard/assignments" },

    { name: "Marks Entry", path: "/dashboard/marks" },

    { name: "Timetable", path: "/dashboard/timetable" },
  ];


  // =====================================
  // ACCOUNTANT MENU
  // =====================================

  const accountantMenu = [

    { name: "Dashboard", path: "/dashboard/accountant" },

    { name: "Fees", path: "/dashboard/fees" },

    { name: "Receipts", path: "/dashboard/receipts" },

    { name: "Fee Reports", path: "/dashboard/fee-reports" },
  ];


  // =====================================
  // ROLE BASED MENU
  // =====================================

  let menuItems = [];


  // SUPER ADMIN

  if (roles.includes("SUPER_ADMIN")) {

    menuItems.push(...superAdminMenu);
  }


  // ADMIN

  if (roles.includes("ADMIN")) {

    menuItems.push(...adminMenu);
  }


  // TEACHER

  if (roles.includes("TEACHER")) {

    menuItems.push(...teacherMenu);
  }


  // ACCOUNTANT

  if (roles.includes("ACCOUNTANT")) {

    menuItems.push(...accountantMenu);
  }


  // =====================================
  // RESPONSIBILITY MENUS
  // =====================================

  responsibilities.forEach((responsibility) => {

    const extraMenus =

      responsibilityMenus?.[responsibility];

    if (extraMenus) {

      menuItems.push(...extraMenus);
    }

  });


  // =====================================
  // REMOVE DUPLICATES
  // =====================================

  menuItems = [

    ...new Map(

      menuItems.map((item) => [

        item.path,

        item
      ])
    ).values()
  ];


  // =====================================
  // DEBUG
  // =====================================

  console.log("MENU ITEMS:", menuItems);


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

      {/* LOGO */}

      <div className="p-6 border-b border-blue-800">

        <h1 className="text-3xl font-bold tracking-wide">

          SIMS

        </h1>

        <p className="text-blue-200 text-sm mt-1">

          School ERP System

        </p>


        {/* ROLE BADGES */}

        <div className="mt-4 flex flex-wrap gap-2">

          {
            roles.map((role) => (

              <span
                key={role}
                className="
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

              </span>
            ))
          }

        </div>

      </div>


      {/* NAVIGATION */}

      <nav
        className="
          flex-1
          p-4
          space-y-2
          overflow-y-auto
        "
      >

        {
          menuItems.length === 0 && (

            <div className="text-blue-200 text-sm">

              No menu items available

            </div>
          )
        }


        {
          menuItems.map((item) => (

            <NavLink

              key={item.path}

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
          ))
        }

      </nav>

    </aside>
  );
};


export default Sidebar;