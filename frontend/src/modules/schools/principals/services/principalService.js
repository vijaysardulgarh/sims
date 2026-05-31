import api from '../../../../services/api/axios';

const BASE_URL = '/schools/principals/';

const principalService = {

    getPrincipals: async () =>
        await api.get(BASE_URL),

    getPrincipal: async (id) =>
        await api.get(`${BASE_URL}${id}/`),

    createPrincipal: async (data) =>
        await api.post(BASE_URL, data),

    updatePrincipal: async (id, data) =>
        await api.put(
            `${BASE_URL}${id}/`,
            data
        ),

    deletePrincipal: async (id) =>
        await api.delete(
            `${BASE_URL}${id}/`
        ),
};

export default principalService;