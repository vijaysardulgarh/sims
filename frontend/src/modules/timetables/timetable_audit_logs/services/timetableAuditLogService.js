import api
    from '../../../../services/api/axios';

export const ENDPOINT =
    '/timetables/timetable-audit-logs/';

export const LIST_PATH =
    '/dashboard/timetables/timetable-audit-logs';

export const ADD_PATH =
    '/dashboard/timetables/timetable-audit-logs/add';

export const EDIT_PATH =
    '/dashboard/timetables/timetable-audit-logs/edit';

const timetableAuditLogService = {

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

};

export default timetableAuditLogService;