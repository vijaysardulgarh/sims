import api from "../../../../services/api/axios";

const associationService = {

  // =========================
  // GET ALL ASSOCIATIONS
  // =========================

  getAssociations: async () => {

    const response =
      await api.get(
        "/associations/associations/"
      );

    return response.data;
  },

  // =========================
  // GET SINGLE ASSOCIATION
  // =========================

  getAssociation: async (id) => {

    const response =
      await api.get(
        `/associations/associations/${id}/`
      );

    return response.data;
  },

  // =========================
  // CREATE ASSOCIATION
  // =========================

  createAssociation: async (data) => {

    const response =
      await api.post(
        "/associations/associations/",
        data
      );

    return response.data;
  },

  // =========================
  // UPDATE ASSOCIATION
  // =========================

  updateAssociation: async (
    id,
    data
  ) => {

    const response =
      await api.put(
        `/associations/associations/${id}/`,
        data
      );

    return response.data;
  },

  // =========================
  // DELETE ASSOCIATION
  // =========================

  deleteAssociation: async (id) => {

    const response =
      await api.delete(
        `/associations/associations/${id}/`
      );

    return response.data;
  },
};

export default associationService;