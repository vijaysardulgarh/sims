import api from '../../../../services/api/axios';

const BASE_URL = '/schools/about-schools/';

const aboutSchoolService = {

    getAboutSchools: async () =>
        await api.get(BASE_URL),

    getAboutSchool: async (id) =>
        await api.get(`${BASE_URL}${id}/`),

    createAboutSchool: async (data) =>
        await api.post(BASE_URL, data),

    updateAboutSchool: async (id, data) =>
        await api.put(
            `${BASE_URL}${id}/`,
            data
        ),

    deleteAboutSchool: async (id) =>
        await api.delete(
            `${BASE_URL}${id}/`
        ),
};

export default aboutSchoolService;