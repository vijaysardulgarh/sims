import {
  useEffect,
  useState,
} from "react";

import toast from "react-hot-toast";

// ============================================
// COMPONENTS
// ============================================

import AcademicStats from "./components/AcademicStats";

import AcademicOverview from "./components/AcademicOverview";

import AcademicQuickActions from "./components/AcademicQuickActions";

import AcademicReports from "./components/AcademicReports";

import AcademicAlerts from "./components/AcademicAlerts";

import TimetablePreview from "./components/TimetablePreview";

// ============================================
// SHARED COMPONENTS
// ============================================

import DashboardHeader from "../../../shared/components/dashboard/DashboardHeader";

// ============================================
// SERVICES
// ============================================

import academicDashboardService from
"./services/academicDashboardService";

// ============================================
// COMPONENT
// ============================================

const AcademicDashboard = () => {

  // ============================================
  // STATE
  // ============================================

  const [stats, setStats] = useState({
    classes: 0,
    subjects: 0,
    sections: 0,
    timetables: 0,
  });

  const [overview, setOverview] = useState({});

  const [alerts, setAlerts] = useState([]);

  const [timetable, setTimetable] = useState([]);

  const [loading, setLoading] = useState(false);

  // ============================================
  // INITIAL LOAD
  // ============================================

  useEffect(() => {

    fetchDashboardData();

  }, []);

  // ============================================
  // FETCH DASHBOARD DATA
  // ============================================

  const fetchDashboardData = async () => {

    try {

      setLoading(true);

      const [
        statsResponse,
        overviewResponse,
        alertsResponse,
        timetableResponse,
      ] = await Promise.all([

        academicDashboardService.getDashboardStats(),

        academicDashboardService.getAcademicOverview(),

        academicDashboardService.getAcademicAlerts(),

        academicDashboardService.getTodayTimetable(),

      ]);

      // ============================================
      // SET STATE
      // ============================================

      setStats(statsResponse.data || {});

      setOverview(overviewResponse.data || {});

      setAlerts(alertsResponse.data || []);

      setTimetable(timetableResponse.data || []);

    } catch (error) {

      console.error(error);

      toast.error(
        "Failed to load academic dashboard"
      );

    } finally {

      setLoading(false);

    }
  };

  // ============================================
  // RENDER
  // ============================================

  return (

    <div className="space-y-6">

      {/* ===================================== */}
      {/* HEADER */}
      {/* ===================================== */}

      <DashboardHeader
        title="Academics Dashboard"
        subtitle="
          Manage academic operations,
          timetable and reports
        "
        actionButton={

          <button
            className="
              px-5
              py-3
              bg-blue-600
              text-white
              rounded-2xl
              shadow-sm
              hover:bg-blue-700
              transition-all
            "
          >
            Generate Timetable
          </button>

        }
      />

      {/* ===================================== */}
      {/* STATS */}
      {/* ===================================== */}

      <AcademicStats
        stats={stats}
        loading={loading}
      />

      {/* ===================================== */}
      {/* QUICK ACTIONS */}
      {/* ===================================== */}

      <AcademicQuickActions />

      {/* ===================================== */}
      {/* OVERVIEW */}
      {/* ===================================== */}

      <AcademicOverview
        overview={overview}
      />

      {/* ===================================== */}
      {/* TIMETABLE */}
      {/* ===================================== */}

      <TimetablePreview
        timetable={timetable}
      />

      {/* ===================================== */}
      {/* REPORTS */}
      {/* ===================================== */}

      <AcademicReports />

      {/* ===================================== */}
      {/* ALERTS */}
      {/* ===================================== */}

      <AcademicAlerts
        alerts={alerts}
      />

    </div>

  );
};

export default AcademicDashboard;