// ============================================
// POST TYPE SERVICE
// File: postTypeService.js
// ============================================

import api from "../../../utils/api";

// ============================================
// GET ALL POST TYPES
// ============================================

const getPostTypes = async () => {

  const response =
    await api.get(
      "/staff/post-types/"
    );

  return response.data;
};

// ============================================
// GET SINGLE POST TYPE
// ============================================

const getPostType = async (id) => {

  const response =
    await api.get(
      `/staff/post-types/${id}/`
    );

  return response.data;
};

// ============================================
// CREATE POST TYPE
// ============================================

const createPostType = async (
  data
) => {

  const response =
    await api.post(
      "/staff/post-types/",
      data
    );

  return response.data;
};

// ============================================
// UPDATE POST TYPE
// ============================================

const updatePostType = async (
  id,
  data
) => {

  const response =
    await api.put(
      `/staff/post-types/${id}/`,
      data
    );

  return response.data;
};

// ============================================
// DELETE POST TYPE
// ============================================

const deletePostType = async (
  id
) => {

  const response =
    await api.delete(
      `/staff/post-types/${id}/`
    );

  return response.data;
};

// ============================================
// EXPORT
// ============================================

const postTypeService = {

  getPostTypes,

  getPostType,

  createPostType,

  updatePostType,

  deletePostType,
};

export default postTypeService;