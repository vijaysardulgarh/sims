import { Outlet } from "react-router-dom";
import Sidebar from "../dashboard/components/Sidebar";
import TopNavbar from "../dashboard/components/TopNavbar";

const DashboardLayout = () => {
  return (
    <div className="flex h-screen bg-gray-100 overflow-hidden">
      {/* Sidebar */}
      <Sidebar />

      {/* Main Area */}
      <div className="flex flex-col flex-1 overflow-hidden">
        <TopNavbar />

        <main className="flex-1 overflow-y-auto p-6">
          <Outlet />
        </main>
      </div>
    </div>
  );
};

export default DashboardLayout;