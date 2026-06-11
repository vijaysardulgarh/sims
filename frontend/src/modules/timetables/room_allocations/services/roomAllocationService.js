import api
    from '../../../../services/api/axios';

export const ENDPOINT =
    '/timetables/room-allocations/';

export const LIST_PATH =
    '/dashboard/timetables/room-allocations';

export const ADD_PATH =
    '/dashboard/timetables/room-allocations/add';

export const EDIT_PATH =
    '/dashboard/timetables/room-allocations/edit';

const roomAllocationService = {

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

export default roomAllocationService;