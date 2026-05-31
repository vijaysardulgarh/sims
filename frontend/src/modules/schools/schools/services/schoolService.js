import api from '../../../../services/api/axios';

const BASE_URL = '/schools/schools/';

const schoolService = {

    getSchools: async (params = {}) =>
        await api.get(BASE_URL, { params }),

    getSchool: async (id) =>
        await api.get(`${BASE_URL}${id}/`),

    createSchool: async (data) =>
        await api.post(BASE_URL, data),

    updateSchool: async (id, data) =>
        await api.put(`${BASE_URL}${id}/`, data),

    deleteSchool: async (id) =>
        await api.delete(`${BASE_URL}${id}/`),
};

export default schoolService;