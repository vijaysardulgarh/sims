// ============================================
// TEACHER ATTENDANCE SERVICE
// File: teacherAttendanceService.js
// ============================================

import api from "../../../utils/api";

// ============================================
// GET ALL
// ============================================

const getTeacherAttendance =
  async () => {

  const response =
    await api.get(
      "/staff/teacher-attendance/"
    );

  return response.data;
};

// ============================================
// GET SINGLE
// ============================================

const getTeacherAttendanceById =
  async (id) => {

  const response =
    await api.get(
      `/staff/teacher-attendance/${id}/`
    );

  return response.data;
};

// ============================================
// CREATE
// ============================================

const createTeacherAttendance =
  async (data) => {

  const response =
    await api.post(
      "/staff/teacher-attendance/",
      data
    );

  return response.data;
};

// ============================================
// UPDATE
// ============================================

const updateTeacherAttendance =
  async (
    id,
    data
  ) => {

  const response =
    await api.put(
      `/staff/teacher-attendance/${id}/`,
      data
    );

  return response.data;
};

// ============================================
// DELETE
// ============================================

const deleteTeacherAttendance =
  async (id) => {

  const response =
    await api.delete(
      `/staff/teacher-attendance/${id}/`
    );

  return response.data;
};

// ============================================
// EXPORT
// ============================================

const teacherAttendanceService = {

  getTeacherAttendance,

  getTeacherAttendanceById,

  createTeacherAttendance,

  updateTeacherAttendance,

  deleteTeacherAttendance,
};

export default teacherAttendanceService;