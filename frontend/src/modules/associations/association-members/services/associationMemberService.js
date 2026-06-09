import api from "../../../../services/api/axios";

const associationMemberService = {

  // =========================
  // GET ALL MEMBERS
  // =========================

  getAll: async () => {

    const response =
      await api.get(
        "/associations/association-members/"
      );

    return response.data;
  },

  // =========================
  // GET SINGLE MEMBER
  // =========================

  getById: async (id) => {

    const response =
      await api.get(
        `/associations/association-members/${id}/`
      );

    return response.data;
  },

  // =========================
  // CREATE MEMBER
  // =========================

  create: async (data) => {

    const response =
      await api.post(
        "/associations/association-members/",
        data
      );

    return response.data;
  },

  // =========================
  // UPDATE MEMBER
  // =========================

  update: async (
    id,
    data
  ) => {

    const response =
      await api.put(
        `/associations/association-members/${id}/`,
        data
      );

    return response.data;
  },

  // =========================
  // DELETE MEMBER
  // =========================

  delete: async (id) => {

    const response =
      await api.delete(
        `/associations/association-members/${id}/`
      );

    return response.data;
  },
};

export default associationMemberService;