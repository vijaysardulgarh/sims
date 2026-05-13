// ============================================
// DASHBOARD SERVICE
// File: dashboardService.js
// ============================================

import api from "../../../utils/api";

// ============================================
// STAFF DASHBOARD
// ============================================

const getStaffDashboard =
  async () => {

  const response =
    await api.get(
      "/staff/dashboard/"
    );

  return response.data;
};

// ============================================
// RECENT ATTENDANCE
// ============================================

const getRecentAttendance =
  async () => {

  const response =
    await api.get(
      "/staff/dashboard/recent-attendance/"
    );

  return response.data;
};

// ============================================
// STAFF STATS
// ============================================

const getStaffStats =
  async () => {

  const response =
    await api.get(
      "/staff/dashboard/stats/"
    );

  return response.data;
};

// ============================================
// EXPORT
// ============================================

const dashboardService = {

  getStaffDashboard,

  getRecentAttendance,

  getStaffStats,
};

export default dashboardService;