import api from "../../../../services/api/axios";

export const ENDPOINT =
    "/timetables/teacher-workloads/";

export const SAVE_ENDPOINT =
    "/timetables/teacher-workloads/save/";

export const LIST_PATH =
    "/dashboard/timetables/teacher-workloads";

const teacherWorkloadService = {

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
            SAVE_ENDPOINT,
            data
        ),

};

export default teacherWorkloadService;