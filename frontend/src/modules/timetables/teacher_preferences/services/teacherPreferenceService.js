import api from "../../../../services/api/axios";

export const ENDPOINT =
    "/timetables/teacher-preferences/";

export const LIST_PATH =
    "/dashboard/timetables/teacher-preferences";

const teacherPreferenceService = {

    endpoint: ENDPOINT,

    getAll: (
        params = {}
    ) =>
        api.get(
            ENDPOINT,
            {
                params,
            }
        ),

    saveAll: (
        data
    ) =>
        api.post(
            `${ENDPOINT}save/`,
            data
        ),

};

export default teacherPreferenceService;