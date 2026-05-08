import api from "./api";

const transportService = {

  getRoutes: async () => {
    const response = await api.get(
      "/transport/routes/"
    );

    return response.data;
  },

};

export default transportService;