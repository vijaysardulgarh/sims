// ============================================
// TEACHER ATTENDANCE SERVICE
// File: teacherAttendanceService.js
// ============================================

import api from "../../../../services/api/axios";

// ============================================
// GET ATTENDANCE BY DATE
// ============================================

const getTeacherAttendance = async (date) => {

  const response = await api.get(

    "/staff/teacher-attendance/",

    {
      params: {
        date,
      },
    }

  );

  return response.data;

};

// ============================================
// SAVE BULK ATTENDANCE
// ============================================

const saveTeacherAttendance = async (data) => {

  const response = await api.post(

    "/staff/teacher-attendance/",

    data

  );

  return response.data;

};

// ============================================
// EXPORT
// ============================================

const teacherAttendanceService = {

  getTeacherAttendance,

  saveTeacherAttendance,

};

export default teacherAttendanceService;