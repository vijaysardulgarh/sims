import api from "../../services/api";

const libraryService = {

  getBooks: async () => {
    const response = await api.get(
      "/library/books/"
    );

    return response.data;
  },

  issueBook: async (data) => {
    const response = await api.post(
      "/library/issue/",
      data
    );

    return response.data;
  },

};

export default libraryService;