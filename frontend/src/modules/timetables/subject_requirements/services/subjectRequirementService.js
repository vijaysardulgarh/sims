import api
    from '../../../../services/api/axios';

export const ENDPOINT =
    '/timetables/subject-requirements/';

export const LIST_PATH =
    '/dashboard/timetables/subject-requirements';

export const ADD_PATH =
    '/dashboard/timetables/subject-requirements/add';

export const EDIT_PATH =
    '/dashboard/timetables/subject-requirements/edit';

const subjectRequirementService = {

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

export default subjectRequirementService;