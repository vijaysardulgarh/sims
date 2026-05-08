import api from "./api";

const academicService = {

  getClasses: async () => {
    const response = await api.get(
      "/academics/classes/"
    );

    return response.data;
  },

  getSubjects: async () => {
    const response = await api.get(
      "/academics/subjects/"
    );

    return response.data;
  },

};

export default academicService;