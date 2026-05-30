import api from "../../services/api";

const feesService = {

  getFees: async () => {
    const response = await api.get(
      "/fees/"
    );

    return response.data;
  },

  collectFees: async (data) => {
    const response = await api.post(
      "/fees/",
      data
    );

    return response.data;
  },

};

export default feesService;