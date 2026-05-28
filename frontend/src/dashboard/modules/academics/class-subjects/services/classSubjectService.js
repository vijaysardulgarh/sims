// ============================================
// CLASS SUBJECT SERVICE
// File: classSubjectService.js
// ============================================

import api from "../../../../../services/api/axios";

// ============================================
// GET ALL CLASS SUBJECTS
// ============================================

const getClassSubjects = async () => {

  const response =
    await api.get(
      "/academics/class-subjects/"
    );

  return response.data;
};

// ============================================
// GET SINGLE CLASS SUBJECT
// ============================================

const getClassSubject = async (id) => {

  const response =
    await api.get(
      `/academics/class-subjects/${id}/`
    );

  return response.data;
};

// ============================================
// CREATE CLASS SUBJECT
// ============================================

const createClassSubject = async (
  data
) => {

  const response =
    await api.post(
      "/academics/class-subjects/",
      data
    );

  return response.data;
};

// ============================================
// UPDATE CLASS SUBJECT
// ============================================

const updateClassSubject = async (
  id,
  data
) => {

  const response =
    await api.put(
      `/academics/class-subjects/${id}/`,
      data
    );

  return response.data;
};

// ============================================
// DELETE CLASS SUBJECT
// ============================================

const deleteClassSubject = async (
  id
) => {

  const response =
    await api.delete(
      `/academics/class-subjects/${id}/`
    );

  return response.data;
};

// ============================================
// EXPORT SERVICE
// ============================================

const classSubjectService = {

  getClassSubjects,

  getClassSubject,

  createClassSubject,

  updateClassSubject,

  deleteClassSubject,
};

export default classSubjectService;