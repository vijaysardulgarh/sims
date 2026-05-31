import api from '../../../../services/api/axios';

const BASE_URL = '/schools/school-settings/';

const schoolSettingService = {

    getSchoolSettings: async () =>
        await api.get(BASE_URL),

    getSchoolSetting: async (id) =>
        await api.get(`${BASE_URL}${id}/`),

    createSchoolSetting: async (data) =>
        await api.post(BASE_URL, data),

    updateSchoolSetting: async (id, data) =>
        await api.put(
            `${BASE_URL}${id}/`,
            data
        ),

    deleteSchoolSetting: async (id) =>
        await api.delete(
            `${BASE_URL}${id}/`
        ),
};

export default schoolSettingService;