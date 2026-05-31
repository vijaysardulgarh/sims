import api from '../../../../services/api/axios';

const BASE_URL = '/schools/branches/';

const branchService = {

    getBranches: async () =>
        await api.get(BASE_URL),

    getBranch: async (id) =>
        await api.get(`${BASE_URL}${id}/`),

    createBranch: async (data) =>
        await api.post(BASE_URL, data),

    updateBranch: async (id, data) =>
        await api.put(
            `${BASE_URL}${id}/`,
            data
        ),

    deleteBranch: async (id) =>
        await api.delete(
            `${BASE_URL}${id}/`
        ),
};

export default branchService;