import api
    from '../../../../services/api/axios';

export const GENERATE_ENDPOINT =
    '/timetables/timetable-designer/generate/';

export const MOVE_ENDPOINT =
    '/timetables/timetable-designer/move-entry/';

export const CONFLICTS_ENDPOINT =
    '/timetables/timetable-designer/conflicts/';

export const GRID_ENDPOINT =
    '/timetables/timetable-designer/grid/';

export const ASSIGN_SUBJECT_ENDPOINT =
    '/timetables/timetable-designer/assign-subject/';

export const ASSIGN_TEACHER_ENDPOINT =
    '/timetables/timetable-designer/assign-teacher/';

export const ASSIGN_ROOM_ENDPOINT =
    '/timetables/timetable-designer/assign-room/';

const timetableDesignerService = {

    generate: (
        timetableId
    ) =>
        api.post(
            GENERATE_ENDPOINT,
            {
                timetable:
                    timetableId,
            }
        ),

    moveEntry: (
        payload
    ) =>
        api.post(
            MOVE_ENDPOINT,
            payload
        ),

    getConflicts: () =>
        api.get(
            CONFLICTS_ENDPOINT
        ),

    getGrid: (
        timetableId
    ) =>
        api.get(
            `${GRID_ENDPOINT}${timetableId}/`
        ),

    assignSubject: (
        payload
    ) =>
        api.post(
            ASSIGN_SUBJECT_ENDPOINT,
            payload
        ),

    assignTeacher: (
        payload
    ) =>
        api.post(
            ASSIGN_TEACHER_ENDPOINT,
            payload
        ),

    assignRoom: (
        payload
    ) =>
        api.post(
            ASSIGN_ROOM_ENDPOINT,
            payload
        ),

};

export default timetableDesignerService;