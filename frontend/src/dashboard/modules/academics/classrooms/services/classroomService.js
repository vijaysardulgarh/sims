// ============================================
// CLASSROOM SERVICE
// File: classroomService.js
// ============================================

import api from "../../../../../services/api/axios";

// ============================================
// GET ALL CLASSROOMS
// ============================================

const getClassrooms = async () => {

  const response =
    await api.get(
      "/academics/classrooms/"
    );

  return response.data;
};

// ============================================
// GET SINGLE CLASSROOM
// ============================================

const getClassroom = async (id) => {

  const response =
    await api.get(
      `/academics/classrooms/${id}/`
    );

  return response.data;
};

// ============================================
// CREATE CLASSROOM
// ============================================

const createClassroom = async (data) => {

  const response =
    await api.post(
      "/academics/classrooms/",
      data
    );

  return response.data;
};

// ============================================
// UPDATE CLASSROOM
// ============================================

const updateClassroom = async (
  id,
  data
) => {

  const response =
    await api.put(
      `/academics/classrooms/${id}/`,
      data
    );

  return response.data;
};

// ============================================
// DELETE CLASSROOM
// ============================================

const deleteClassroom = async (id) => {

  const response =
    await api.delete(
      `/academics/classrooms/${id}/`
    );

  return response.data;
};

// ============================================
// EXPORT
// ============================================

const classroomService = {

  getClassrooms,

  getClassroom,

  createClassroom,

  updateClassroom,

  deleteClassroom,
};

export default classroomService;