// ============================================
// MEDIUM SERVICE
// File: mediumService.js
// ============================================

import api from "../../../utils/api";

// ============================================
// GET ALL MEDIUMS
// ============================================

const getMediums = async () => {

  const response =
    await api.get(
      "/academics/mediums/"
    );

  return response.data;
};

// ============================================
// GET SINGLE MEDIUM
// ============================================

const getMedium = async (id) => {

  const response =
    await api.get(
      `/academics/mediums/${id}/`
    );

  return response.data;
};

// ============================================
// CREATE MEDIUM
// ============================================

const createMedium = async (data) => {

  const response =
    await api.post(
      "/academics/mediums/",
      data
    );

  return response.data;
};

// ============================================
// UPDATE MEDIUM
// ============================================

const updateMedium = async (
  id,
  data
) => {

  const response =
    await api.put(
      `/academics/mediums/${id}/`,
      data
    );

  return response.data;
};

// ============================================
// DELETE MEDIUM
// ============================================

const deleteMedium = async (id) => {

  const response =
    await api.delete(
      `/academics/mediums/${id}/`
    );

  return response.data;
};

// ============================================
// EXPORT SERVICE
// ============================================

const mediumService = {

  getMediums,

  getMedium,

  createMedium,

  updateMedium,

  deleteMedium,
};

export default mediumService;