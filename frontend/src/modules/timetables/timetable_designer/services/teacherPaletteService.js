import api
    from '../../../../services/api/axios';

export const ENDPOINT =
    '/staff/staff-profiles/';

const teacherPaletteService = {

    getAll: () =>

        api.get(
            ENDPOINT
        ),

};

export default teacherPaletteService;