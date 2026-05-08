import api from "./api";

const examService = {

  getExams: async () => {
    const response = await api.get(
      "/exams/"
    );

    return response.data;
  },

};

export default examService;