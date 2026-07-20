import api from "../../../../services/api/axios";

export const ENDPOINT =
    "/timetables/teacher-availabilities/";

export const LIST_PATH =
    "/dashboard/timetables/teacher-availabilities";

export const ADD_PATH =
    "/dashboard/timetables/teacher-availabilities/add";

export const EDIT_PATH =
    "/dashboard/timetables/teacher-availabilities/edit";

const teacherAvailabilityService = {

    endpoint: ENDPOINT,

    // ============================================
    // CRUD
    // ============================================

    getAll: (params = {}) =>
        api.get(
            ENDPOINT,
            {
                params,
            }
        ),

    getById: (id) =>
        api.get(
            `${ENDPOINT}${id}/`
        ),

    create: (data) =>
        api.post(
            ENDPOINT,
            data
        ),

    update: (id, data) =>
        api.put(
            `${ENDPOINT}${id}/`,
            data
        ),

    delete: (id) =>
        api.delete(
            `${ENDPOINT}${id}/`
        ),

    // ============================================
    // TEACHERS
    // ============================================

    getTeachers: () =>
        api.get(
            `${ENDPOINT}teachers/`
        ),

    // ============================================
    // BULK MATRIX
    // ============================================

    getBulkMatrix: (params = {}) =>
        api.get(
            `${ENDPOINT}bulk-matrix/`,
            {
                params,
            }
        ),

    bulkSave: (data) =>
        api.post(
            `${ENDPOINT}bulk-save/`,
            data
        ),

};

export default teacherAvailabilityService;