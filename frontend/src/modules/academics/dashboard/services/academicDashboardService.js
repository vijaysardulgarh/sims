import api from "../../../../services/api/axios";

const academicDashboardService = {

  // ================================
  // DASHBOARD STATS
  // ================================

  getDashboardStats: async () => {
    return await api.get(
      "/academics/dashboard/stats/"
    );
  },

  // ================================
  // QUICK OVERVIEW
  // ================================

  getAcademicOverview: async () => {
    return await api.get(
      "/academics/dashboard/overview/"
    );
  },

  // ================================
  // TIMETABLE PREVIEW
  // ================================

  getTodayTimetable: async () => {
    return await api.get(
      "/academics/dashboard/timetable-preview/"
    );
  },

  // ================================
  // ALERTS
  // ================================

  getAcademicAlerts: async () => {
    return await api.get(
      "/academics/dashboard/alerts/"
    );
  },

  // ================================
  // REPORTS SUMMARY
  // ================================

  getReportsSummary: async () => {
    return await api.get(
      "/academics/dashboard/reports-summary/"
    );
  },

  // ================================
  // TIMETABLE ANALYTICS
  // ================================

  getTimetableAnalytics: async () => {
    return await api.get(
      "/academics/dashboard/timetable-analytics/"
    );
  },

  // ================================
  // TEACHER WORKLOAD
  // ================================

  getTeacherWorkload: async () => {
    return await api.get(
      "/academics/dashboard/teacher-workload/"
    );
  },

  // ================================
  // SUBJECT STRENGTH
  // ================================

  getSubjectStrength: async () => {
    return await api.get(
      "/academics/dashboard/subject-strength/"
    );
  },

  // ================================
  // CLASS STRENGTH
  // ================================

  getClassStrength: async () => {
    return await api.get(
      "/academics/dashboard/class-strength/"
    );
  },

  // ================================
  // FULL DASHBOARD DATA
  // ================================

  getFullDashboardData: async () => {
    return await api.get(
      "/academics/dashboard/full-data/"
    );
  },

};

export default academicDashboardService;