// ============================================
// SANCTIONED POST SERVICE
// File: sanctionedPostService.js
// ============================================

import api from "../../../utils/api";

// ============================================
// GET ALL
// ============================================

const getSanctionedPosts =
  async () => {

  const response =
    await api.get(
      "/staff/sanctioned-posts/"
    );

  return response.data;
};

// ============================================
// GET SINGLE
// ============================================

const getSanctionedPost =
  async (id) => {

  const response =
    await api.get(
      `/staff/sanctioned-posts/${id}/`
    );

  return response.data;
};

// ============================================
// CREATE
// ============================================

const createSanctionedPost =
  async (data) => {

  const response =
    await api.post(
      "/staff/sanctioned-posts/",
      data
    );

  return response.data;
};

// ============================================
// UPDATE
// ============================================

const updateSanctionedPost =
  async (
    id,
    data
  ) => {

  const response =
    await api.put(
      `/staff/sanctioned-posts/${id}/`,
      data
    );

  return response.data;
};

// ============================================
// DELETE
// ============================================

const deleteSanctionedPost =
  async (id) => {

  const response =
    await api.delete(
      `/staff/sanctioned-posts/${id}/`
    );

  return response.data;
};

// ============================================
// EXPORT
// ============================================

const sanctionedPostService = {

  getSanctionedPosts,

  getSanctionedPost,

  createSanctionedPost,

  updateSanctionedPost,

  deleteSanctionedPost,
};

export default sanctionedPostService;