// ============================================
// STAFF DASHBOARD
// File: StaffDashboard.jsx
// ============================================

import {
  useEffect,
  useState
} from "react";

import StaffStats
from "./StaffStats";

import RecentAttendance
from "./RecentAttendance";

import dashboardService
from "./dashboardService";

const StaffDashboard = () => {

  // ============================================
  // STATES
  // ============================================

  const [dashboardData,
    setDashboardData] =
    useState({});

  const [loading, setLoading] =
    useState(true);

  // ============================================
  // FETCH
  // ============================================

  useEffect(() => {

    fetchDashboard();

  }, []);

  const fetchDashboard = async () => {

    try {

      const response =
        await dashboardService.getStaffDashboard();

      setDashboardData(response);

    } catch (error) {

      console.log(error);

    } finally {

      setLoading(false);
    }
  };

  // ============================================
  // LOADING
  // ============================================

  if (loading) {

    return (

      <div className="p-6">

        Loading dashboard...

      </div>
    );
  }

  // ============================================
  // UI
  // ============================================

  return (

    <div className="space-y-6">

      {/* HEADER */}

      <div>

        <h1 className="
          text-3xl
          font-bold
          text-gray-800
        ">

          Staff Dashboard

        </h1>

        <p className="
          text-gray-500
          mt-1
        ">

          Staff management overview

        </p>

      </div>

      {/* STATS */}

      <StaffStats
        stats={dashboardData.stats}
      />

      {/* RECENT ATTENDANCE */}

      <RecentAttendance />

    </div>
  );
};

export default StaffDashboard;