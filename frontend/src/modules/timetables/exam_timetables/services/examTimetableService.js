import api
    from '../../../../services/api/axios';

export const ENDPOINT =
    '/timetables/exam-timetables/';

export const LIST_PATH =
    '/dashboard/timetables/exam-timetables';

export const ADD_PATH =
    '/dashboard/timetables/exam-timetables/add';

export const EDIT_PATH =
    '/dashboard/timetables/exam-timetables/edit';

const examTimetableService = {

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

    getById: (
        id
    ) =>
        api.get(
            `${ENDPOINT}${id}/`
        ),

    create: (
        data
    ) =>
        api.post(
            ENDPOINT,
            data
        ),

    update: (
        id,
        data
    ) =>
        api.put(
            `${ENDPOINT}${id}/`,
            data
        ),

    delete: (
        id
    ) =>
        api.delete(
            `${ENDPOINT}${id}/`
        ),

};

export default examTimetableService;