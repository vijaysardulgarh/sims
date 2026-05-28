// ============================================
// STAFF SERVICE
// File: staffService.js
// ============================================

import api from "../../../../../services/api/axios";

// ============================================
// GET ALL STAFF
// ============================================

const getStaff = async () => {

  const response =
    await api.get(
      "/staff/staff/"
    );

  return response.data;
};

// ============================================
// GET SINGLE STAFF
// ============================================

const getStaffMember = async (
  id
) => {

  const response =
    await api.get(
      `/staff/staff/${id}/`
    );

  return response.data;
};

// ============================================
// CREATE STAFF
// ============================================

const createStaff = async (
  data
) => {

  const response =
    await api.post(
      "/staff/staff/",
      data
    );

  return response.data;
};

// ============================================
// UPDATE STAFF
// ============================================

const updateStaff = async (
  id,
  data
) => {

  const response =
    await api.put(
      `/staff/staff/${id}/`,
      data
    );

  return response.data;
};

// ============================================
// DELETE STAFF
// ============================================

const deleteStaff = async (
  id
) => {

  const response =
    await api.delete(
      `/staff/staff/${id}/`
    );

  return response.data;
};

// ============================================
// EXPORT
// ============================================

const staffService = {

  getStaff,

  getStaffMember,

  createStaff,

  updateStaff,

  deleteStaff,
};

export default staffService;