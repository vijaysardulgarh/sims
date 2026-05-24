import {
    useAuth
} from "../../modules/access_control/auth/context/AuthContext";

import StatCard
from "../components/StatCard";

import QuickActions
from "../components/QuickActions";
  
  
  const DashboardHomePage = () => {
  
    const {
      user
    } = useAuth();
  
    const roles =
      user?.roles || [];
  
  
    return (
  
      <div className="space-y-6">
  
        {/* HEADER */}
        <div>
  
          <h1 className="text-3xl font-bold text-gray-800">
  
            Welcome Back
  
          </h1>
  
          <p className="text-gray-500 mt-2">
  
            {user?.school_name}
  
          </p>
  
        </div>
  
  
        {/* STATS */}
        <div
          className="
            grid
            grid-cols-1
            md:grid-cols-2
            xl:grid-cols-4
            gap-6
          "
        >
  
          <StatCard
            title="Students"
            value="2,540"
          />
  
          <StatCard
            title="Teachers"
            value="120"
          />
  
          <StatCard
            title="Attendance"
            value="94%"
          />
  
          <StatCard
            title="Fees Collected"
            value="₹12.4L"
          />
  
        </div>
  
  
        {/* QUICK ACTIONS */}
        <QuickActions />
  
  
        {/* ROLE BASED CONTENT */}
  
        {
          roles.includes(
            "PRINCIPAL"
          ) && (
  
            <div
              className="
                bg-white
                rounded-2xl
                p-6
                shadow-sm
              "
            >
  
              <h2 className="text-xl font-bold mb-4">
  
                Principal Overview
  
              </h2>
  
              <p className="text-gray-600">
  
                School performance analytics,
                attendance trends,
                examination insights,
                and staff monitoring.
  
              </p>
  
            </div>
          )
        }
  
  
        {
          roles.includes(
            "TEACHER"
          ) && (
  
            <div
              className="
                bg-white
                rounded-2xl
                p-6
                shadow-sm
              "
            >
  
              <h2 className="text-xl font-bold mb-4">
  
                Teacher Dashboard
  
              </h2>
  
              <p className="text-gray-600">
  
                Today's timetable,
                pending homework,
                assignments,
                and attendance tasks.
  
              </p>
  
            </div>
          )
        }
  
      </div>
    );
  };
  
  export default DashboardHomePage;