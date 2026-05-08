import api from "./api";

const communicationService = {

  sendNotification: async (data) => {
    const response = await api.post(
      "/communication/send/",
      data
    );

    return response.data;
  },

};

export default communicationService;