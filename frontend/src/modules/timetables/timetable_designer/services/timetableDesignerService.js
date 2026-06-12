import api
    from '../../../../services/api/axios';

export const GENERATE_ENDPOINT =
    '/timetables/timetable-designer/generate/';

export const MOVE_ENDPOINT =
    '/timetables/timetable-designer/move-entry/';

export const CONFLICTS_ENDPOINT =
    '/timetables/timetable-designer/conflicts/';

export const TEACHER_VIEW_ENDPOINT =
    '/timetables/timetable-designer/teacher-view/';

export const ROOM_VIEW_ENDPOINT =
    '/timetables/timetable-designer/room-view/';

export const CLASS_VIEW_ENDPOINT =
    '/timetables/timetable-designer/class-view/';

const timetableDesignerService = {

    generate: (
        timetableId
    ) =>
        api.post(
            GENERATE_ENDPOINT,
            {
                timetable: timetableId,
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

};

export default timetableDesignerService;