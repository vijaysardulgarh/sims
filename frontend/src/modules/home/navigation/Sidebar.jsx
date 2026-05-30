import {

  useEffect,

  useState

} from "react";

import {

  NavLink

} from "react-router-dom";

import api from '../../../services/api/axios';


const Sidebar = () => {

  // =====================================
  // STATE
  // =====================================

  const [menus, setMenus] =
    useState([]);

  const [openMenus, setOpenMenus] =
    useState({});


  // =====================================
  // LOAD SIDEBAR
  // =====================================

  useEffect(() => {

    fetchSidebar();

  }, []);


  // =====================================
  // FETCH SIDEBAR
  // =====================================

  const fetchSidebar = async () => {

    try {

      const response = await api.get(

        "/accounts/modules/sidebar/"
      );

      console.log(
        "SIDEBAR DATA:",
        response.data
      );

      setMenus(
        response.data
      );

    } catch (error) {

      console.error(
        "Sidebar Error:",
        error
      );
    }
  };


  // =====================================
  // TOGGLE MENU
  // =====================================

  const toggleMenu = (menuId) => {

    setOpenMenus((prev) => ({

      ...prev,

      [menuId]: !prev[menuId],
    }));
  };


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

      {/* ================================= */}
      {/* LOGO */}
      {/* ================================= */}

      <div className="p-6 border-b border-blue-800">

        <h1 className="text-3xl font-bold tracking-wide">

          SIMS

        </h1>

        <p className="text-blue-200 text-sm mt-1">

          School ERP System

        </p>

      </div>


      {/* ================================= */}
      {/* NAVIGATION */}
      {/* ================================= */}

      <nav
        className="
          flex-1
          p-4
          overflow-y-auto
        "
      >

        <div className="space-y-2">

          {
            menus.map((menu) => {

              const hasChildren =

                menu.children &&
                menu.children.length > 0;

              const isOpen =
                openMenus[menu.id];

              return (

                <div
                  key={menu.id}
                >

                  {/* ===================== */}
                  {/* PARENT MENU */}
                  {/* ===================== */}

                  {
                    hasChildren ? (

                      <button

                        onClick={() =>
                          toggleMenu(menu.id)
                        }

                        className="
                          w-full
                          flex
                          items-center
                          justify-between
                          px-4
                          py-3
                          rounded-xl
                          hover:bg-blue-800
                          transition-all
                          duration-200
                          text-left
                        "
                      >

                        <span>

                          {menu.name}

                        </span>

                        <span>

                          {
                            isOpen
                              ? "−"
                              : "+"
                          }

                        </span>

                      </button>

                    ) : (

                      <NavLink

                        to={menu.path || "#"}

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

                        {menu.name}

                      </NavLink>
                    )
                  }


                  {/* ===================== */}
                  {/* CHILD MENUS */}
                  {/* ===================== */}

                  {
                    hasChildren &&
                    isOpen && (

                      <div
                        className="
                          ml-4
                          mt-1
                          space-y-1
                          border-l
                          border-blue-700
                          pl-3
                        "
                      >

                        {
                          menu.children.map((child) => (

                            <NavLink

                              key={child.id}

                              to={child.path || "#"}

                              className={({ isActive }) =>

                                `
                                  block
                                  px-4
                                  py-2
                                  text-sm
                                  rounded-lg
                                  transition-all
                                  duration-200
                                  ${
                                    isActive
                                      ? "bg-white text-blue-900 font-medium"
                                      : "hover:bg-blue-800 text-blue-100"
                                  }
                                `
                              }
                            >

                              {child.name}

                            </NavLink>
                          ))
                        }

                      </div>
                    )
                  }

                </div>
              );
            })
          }

        </div>

      </nav>

    </aside>
  );
};


export default Sidebar;