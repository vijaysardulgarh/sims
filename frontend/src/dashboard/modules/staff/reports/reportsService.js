// ============================================
// REPORT SERVICE
// File: reportService.js
// ============================================

import api from "../../../utils/api";

// ============================================
// STAFF REPORT
// ============================================

const getStaffReport =
  async () => {

  const response =
    await api.get(
      "/staff/reports/staff/"
    );

  return response.data;
};

// ============================================
// ATTENDANCE REPORT
// ============================================

const getAttendanceReport =
  async () => {

  const response =
    await api.get(
      "/staff/reports/attendance/"
    );

  return response.data;
};

// ============================================
// VACANCY REPORT
// ============================================

const getVacancyReport =
  async () => {

  const response =
    await api.get(
      "/staff/reports/vacancy/"
    );

  return response.data;
};

// ============================================
// WORKLOAD REPORT
// ============================================

const getWorkloadReport =
  async () => {

  const response =
    await api.get(
      "/staff/reports/workload/"
    );

  return response.data;
};

// ============================================
// EXPORT
// ============================================

const reportService = {

  getStaffReport,

  getAttendanceReport,

  getVacancyReport,

  getWorkloadReport,
};

export default reportService;