import api from "./api";

const hostelService = {

  getRooms: async () => {
    const response = await api.get(
      "/hostel/rooms/"
    );

    return response.data;
  },

};

export default hostelService;