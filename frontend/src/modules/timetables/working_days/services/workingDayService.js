import api from "../../../../services/api/axios";

export const ENDPOINT =
    "/timetables/working-days/";

export const LIST_PATH =
    "/dashboard/timetables/working-days";

const workingDayService = {

    endpoint: ENDPOINT,

    /**
     * Get all working days
     */
    getAll: (params = {}) =>
        api.get(
            ENDPOINT,
            {
                params,
            },
        ),

    /**
     * Save all working days
     */
    save: (data) =>
        api.post(
            `${ENDPOINT}save/`,
            data,
        ),

};

export default workingDayService;