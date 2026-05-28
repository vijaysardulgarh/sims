// ============================================
// STREAM SERVICE
// File: streamService.js
// ============================================

import api from "../../../../../services/api/axios";

// ============================================
// GET ALL STREAMS
// ============================================

const getStreams = async () => {

  const response =
    await api.get(
      "/academics/streams/"
    );

  return response.data;
};

// ============================================
// GET SINGLE STREAM
// ============================================

const getStream = async (id) => {

  const response =
    await api.get(
      `/academics/streams/${id}/`
    );

  return response.data;
};

// ============================================
// CREATE STREAM
// ============================================

const createStream = async (data) => {

  const response =
    await api.post(
      "/academics/streams/",
      data
    );

  return response.data;
};

// ============================================
// UPDATE STREAM
// ============================================

const updateStream = async (
  id,
  data
) => {

  const response =
    await api.put(
      `/academics/streams/${id}/`,
      data
    );

  return response.data;
};

// ============================================
// DELETE STREAM
// ============================================

const deleteStream = async (id) => {

  const response =
    await api.delete(
      `/academics/streams/${id}/`
    );

  return response.data;
};

// ============================================
// EXPORT SERVICE
// ============================================

const streamService = {

  getStreams,

  getStream,

  createStream,

  updateStream,

  deleteStream,
};

export default streamService;