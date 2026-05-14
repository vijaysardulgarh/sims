import api from "../../services/api";

const examService = {

  getExams: async () => {
    const response = await api.get(
      "/exams/"
    );

    return response.data;
  },

};

export default examService;