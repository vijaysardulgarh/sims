import api
    from '../../../../services/api/axios';

export const ENDPOINT =
    '/timetables/timetable-designer/compare/';

const timetableVersionService = {

    compare: (
        payload
    ) =>

        api.post(
            ENDPOINT,
            payload
        ),

};

export default timetableVersionService;