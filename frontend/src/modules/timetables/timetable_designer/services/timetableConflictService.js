import api
    from '../../../../services/api/axios';

export const ENDPOINT =
    '/timetables/timetable-designer/conflicts/';

const timetableConflictService = {

    getAll: () =>

        api.get(
            ENDPOINT
        ),

};

export default timetableConflictService;