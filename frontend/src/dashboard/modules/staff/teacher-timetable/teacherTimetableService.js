// ============================================
// TEACHER TIMETABLE SERVICE
// File: teacherTimetableService.js
// ============================================

import api from "../../../../../services/api/axios";

// ============================================
// GET TEACHER TIMETABLE
// ============================================

const getTeacherTimetable =
  async (staffId) => {

  const response =
    await api.get(
      `/staff/teacher-timetable/${staffId}/`
    );

  return response.data;
};

// ============================================
// GET TEACHER WORKLOAD
// ============================================

const getTeacherWorkload =
  async (staffId) => {

  const response =
    await api.get(
      `/staff/teacher-workload/${staffId}/`
    );

  return response.data;
};

// ============================================
// GET FREE PERIODS
// ============================================

const getTeacherFreePeriods =
  async (staffId) => {

  const response =
    await api.get(
      `/staff/teacher-free-periods/${staffId}/`
    );

  return response.data;
};

// ============================================
// EXPORT
// ============================================

const teacherTimetableService = {

  getTeacherTimetable,

  getTeacherWorkload,

  getTeacherFreePeriods,
};

export default teacherTimetableService;