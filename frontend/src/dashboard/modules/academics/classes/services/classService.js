import api from "../../../../../services/api/axios";

const classService = {

  // =========================
  // GET ALL CLASSES
  // =========================

  getClasses: async () => {

    const response =
      await api.get(
        "/academics/classes/"
      );

    return response.data;
  },

  // =========================
  // GET SINGLE CLASS
  // =========================

  getClass: async (id) => {

    const response =
      await api.get(
        `/academics/classes/${id}/`
      );

    return response.data;
  },

  // =========================
  // CREATE CLASS
  // =========================

  createClass: async (data) => {

    const response =
      await api.post(
        "/academics/classes/",
        data
      );

    return response.data;
  },

  // =========================
  // UPDATE CLASS
  // =========================

  updateClass: async (
    id,
    data
  ) => {

    const response =
      await api.put(

        `/academics/classes/${id}/`,

        data
      );

    return response.data;
  },

  // =========================
  // DELETE CLASS
  // =========================

  deleteClass: async (id) => {

    const response =
      await api.delete(
        `/academics/classes/${id}/`
      );

    return response.data;
  },
};

export default classService;