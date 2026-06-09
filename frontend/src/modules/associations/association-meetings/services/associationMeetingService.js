import api from "../../../../services/api/axios";

const associationMeetingService = {

  // =========================
  // GET ALL MEETINGS
  // =========================

  getAll: async () => {

    const response =
      await api.get(
        "/associations/association-meetings/"
      );

    return response.data;
  },

  // =========================
  // GET SINGLE MEETING
  // =========================

  getById: async (id) => {

    const response =
      await api.get(
        `/associations/association-meetings/${id}/`
      );

    return response.data;
  },

  // =========================
  // CREATE MEETING
  // =========================

  create: async (data) => {

    const response =
      await api.post(
        "/associations/association-meetings/",
        data
      );

    return response.data;
  },

  // =========================
  // UPDATE MEETING
  // =========================

  update: async (
    id,
    data
  ) => {

    const response =
      await api.put(
        `/associations/association-meetings/${id}/`,
        data
      );

    return response.data;
  },

  // =========================
  // DELETE MEETING
  // =========================

  delete: async (id) => {

    const response =
      await api.delete(
        `/associations/association-meetings/${id}/`
      );

    return response.data;
  },

};

export default associationMeetingService;