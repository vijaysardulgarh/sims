import api from "../api";

const classService = {

  getClasses: async () => {

    const response =
      await api.get("/classes/");

    return response.data;
  },

  getClass: async (id) => {

    const response =
      await api.get(`/classes/${id}/`);

    return response.data;
  },

  createClass: async (data) => {

    const response =
      await api.post("/classes/", data);

    return response.data;
  },

  updateClass: async (id, data) => {

    const response =
      await api.put(
        `/classes/${id}/`,
        data
      );

    return response.data;
  },

  deleteClass: async (id) => {

    const response =
      await api.delete(
        `/classes/${id}/`
      );

    return response.data;
  },
};

export default classService;