import { Outlet } from "react-router-dom";

import Sidebar from "../components/Sidebar";

import TopNavbar from "../components/TopNavbar";

const DashboardLayout = () => {

  return (

    <div
      className="
        h-screen
        overflow-hidden
        bg-gray-100
        flex
      "
    >

      {/* ===================================== */}
      {/* SIDEBAR */}
      {/* ===================================== */}

      <Sidebar />

      {/* ===================================== */}
      {/* MAIN CONTENT */}
      {/* ===================================== */}

      <div
        className="
          flex-1
          flex
          flex-col
          overflow-hidden
        "
      >

        {/* ===================================== */}
        {/* TOP NAVBAR */}
        {/* ===================================== */}

        <TopNavbar />

        {/* ===================================== */}
        {/* PAGE CONTENT */}
        {/* ===================================== */}

        <main
          className="
            flex-1
            overflow-y-auto
            overflow-x-hidden
            p-6
            custom-scrollbar
          "
        >

          <Outlet />

        </main>

      </div>

    </div>

  );
};

export default DashboardLayout;