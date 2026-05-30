// ============================================
// TIMETABLE SERVICE
// File: timetableService.js
// ============================================

import api from "../../../../services/api/axios";

// ============================================
// GET ALL TIMETABLES
// ============================================

const getTimetables = async () => {

  const response =
    await api.get(
      "/academics/timetable/"
    );

  return response.data;
};

// ============================================
// GET SINGLE TIMETABLE
// ============================================

const getTimetable = async (id) => {

  const response =
    await api.get(
      `/academics/timetable/${id}/`
    );

  return response.data;
};

// ============================================
// CREATE TIMETABLE
// ============================================

const createTimetable = async (
  data
) => {

  const response =
    await api.post(
      "/academics/timetable/",
      data
    );

  return response.data;
};

// ============================================
// UPDATE TIMETABLE
// ============================================

const updateTimetable = async (
  id,
  data
) => {

  const response =
    await api.put(
      `/academics/timetable/${id}/`,
      data
    );

  return response.data;
};

// ============================================
// DELETE TIMETABLE
// ============================================

const deleteTimetable = async (
  id
) => {

  const response =
    await api.delete(
      `/academics/timetable/${id}/`
    );

  return response.data;
};

// ============================================
// GENERATE TIMETABLE
// ============================================

const generateTimetable = async (
  data
) => {

  const response =
    await api.post(
      "/academics/timetable/generate/",
      data
    );

  return response.data;
};

// ============================================
// EXPORT SERVICE
// ============================================

const timetableService = {

  getTimetables,

  getTimetable,

  createTimetable,

  updateTimetable,

  deleteTimetable,

  generateTimetable,
};

export default timetableService;