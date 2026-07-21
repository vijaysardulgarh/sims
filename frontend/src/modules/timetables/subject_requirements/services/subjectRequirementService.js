import api from '../../../../services/api/axios';

export const ENDPOINT = '/timetables/subject-requirements/';

export const LIST_PATH = '/dashboard/timetables/subject-requirements';

const subjectRequirementService = {
  endpoint: ENDPOINT,

  getAll: (params = {}) => 
    api.get(ENDPOINT, { params }),

  bulkSave: (rows) => 
    api.post(`${ENDPOINT}bulk-save/`, rows),

  refresh: (params = {}) => 
    api.get(ENDPOINT, { params }),

  exportExcel: () =>
    api.get(`${ENDPOINT}export/`, {
      responseType: "blob",
    }),

  importExcel: (formData) =>
    api.post(`${ENDPOINT}import/`, formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    }),
};

export default subjectRequirementService;