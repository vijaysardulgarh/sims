import api
    from '../../../../services/api/axios';

export const ENDPOINT =
    '/timetables/substitute-assignments/';

export const LIST_PATH =
    '/dashboard/timetables/substitute-assignments';

export const ADD_PATH =
    '/dashboard/timetables/substitute-assignments/add';

export const EDIT_PATH =
    '/dashboard/timetables/substitute-assignments/edit';

const substituteAssignmentService = {

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

    patch: (
        id,
        data
    ) =>
        api.patch(
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

export default substituteAssignmentService;