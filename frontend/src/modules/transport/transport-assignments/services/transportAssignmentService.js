import api from "@/services/api";

const BASE_URL =
    "/transport/transport-assignments/";


const transportAssignmentService = {

    getAssignments: async () => {

        const response = await api.get(
            BASE_URL
        );

        return response.data;
    },

    getAssignment: async (id) => {

        const response = await api.get(
            `${BASE_URL}${id}/`
        );

        return response.data;
    },

    createAssignment: async (data) => {

        const response = await api.post(
            BASE_URL,
            data
        );

        return response.data;
    },

    updateAssignment: async (id, data) => {

        const response = await api.put(
            `${BASE_URL}${id}/`,
            data
        );

        return response.data;
    },

    deleteAssignment: async (id) => {

        const response = await api.delete(
            `${BASE_URL}${id}/`
        );

        return response.data;
    },
};

export default transportAssignmentService;