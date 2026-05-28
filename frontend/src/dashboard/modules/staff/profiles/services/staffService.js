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
      "/staff/staff-profiles/"
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
      `/staff/staff-profiles/${id}/`
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
      "/staff/staff-profiles/",
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
      `/staff/staff-profiles/${id}/`,
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
      `/staff/staff-profiles/${id}/`
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