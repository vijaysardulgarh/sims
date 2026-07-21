import api from '../../../../services/api/axios';

export const ENDPOINT =
    '/timetables/subject-constraints/';

export const LIST_PATH =
    '/dashboard/timetables/subject-constraints';

const subjectConstraintService = {

    endpoint: ENDPOINT,

    getAll: (
        params = {},
    ) =>
        api.get(
            ENDPOINT,
            {
                params,
            },
        ),

    bulkSave: (
        data,
    ) =>
        api.post(
            `${ENDPOINT}bulk-save/`,
            data,
        ),

};

export default subjectConstraintService;