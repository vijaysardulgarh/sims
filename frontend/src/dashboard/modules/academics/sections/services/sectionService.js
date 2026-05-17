// ============================================
// SECTION SERVICE
// File: sectionService.js
// ============================================

import api from "../../../../../utils/api";

// ============================================
// GET ALL SECTIONS
// ============================================

const getSections = async () => {

  const response =
    await api.get(
      "/academics/sections/"
    );

  return response.data;
};

// ============================================
// GET SINGLE SECTION
// ============================================

const getSection = async (id) => {

  const response =
    await api.get(
      `/academics/sections/${id}/`
    );

  return response.data;
};

// ============================================
// CREATE SECTION
// ============================================

const createSection = async (data) => {

  const response =
    await api.post(
      "/academics/sections/",
      data
    );

  return response.data;
};

// ============================================
// UPDATE SECTION
// ============================================

const updateSection = async (
  id,
  data
) => {

  const response =
    await api.put(
      `/academics/sections/${id}/`,
      data
    );

  return response.data;
};

// ============================================
// DELETE SECTION
// ============================================

const deleteSection = async (id) => {

  const response =
    await api.delete(
      `/academics/sections/${id}/`
    );

  return response.data;
};

// ============================================
// EXPORT SERVICE
// ============================================

const sectionService = {

  getSections,

  getSection,

  createSection,

  updateSection,

  deleteSection,
};

export default sectionService;