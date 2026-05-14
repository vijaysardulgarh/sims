import api from "../../services/api";

const attendanceService = {

  getAttendance: async () => {
    const response = await api.get(
      "/attendance/"
    );

    return response.data;
  },

  markAttendance: async (data) => {
    const response = await api.post(
      "/attendance/",
      data
    );

    return response.data;
  },

};

export default attendanceService;