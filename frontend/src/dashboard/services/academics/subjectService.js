// ============================================
// SUBJECT SERVICE
// File: subjectService.js
// ============================================

import api from "../../../utils/api";

// ============================================
// GET ALL SUBJECTS
// ============================================

const getSubjects = async () => {

  const response =
    await api.get(
      "/academics/subjects/"
    );

  return response.data;
};

// ============================================
// GET SINGLE SUBJECT
// ============================================

const getSubject = async (id) => {

  const response =
    await api.get(
      `/academics/subjects/${id}/`
    );

  return response.data;
};

// ============================================
// CREATE SUBJECT
// ============================================

const createSubject = async (data) => {

  const response =
    await api.post(
      "/academics/subjects/",
      data
    );

  return response.data;
};

// ============================================
// UPDATE SUBJECT
// ============================================

const updateSubject = async (
  id,
  data
) => {

  const response =
    await api.put(
      `/academics/subjects/${id}/`,
      data
    );

  return response.data;
};

// ============================================
// DELETE SUBJECT
// ============================================

const deleteSubject = async (id) => {

  const response =
    await api.delete(
      `/academics/subjects/${id}/`
    );

  return response.data;
};

// ============================================
// EXPORT SERVICE
// ============================================

const subjectService = {

  getSubjects,

  getSubject,

  createSubject,

  updateSubject,

  deleteSubject,
};

export default subjectService;