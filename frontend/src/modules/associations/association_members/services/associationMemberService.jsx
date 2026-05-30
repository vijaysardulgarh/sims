import api from '../../../../services/api/axios';

const BASE_URL =
    '/associations/association-members/';

const associationMemberService = {

    getAll: async () =>
        await api.get(BASE_URL),

    getById: async (id) =>
        await api.get(
            `${BASE_URL}${id}/`
        ),

    create: async (data) =>
        await api.post(
            BASE_URL,
            data
        ),

    update: async (id, data) =>
        await api.put(
            `${BASE_URL}${id}/`,
            data
        ),

    delete: async (id) =>
        await api.delete(
            `${BASE_URL}${id}/`
        ),
};

export default associationMemberService;