// ============================================
// TIMETABLE SLOT SERVICE
// File: timetableSlotService.js
// ============================================

import api from "../../../../utils/api";

// ============================================
// GET ALL TIMETABLE SLOTS
// ============================================

const getTimetableSlots = async () => {

  const response =
    await api.get(
      "/academics/timetable-slots/"
    );

  return response.data;
};

// ============================================
// GET SINGLE TIMETABLE SLOT
// ============================================

const getTimetableSlot = async (
  id
) => {

  const response =
    await api.get(
      `/academics/timetable-slots/${id}/`
    );

  return response.data;
};

// ============================================
// CREATE TIMETABLE SLOT
// ============================================

const createTimetableSlot = async (
  data
) => {

  const response =
    await api.post(
      "/academics/timetable-slots/",
      data
    );

  return response.data;
};

// ============================================
// UPDATE TIMETABLE SLOT
// ============================================

const updateTimetableSlot = async (
  id,
  data
) => {

  const response =
    await api.put(
      `/academics/timetable-slots/${id}/`,
      data
    );

  return response.data;
};

// ============================================
// DELETE TIMETABLE SLOT
// ============================================

const deleteTimetableSlot = async (
  id
) => {

  const response =
    await api.delete(
      `/academics/timetable-slots/${id}/`
    );

  return response.data;
};

// ============================================
// EXPORT SERVICE
// ============================================

const timetableSlotService = {

  getTimetableSlots,

  getTimetableSlot,

  createTimetableSlot,

  updateTimetableSlot,

  deleteTimetableSlot,
};

export default timetableSlotService;