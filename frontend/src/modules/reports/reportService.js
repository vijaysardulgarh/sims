import api from "../../services/api";

const reportService = {

  getReports: async () => {
    const response = await api.get(
      "/reports/"
    );

    return response.data;
  },

};

export default reportService;