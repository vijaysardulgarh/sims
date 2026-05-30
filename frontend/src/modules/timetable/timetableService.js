import api from "../../services/api";

const timetableService = {

  getTimetable: async () => {
    const response = await api.get(
      "/timetable/"
    );

    return response.data;
  },

};

export default timetableService;