// ============================================
// DAY SERVICE
// File: dayService.js
// ============================================

import api from "../../../../../services/api/axios";

// ============================================
// GET ALL DAYS
// ============================================

const getDays = async () => {

  const response =
    await api.get(
      "/academics/days/"
    );

  return response.data;
};

// ============================================
// GET SINGLE DAY
// ============================================

const getDay = async (id) => {

  const response =
    await api.get(
      `/academics/days/${id}/`
    );

  return response.data;
};

// ============================================
// CREATE DAY
// ============================================

const createDay = async (data) => {

  const response =
    await api.post(
      "/academics/days/",
      data
    );

  return response.data;
};

// ============================================
// UPDATE DAY
// ============================================

const updateDay = async (
  id,
  data
) => {

  const response =
    await api.put(
      `/academics/days/${id}/`,
      data
    );

  return response.data;
};

// ============================================
// DELETE DAY
// ============================================

const deleteDay = async (id) => {

  const response =
    await api.delete(
      `/academics/days/${id}/`
    );

  return response.data;
};

// ============================================
// EXPORT SERVICE
// ============================================

const dayService = {

  getDays,

  getDay,

  createDay,

  updateDay,

  deleteDay,
};

export default dayService;