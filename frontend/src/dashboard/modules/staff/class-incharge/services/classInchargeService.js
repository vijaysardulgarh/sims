// ============================================
// CLASS INCHARGE SERVICE
// File: classInchargeService.js
// ============================================

import api from "../../../../../services/api/axios";

// ============================================
// GET ALL CLASS INCHARGES
// ============================================

const getClassIncharges = async () => {

  const response =
    await api.get(
      "/staff/class-incharge/"
    );

  return response.data;
};

// ============================================
// GET SINGLE CLASS INCHARGE
// ============================================

const getClassIncharge = async (
  id
) => {

  const response =
    await api.get(
      `/staff/class-incharge/${id}/`
    );

  return response.data;
};

// ============================================
// CREATE CLASS INCHARGE
// ============================================

const createClassIncharge = async (
  data
) => {

  const response =
    await api.post(
      "/staff/class-incharge/",
      data
    );

  return response.data;
};

// ============================================
// UPDATE CLASS INCHARGE
// ============================================

const updateClassIncharge = async (
  id,
  data
) => {

  const response =
    await api.put(
      `/staff/class-incharge/${id}/`,
      data
    );

  return response.data;
};

// ============================================
// DELETE CLASS INCHARGE
// ============================================

const deleteClassIncharge = async (
  id
) => {

  const response =
    await api.delete(
      `/staff/class-incharge/${id}/`
    );

  return response.data;
};

// ============================================
// EXPORT SERVICE
// ============================================

const classInchargeService = {

  getClassIncharges,

  getClassIncharge,

  createClassIncharge,

  updateClassIncharge,

  deleteClassIncharge,
};

export default classInchargeService;